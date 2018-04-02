# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models


# Create your models here.


class UserInfo(models.Model):
    password = models.CharField(max_length=100, verbose_name=u"密码")
    email = models.EmailField(verbose_name=u"邮箱")
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称 ", default="游客")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female", verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u"", verbose_name=u"详细地址")
    city = models.CharField(max_length=10,default="", verbose_name=u"所在城市")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号", default=u"")
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image/user/%Y%m", default="image/user/default", max_length=100)
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=30, choices=(("register", u"注册"), ("forget", u"忘记密码"), ("update_email", u"修改邮箱")), verbose_name=u"类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Message(models.Model):
    send_to = models.IntegerField(verbose_name=u"发送对象")
    message = models.TextField(verbose_name=u"信息内容")
    has_read = models.BooleanField(verbose_name=u"是否已读", default=False)
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"方送时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name





