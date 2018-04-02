# _*_ coding: utf-8 _*_
__date__ = '2018/3/14 12:36'
from users.models import EmailVerifyRecord
from MealOrderingOnline.settings import EMAIL_FROM
import random
from django.core.mail import send_mail


def send_register(email, send_type="register", send_to="user"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_to == "user":
        if send_type == "register":
            email_title = "好吃网在线注册"
            email_body = "请点击链接激活您的账号：http://127.0.0.1:8000/active/{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass
        elif send_type == "forget":
            email_title = "好吃网密码重置"
            email_body = "请点击链接重置您的账号密码：http://127.0.0.1:8000/user_reset/{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass
        elif send_type == "update_email":
            email_title = "好吃网邮箱修改验证码"

            email_body = "你的邮箱验证码为：{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass
    else:
        if send_type == "forget":
            email_title = "好吃网密码重置"
            email_body = "请点击链接重置您的账号密码：http://127.0.0.1:8000/business/reset/{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass
        elif send_type == "register":
            email_title = "好吃网在线注册"
            email_body = "请点击链接激活您的账号：http://127.0.0.1:8000/business/active/{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass




def random_str(randlenth):
    str = ''
    Chars = 'ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    lenth = len(Chars)-1
    for i in range(randlenth):
        str = str + Chars[random.randint(0, lenth)]
    return str


