from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    email = models.EmailField(unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=32, verbose_name='密码')

    class Meta:
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username

class bookMark(models.Model):
    icon = models.ImageField(upload_to='')
    urls = models.URLField()
    title = models.
    description = models.

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    icon = models.ImageField(upload_to='bookmarks/icons/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name