from django.shortcuts import render
from django.core import mail
from django.core.cache import cache
from django.contrib import messages
from django.conf import settings
import random, time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.utils import create_jwt, verify_jwt, refresh_jwt
from user import models
import json


# Create your views here.

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']
        try:
            user = models.UserInfo.objects.get(email=email, password=password)
        except models.UserInfo.DoesNotExist:
            messages.error(request, '用户不存在或密码错误')
            return render(request, 'login.html')
        new_token = create_jwt(user.id)
        messages.success(request, '登录成功')
        return JsonResponse({'messages': '登录成功', 'token': new_token})


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']
        code = request.POST.get['code']
        try:
            user = models.UserInfo.objects.get(email=email)
        except models.UserInfo.DoesNotExist:
            user = None
        if user is not None:
            if code == '':
                messages.error(request, '请输入验证码')
                return render(request, 'register.html')
            elif code == cache.get(email):
                cache.delete(email)
                models.UserInfo.objects.create(username=email, email=email, password=password)
                messages.success(request, '注册成功')
                return render(request, 'login.html')
            elif code != cache.get(email):
                messages.error(request, '验证码错误')
                return render(request, 'register.html')
        else:
            messages.error(request, '用户已存在')
            return render(request, 'register.html')


# 找回密码
def retrieve(request):
    if request.method == 'GET':
        return render(request, 'retrieve.html')
    elif request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']
        code = request.POST.get['code']
        try:
            user = models.UserInfo.objects.get(email=email)
        except models.UserInfo.DoesNotExist:
            messages.error(request, '用户不存在')
            return render(request, 'retrieve.html')
        if code == '':
            messages.error(request, '请输入验证码')
            return render(request, 'retrieve.html')
        elif code == cache.get(email):
            cache.delete(email)
            user.password = password
            user.save()
            messages.success(request, '验证成功')
            return render(request, 'login.html')
        elif code != cache.get(email):
            messages.error(request, '验证码错误')
            return render(request, 'retrieve.html')


# 发送邮箱验证码
def send_email(request):
    email = request.POST.get['email']
    chars = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWSYZ0123456789'
    code = ''.join([str(random.choice(chars)) for _ in range(6)])
    mail.send_mail(
        subject='你的验证码',  # 题目
        message=f'欢迎使用书签，为保证您的正常使用，请输入下面的验证码\n{code}\n注意：验证码的有效期为10分钟',  # 消息内容
        from_email=settings.DEFAULT_FROM_EMAIL,  # 发送者[当前配置邮箱]
        recipient_list=[email],  # 接收者邮件列表
        fail_silently=False,
    )
    cache.set(code, code, 600)  # （键，赋给键的值，缓存时间）
    messages.success(request, '发送成功')
    return render(request, 'send_email.html')  # 需要加入自动跳转至上一页面的功能


# 检查token有效性
@csrf_exempt
def check_token_validity(request):
    if request.method == 'POST':
        token = request.headers.get('X-Token')
        valid, result = verify_jwt(token)
        if not valid:
            response_data = {'code': 1234, 'message': result, 'data': {}}
        else:
            response_data = {'code': 0, 'message': 'Token有效', 'data': {}}
        return JsonResponse(response_data)


# 刷新token
@csrf_exempt
def refresh_token(request):
    if request.method == 'POST':
        old_token = request.headers.get('X-Token')  # 从请求头中获取旧的token
        success, result = refresh_jwt(old_token)  # 如果旧的token存在并且已经过期
        if success:
            response_data = {'code': 0, 'message': '成功刷新Token', 'data': {'token': result}}
        else:
            response_data = {'code': 1234, 'message': result, 'data': {}}
        return JsonResponse(response_data)
