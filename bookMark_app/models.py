from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UseInfo(models.Model):
    portrait = models.ImageField(upload_to='portrait', default='portrait.jpg', verbose_name='头像')
    user_name = models.CharField(max_length=32, verbose_name='用户名')
    account = models.CharField(max_length=32, verbose_name='账号', unique=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    mailbox = models.EmailField(unique=True, verbose_name='邮箱')
    phone_number = PhoneNumberField(unique=True, verbose_name='手机号')

    class Meta:
        verbose_name_plural = '个人信息'

    def __str__(self):
        return self.user_name

class School(models.Model):
    school = models.CharField(max_length=32, verbose_name='学校')

    class Meta:
        verbose_name_plural = '学校信息'

    def __str__(self):
        return self.school
    # 学校信息