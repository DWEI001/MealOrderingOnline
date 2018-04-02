from django.db import models
from datetime import datetime

from users.models import UserInfo
from business.models import Business


class Ordering(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=u"用户")
    bname = models.CharField(max_length=50, verbose_name=u"商家名称", default="")
    bimage = models.ImageField(default="")
    bid = models.IntegerField(default=0, verbose_name=u"商家ID")
    status = models.CharField(max_length=30, default="5",
                              choices=(("1", u"已付款"), ("2", u"已接单"), ("3", u"配送中"), ("4", u"已完成"), ("5", u"未付款")))
    total = models.FloatField(default=0.0, verbose_name=u"总价")
    address = models.CharField(max_length=50, default="", verbose_name=u"收货地址")
    is_pay = models.BooleanField(default=False)
    content = models.TextField(verbose_name=u"留言", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
         return self.business.bname


class OrderDetail(models.Model):
    orderid = models.ForeignKey(Ordering, verbose_name=u"订单号", default=1)
    name = models.CharField(max_length=50, verbose_name=u"菜名")
    count = models.IntegerField(verbose_name=u"数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"单价")
    discount = models.FloatField(default=1.0, verbose_name=u"折扣")
    image = models.ImageField(default="")

    class Meta:
        verbose_name = u"订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


