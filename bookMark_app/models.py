from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    email = models.EmailField(unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=32, verbose_name='密码')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    class Meta:
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username


class Category(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='大类名')

    def __str__(self):
        return self.name


class bookMark(models.Model):
    icon = models.ImageField(blank=True, null=True, upload_to='bookmarks/icons/', verbose_name='网站图标')
    urls = models.URLField(verbose_name='url地址')
    title = models.CharField(max_length=200, verbose_name='网站名称')
    description = models.TextField(blank=True, null=True, verbose_name='网站介绍')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """待细看"""
    access_time = models.DateTimeField(verbose_name="访问时间")
    access_number = models.IntegerField(verbose_name="访问次数")
    user = models.ForeignKey('Information', on_delete=models.CASCADE())
    sort = models.ForeignKey('Category', on_delete=models.CASCADE())

    def __str__(self):
        return self.title


class bookMark_recommend(models.Model):
    """推荐书签"""
    bookMark = models.ForeignKey(bookMark, on_delete=models.CASCADE)
