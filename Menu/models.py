from django.db import models
from business.models import Business
from datetime import datetime
# Create your models here.


class MenuType(models.Model):
    type = models.CharField(max_length=20,   verbose_name=u"菜品类型")

    class Meta:
        verbose_name = u"菜品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type


class MenuInfo(models.Model):
    business = models.ForeignKey(Business, verbose_name=u"商家名称")
    menu_type = models.CharField(max_length=30, verbose_name=u"菜品类型",default="")
    mname = models.CharField(max_length=100, verbose_name=u"菜品名称")
    mprice = models.FloatField(default=0.0, verbose_name=u"单价")
    mimage = models.ImageField(upload_to="image/menu/%Y%m", max_length=100, verbose_name=u"菜品封面")
    discount = models.FloatField(verbose_name=u"折扣", default=1.0)
    people_num = models.IntegerField(default=0, verbose_name=u"点餐人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"菜品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mname




