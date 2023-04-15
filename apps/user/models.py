from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    email = models.EmailField(unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=32, verbose_name='密码')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    class Meta:
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username

