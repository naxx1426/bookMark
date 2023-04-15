from django.db import models


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
    mark_name = models.CharField(verbose_name="网站名称", max_length=20)
    url = models.URLField(verbose_name="网址")
    introduction = models.CharField(verbose_name="网站简要信息")
    icon = models.URLField(verbose_name="图标地址", default="//")
    access_time = models.DateTimeField(verbose_name="访问时间")
    access_number = models.IntegerField(verbose_name="访问次数")
    user = models.ForeignKey('Information', on_delete=models.CASCADE())
    sort = models.ForeignKey('Category', on_delete=models.CASCADE())
