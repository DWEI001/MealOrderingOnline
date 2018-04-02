# _*_ coding: utf-8 _*_
from django.shortcuts import render
import json
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse


from .models import UserInfo, EmailVerifyRecord, Message
from business.models import Business, City, BusinessMessage
from utils.email_send import send_register
# Create your views here.


# 用户注册
class UserRegisterView(View):

    def get(self, request):
        return render(request, "user_register.html")

    def post(self, request):
        user_email = request.POST.get("email", "")
        user_password = request.POST.get("password", "")
        try:
            user_check = UserInfo.objects.get(email=user_email)
        except Exception as e:
            user_check = None
        if user_check is not None:
            return render(request, "user_register.html", {'msg': "该邮箱已注册过！"})
        user = UserInfo()
        user.email = user_email
        user.password = user_password
        user.save()
        send_register(user_email, "register")
        return render(request, "user_register.html", {'msg': "注册成功！请登陆邮箱点击链接激活账户！"})


# 用户激活
class UserActiveView(View):
    def get(self, request, active_code):
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                user = UserInfo.objects.get(email=email)
                user.is_active = True
                user.save()
                message = Message()
                message.send_to = user.id
                message.message = "欢迎注册好吃网在线订餐系统账号"
                message.save()
            return render(request, "user_login.html")
        else:
            return render(request, "active_fail.html")


# 用户忘记密码
class UserForgetView(View):
    def get(self, request):
        return render(request, "user_forgetpwd.html")

    def post(self, request):
        email = request.POST.get("email", "")
        try:
            user_check = UserInfo.objects.get(email=email)
        except Exception as e:
            user_check = None
        if user_check:
            send_register(email, "forget")
            return render(request, "user_forgetpwd.html", {'msg': "重置密码链接已发送！请查收！"})
        else:
            return render(request, "user_forgetpwd.html", {'msg': "该账号未注册！"})


# 用户重置密码
class UserResetView(View):
    def get(self, request, active_code):
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                return render(request, "user_password_reset.html", {'email': email})


# 用户修改密码
class UserModifyView(View):
    def post(self, request):
        email = request.POST.get("email", "")
        password1 = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        if password1 == password2:
            user = UserInfo.objects.get(email=email)
            user.password = password1
            user.save()
            message = Message()
            message.send_to = user.id
            message.message = "您的密码已修改成功"
            message.save()
            respose = HttpResponseRedirect('/user_login/')
            return respose
        else:
            return render(request, "user_password_reset.html", {'msg': "两次输入的密码不一致，请重新输入", 'email': email})


# 用户登陆
class UserLoginView(View):
    def get(self, request):
        return render(request, "user_login.html")

    def post(self, request):
        busin_all = Business.objects.all()
        user_name = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        try:
            user = UserInfo.objects.get(email=user_name, password=pwd)
        except Exception as e:
            user = None
        if user is not None:
            if user.is_active:
                user.status = True
                request.session['username'] = user.nick_name
                request.session['userid'] = user.id
                request.session['userimage'] = user.image.name
                request.session['useraddress'] = user.address
                request.session['userphone'] = user.mobile
                request.session['usergender'] = user.gender
                request.session['useremail'] = user.email
                user.save()
                return HttpResponseRedirect('/')
            else:
                return render(request, "user_login.html", {"msg": "用户未激活！"})

        else:
            return render(request, "user_login.html", {"msg": "用户名或者密码错误！"})


# 用户退出登录
class UserLogoutView(View):
    def get(self, request):
        del request.session['username']
        del request.session['userid']
        del request.session['userimage']
        return HttpResponseRedirect('/')


# 用户个人中心
class UserInfoView(View):
    def get(self, request):
        return render(request, "usercenter-info.html")

    def post(self, request):
        userid = request.session.get("userid", "")
        user = UserInfo.objects.get(id=userid)
        username = request.POST.get("nick_name", "")
        gender = request.POST.get("gender", "")
        address = request.POST.get("address", "")
        mobile = request.POST.get("mobile", "")
        user.nick_name = username
        user.address = address
        user.mobile = mobile
        user.gender = gender
        user.save()
        data ={}
        data["status"] = "success"
        data["msg"] = "保存成功"
        return HttpResponse(json.dumps(data), content_type="application/json")


# 个人中心修改密码
class UpdatePwdView(View):
    def post(self,request):
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        user = UserInfo.objects.get(id=request.session.get("userid"))
        data = {}
        if password1 == password2:
            user.password = password1
            user.save()
            data['status'] = "success"
            data["msg"] = "密码修改成功"
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data['status'] = "fail"
            data['msg'] = "密码不一致"
            return HttpResponse(json.dumps(data), content_type="application/json")


# 个人中心修改头像
class UploadImageView(View):
    def post(self, request):
        user = UserInfo.objects.get(id=request.session.get('userid'))
        user.image = request.FILES['image']
        user.save()
        request.session['userimage'] = user.image
        data = {}
        data['status'] = "success"
        data["msg"] = "修改成功"
        return HttpResponse(json.dumps(data), content_type="application/json")


# 发送邮箱验证码并修改邮箱
class UpdateEmailView(View):
    def get(self, request):
        """
        获取邮箱验证码
        """
        email = request.GET.get("email", "")
        data = {}
        if UserInfo.objects.filter(email=email):
            data["email"] = "该邮箱已经注册过"
            return HttpResponse(json.dumps(data), content_type="application/json")
        send_register(email, "update_email")
        data["status"] = "success"
        return HttpResponse(json.dumps(data), content_type="application/json")

    def post(self, request):
        """
        修改邮箱
        :param request:
        :return:
        """
        email = request.POST.get("email", "")
        code = request.POST.get("code", "")
        data = {}
        exist_code = EmailVerifyRecord.objects.filter(email=email, code=code, send_type="update_email")
        if exist_code:
            userid = request.session.get("userid","")
            user = UserInfo.objects.get(id=userid)
            user.email = email
            user.save()
            data["status"] = "success"
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data["email"] = "验证码出错"
            return HttpResponse(json.dumps(data), content_type="application/json")


# 用户消息
class UserMessageView(View):
    def get(self, request):
        userid = request.session.get("userid", "")
        all_messages = Message.objects.filter(send_to=userid).order_by("-send_time")
        unread = all_messages.filter(has_read=False).count()
        return render(request, "user_message.html", {
            "messages": all_messages,
            "unread": unread
                                                     })


# 网站首页
class IndexView(View):
    def get(self, request):
        busin_all = Business.objects.all()
        bus_nums = busin_all.count()
        all_citys = City.objects.all()
        city_id = request.GET.get("city", "")
        if city_id:
            busin_all = busin_all.filter(city_id=int(city_id))
        pagintor = Paginator(busin_all, 10)
        page = request.GET.get('page')
        try:
            business = pagintor.page(page)
        except PageNotAnInteger:
            business = pagintor.page(1)
        except EmptyPage:
            business = pagintor.page(pagintor.num_pages)

        return render(request, "index.html", {
            "all_business": business,
            "all_city": all_citys,
            "business_nums": bus_nums
                                                      })






