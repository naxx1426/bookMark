from django.shortcuts import render
from django.contrib import messages
import random
import string
from twilio.rest import Client
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
            verification_code = ''
            for x in range(6):
                verification_code += random.choice(chars)
            send_sms(user.phone_number, verification_code)
            # 将带有验证码的用户实例作为session变量存储
            request.session['user'] = user
            request.session['verification_code'] = verification_code
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
        input_code = request.POST.get('verification_code')
        if input_code == request.session.get('verification_code'):
            user = request.session.get('user')
            user.save()
            messages.error(request, '你的账号创建成功')
            return render(request, 'bookMark_app/success.html')
        else:
            messages.error(request, '验证失败，请重新尝试')
            return render(request, 'bookMark_app/failed.html')
    return render(request, 'bookMark_app/verify.html')
