
from datetime import datetime

from django.db import models
from users.models import UserInfo

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"城市名称")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Business(models.Model):
    bname = models.CharField(max_length=300, verbose_name=u"名称",default=u"默认名称")
    bpassword = models.CharField(max_length=100, verbose_name=u"密码")
    bphone = models.CharField(max_length=11, verbose_name=u"电话", default="")
    bemail = models.EmailField(verbose_name=u"邮箱")
    baddress = models.CharField(max_length=300, verbose_name=u"详细地址",default="")
    city = models.ForeignKey(City, verbose_name=u"城市", default=1)
    hit_nums = models.IntegerField(default=0, verbose_name=u"点餐人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    bstatus = models.BooleanField(default=False, verbose_name=u"在线状态")
    is_active = models.BooleanField(default=False, verbose_name=u"激活状态")
    bimage = models.ImageField(upload_to="image/business/%Y%m", default="image/business/default", max_length=100)
    bcreate_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"商家信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bname


class UserFavorite(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"收藏数据")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class BusinessMessage(models.Model):
    send_to = models.IntegerField(verbose_name=u"发送对象")
    message = models.TextField(verbose_name=u"信息内容")
    has_read = models.BooleanField(verbose_name=u"是否已读", default=False)
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"方送时间")

    class Meta:
        verbose_name = u"商家消息"
        verbose_name_plural = verbose_name

