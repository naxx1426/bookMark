from django.db import models

# Create your models here.

class UseInfo(models.Model):
    portrait = models.ImageField(upload_to='portrait', default='portrait.jpg', verbose_name='头像')
    user_name = models.CharField(max_length=32, verbose_name='用户名')
    account = models.CharField(max_length=32, verbose_name='账号', unique=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    region = models.CharField(max_length=32, verbose_name='地区')