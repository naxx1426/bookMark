from django.db import models
from apps.user.models import UserInfo

# Create your models here.
class Category(models.Model):
    """
    分类
    """
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='分类名称')

    def __str__(self):
        return self.name

class Bookmark_recommend(models.Model):
    """ 推荐书签 """
    mark_name = models.CharField(verbose_name="网站名称", max_length=20)
    url = models.URLField(verbose_name="网址")
    introduction = models.CharField(verbose_name="网站简要信息")
    icon = models.URLField(verbose_name="图标地址", default="//")


class Bookmark(models.Model):
    """ 书签 """
    title = models.CharField(verbose_name="网站名称", max_length=20)
    default_icon = models.ImageField(upload_to='bookmarks/icons/', blank=True, null=True,
                                     verbose_name='自动爬取的网站图标')
    custom_icon = models.ImageField(upload_to='bookmarks/icons/', blank=True, null=True,
                                    verbose_name='用户上传的网站图标')
    urls = models.URLField(verbose_name='url地址')
    description = models.TextField(blank=True, null=True, verbose_name='网站介绍')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='书签对应的用户')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='书签所处的分类')
    """待细看"""
    access_time = models.DateTimeField(verbose_name="访问时间")
    access_number = models.IntegerField(verbose_name="访问次数")

    @property
    def icon(self):
        return self.custom_icon or self.default_icon

    def __str__(self):
        return self.title
