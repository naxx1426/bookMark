import random

from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.user import models
from .utils import create_jwt, verify_jwt, refresh_jwt
from .. import user


# Create your views here.

# 登录
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            login_user = user.models.UserInfo.objects.get(email=email, password=password)
        except user.models.UserInfo.DoesNotExist:
            return JsonResponse({'messages': '用户不存在或密码错误', 'token': {}})
        new_token = create_jwt(login_user.id)
        return JsonResponse({'messages': '登录成功', 'token': new_token})


# 注册
def register(request):
    if request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']
        code = request.POST.get['code']
        try:
            register_user = user.models.UserInfo.objects.get(email=email)
        except user.models.UserInfo.DoesNotExist:
            register_user = None
        if user is not None:
            if code == '':
                return JsonResponse({'messages': '请输入验证码'})
            elif code == cache.get(email):
                cache.delete(email)
                user.models.UserInfo.objects.create(username=email, email=email, password=password)
                return JsonResponse({'messages': '注册成功'})
            elif code != cache.get(email):
                return JsonResponse({'messages': '验证码错误'})
        else:
            return JsonResponse({'messages': '用户已存在'})


# 找回密码
def retrieve(request):
    if request.method == 'GET':
        return render(request, 'retrieve.html')
    elif request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']
        code = request.POST.get['code']
        try:
            retrieve_user = user.models.UserInfo.objects.get(email=email)
        except user.models.UserInfo.DoesNotExist:
            return JsonResponse({'messages': '用户不存在'})
        if code == '':
            return JsonResponse({'messages': '请输入验证码'})
        elif code == cache.get(email):
            cache.delete(email)
            retrieve_user.password = password
            retrieve_user.save()
            return JsonResponse({'messages': '验证成功'})
        elif code != cache.get(email):
            return JsonResponse({'messages': '验证码错误'})


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
    return JsonResponse({'messages': '发送成功'})


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
