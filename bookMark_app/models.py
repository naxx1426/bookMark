from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class UseInfo(models.Model):
    portrait = models.ImageField(upload_to='portrait', default='portrait.jpg', verbose_name='头像')
    user_name = models.CharField(max_length=32, verbose_name='用户名')
    account = models.CharField(max_length=32, verbose_name='账号', unique=True)
    phone_number = PhoneNumberField(unique=True, verbose_name='手机号')
    password = models.CharField(max_length=32, verbose_name='密码')
    mailbox = models.EmailField(unique=True, verbose_name='邮箱')
    introduction = RichTextUploadingField(verbose_name='个人简介')

    class Meta:
        verbose_name_plural = '个人信息'

    def __str__(self):
        return self.user_name


class Category(models.Model):
    user = models.ForeignKey('UseInfo', on_delete=models.CASCADE, verbose_name='用户')
    category = models.CharField(max_length=32, verbose_name='书签分类')

    class Meta:
        verbose_name_plural = '书签分类'

    def __str__(self):
        return self.category
    # 书签分类


class Subcategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='书签分类')
    subcategory = models.CharField(max_length=32, verbose_name='书签子类')

    class Meta:
        verbose_name_plural = '书签子类'

    def __str__(self):
        return self.subcategory

    # 书签子类
