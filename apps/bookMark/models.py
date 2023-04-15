from django.db import models

from apps.user.models import User


# Create your models here.
class Category(models.Model):
    """
    分类
    """
    sort_name = models.CharField(verbose_name="分类名称", max_length=10)
    user = models.ForeignKey(to=User, related_name='Category', on_delete=models.CASCADE, verbose_name="所属用户")

    def __str__(self):
        return self.sort_name


# class Bookmark_recommend(models.Model):
#     """ 推荐书签 """
#     mark_name = models.CharField(verbose_name="网站名称", max_length=20)
#     url = models.URLField(verbose_name="网址")
#     introduction = models.CharField(verbose_name="网站简要信息")
#     icon = models.URLField(verbose_name="图标地址", default="//")
#     updated = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#
#     def __str__(self):
#         return self.mark_name


class Bookmark(models.Model):
    """ 书签 """
    CHOICE = (
        (0, "否"),
        (1, "是")
    )
    mark_name = models.CharField(verbose_name="网站名称", max_length=20)
    url = models.URLField(verbose_name="网址")
    introduction = models.CharField(verbose_name="网站简要信息")
    icon = models.URLField(verbose_name="图标地址", default="//")
    access_time = models.DateTimeField(verbose_name="访问时间")
    access_number = models.IntegerField(verbose_name="访问次数")
    isRecommond = models.IntegerField(verbose_name="是否是推荐书签", default=0, choices=CHOICE)
    user = models.ForeignKey(to=User, related_name="bookMark", on_delete=models.CASCADE)
    sort = models.ForeignKey(to=Category, related_name="bookMark", on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.mark_name
