from django.shortcuts import render
from smtplib import SMTPRecipientsRefused
from django.contrib import messages
import random
import string
from twilio.rest import Client
from django.core import mail
from .models import UseInfo
from .forms import UserInfoForm
# Create your views here.

def index(request):
    return render(request, 'bookMark_app/index.html')
def register(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.account_id = generate_account_id()
            #创建并发送验证码
            chars = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWSYZ0123456789'
            phone_verification_code = ''
            mailbox_verification_code = ''
            for x in range(6):
                phone_verification_code += random.choice(chars)
                mailbox_verification_code += random.choice(chars)
            send_sms(user.phone_number, phone_verification_code)
            mail.send_mail(
                subject='你的验证码',  # 题目
                message='欢迎使用盲盒，为保证您的正常使用，请输入下面的验证码\n' + mailbox_verification_code +
                        '\n注意：验证码的有效期为30分钟',
                 # 消息内容
                from_email='2228795091@qq.com',  # 发送者[当前配置邮箱]
                 recipient_list=[user.mailbox],  # 接收者邮件列表
            )
            # 将带有验证码的用户实例作为session变量存储
            request.session['user'] = user
            request.session['phone_verification_code'] = phone_verification_code
            request.session['mailbox_verification_code'] = mailbox_verification_code
            return render(request, 'bookMark_app/verify.html')
    else:
        form = UserInfoForm()
    return render(request, 'bookMark_app/register.html', {'form': form})

def generate_account_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

def send_sms(phone_number, code):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"你的验证码为: {code}",
        from_='+1234567890',  # 在示例代码中替换为您自己的Twilio电话号码
        to=str(phone_number)
    )

def verify(request):
    if request.method == 'POST':
        input_phone_code = request.POST.get('phone_verification_code')
        input_mailbox_code = request.POST.get('mailbox_verification_code')
        if input_phone_code == request.session.get('phone_verification_code')\
                and input_mailbox_code == request.session.get('mailbox_verification_code'):
            user = request.session.get('user')
            user.save()
            messages.error(request, '你的账号创建成功')
            return render(request, 'bookMark_app/index.html')
        else:
            messages.error(request, '验证失败，请重新尝试')
            return render(request, 'bookMark_app/failed.html')
    return render(request, 'bookMark_app/verify.html')