# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from utils.email_send import send_register

from business.models import Business, UserFavorite, BusinessMessage
from Menu.models import MenuInfo
from users.models import UserInfo, EmailVerifyRecord, Message
from Ordering.models import Ordering, OrderDetail
# Create your views here.


class BusinessRegisterView(View):

    def get(self, request):
        return render(request, "business_register.html")

    def post(self, request):
        business_email = request.POST.get("email", "")
        business_password = request.POST.get("password", "")
        try:
            business_check = Business.objects.get(Bemail=business_email)
        except Exception as e:
            business_check = None
        if business_check is not None:
            return render(request, "business_register.html", {'msg': "该邮箱已注册过！"})
        business = Business()
        business.bemail = business_email
        business.bpassword = business_password
        business.save()
        send_register(business_email, "register", send_to="business")
        return render(request, "business_register.html", {'msg': "注册成功！请登陆邮箱点击链接激活账户！"})


# 激活
class BusinessActiveView(View):
    def get(self, request, active_code):
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                business = Business.objects.get(bemail=email)
                business.is_active = True
                business.save()
                return HttpResponseRedirect('/business/login/')
        else:
            return render(request, "active_fail.html")


# 忘记密码
class BusinessForgetView(View):
    def get(self, request):
        return render(request, "business_forgetpwd.html")

    def post(self, request):
        email = request.POST.get("email", "")
        try:
            business_check = Business.objects.get(bemail=email)
        except Exception as e:
            business_check = None
        if business_check:
            send_register(email, "forget", send_to="business")
            return render(request, "business_forgetpwd.html", {'msg': "重置密码链接已发送！请查收！"})
        else:
            return render(request, "business_forgetpwd.html", {'msg': "该账号已注册！"})


# 重置密码链接
class BusinessResetView(View):
    def get(self, request, active_code):
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                return render(request, "business_password_reset.html", {'email': email})
        else:
            return render(request, "active_fail.html")


# 修改密码
class BusinessModifyView(View):
    def post(self, request):
        email = request.POST.get("email", "")
        password1 = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        if password2 == "" or password1 == "":
            return render(request, "business_password_reset.html", {'msg': "密码不能为空", 'email': email})
        if password1 == password2:
            business = Business.objects.get(bemail=email)
            business.bpassword = password1
            business.save()
            respose = HttpResponseRedirect('/business/login/')
            return respose
        else:
            return render(request, "business_password_reset.html", {'msg': "两次输入的密码不一致，请重新输入", 'email': email})


class BusinessLoginView(View):
    def get(self, request):
        return render(request, "business_login.html")

    def post(self, request):
        business_name = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        try:
            business = Business.objects.get(bemail=business_name, bpassword=pwd)
        except Exception as e:
            business = None
        if business is not None:
                request.session['bname'] = business.bname
                request.session['bid'] = business.id
                request.session['bimage'] = business.bimage.name
                request.session['baddress'] = business.baddress
                request.session['bphone'] = business.bphone
                request.session['bemail'] = business.bemail
                business.bstatus = True
                business.save()
                return render(request, "businessinfo.html")
        else:
            return render(request, "business_login.html", {"msg": "用户名或者密码错误！"})


class BusinessLogoutView(View):
    def get(self, request):
        del request.session['bname']
        del request.session['bid']
        del request.session['bimage']
        del request.session['baddress']
        del request.session['bemail']
        return HttpResponseRedirect('/')


class BusinessMenuView(View):
    def get(self,request):
        businessid = request.session.get("bid", "")
        all_menu = MenuInfo.objects.filter(business_id=businessid)
        return render(request, "business_menu.html", {"all_munu": all_menu})


class BusinessInfoView(View):
    def get(self, request):
        return render(request, 'businessinfo.html')

    def post(self, request):
        bid = request.session.get("bid", "")
        business = Business.objects.get(id=bid)
        name = request.POST.get("nick_name", "")
        address = request.POST.get("address", "")
        mobile = request.POST.get("mobile", "")
        business.bname = name
        business.baddress = address
        business.bphone = mobile
        business.save()
        data = {}
        data["status"] = "success"
        data["msg"] = "保存成功"
        return HttpResponse(json.dumps(data), content_type="application/json")


class UpdateBusEmailView(View):
    def get(self, request):
        """
        获取邮箱验证码
        """
        email = request.GET.get("email", "")
        data = {}
        if Business.objects.filter(bemail=email):
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
            businessid = request.session.get("bid", "")
            business = Business.objects.get(id=businessid)
            business.bemail = email
            business.save()
            data["status"] = "success"
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data["email"] = "验证码出错"
            return HttpResponse(json.dumps(data), content_type="application/json")


class UploadMenuImageView(View):
    def post(self, request, menu_id):
        menu = MenuInfo.objects.get(id=menu_id)
        menu.mimage = request.FILES['image']
        menu.save()
        data = {}
        data['status'] = "success"
        data["msg"] = "修改成功"
        return HttpResponse(json.dumps(data), content_type="application/json")


class UpdatePwdView(View):
    def post(self, request):
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        user = Business.objects.get(id=request.session.get("bid"))
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


class UploadBusinessImageView(View):
    def post(self, request):
        user = Business.objects.get(id=request.session.get('bid'))
        user.bimage = request.FILES['image']
        user.save()
        request.session['bimage'] = user.image
        data = {}
        data['status'] = "success"
        data["msg"] = "修改成功"
        return HttpResponse(json.dumps(data), content_type="application/json")


class MenuDetailView(View):
    def get(self, request, menu_id):
        menu = MenuInfo.objects.get(id=menu_id)
        return render(request, "menu_info.html", {"menu": menu})


class AddMenuView(View):
    def get(self, request):
        return render(request, "addmenu.html")

    def post(self, request):
        name = request.POST.get("name", "")
        price = request.POST.get("price", "")
        discount = request.POST.get("discount", "")
        type = request.POST.get("type", "")
        menu = MenuInfo()
        menu.mname = name
        menu.mprice = price
        menu.discount = discount
        menu.menu_type = type
        menu.business_id = request.session.get("bid", "")
        menu.save()
        return HttpResponseRedirect('/business/add_menu/')


class BusinessOrderView(View):
    def get(self, request):
        businessid = request.session.get("bid", "")
        all_orders = Ordering.objects.filter(bid=businessid, is_pay=1)
        count = all_orders.count()
        return render(request, "business_order_list.html", {
            "all_orders": all_orders,
            "count": count
                                                            })


class BusinessOrderDetailView(View):
    def get(self, request, order_id):
        order_detail = OrderDetail.objects.filter(orderid_id=order_id)
        order = Ordering.objects.get(id=order_id)
        return render(request, "business_order_detail.html", {
            "order_detail": order_detail,
            "order": order
                                                              })


class BusinessCheckoutView(View):
    def post(self, request, order_id):
        order = Ordering.objects.get(id=order_id)
        status = request.POST.get("状态")
        message = Message()
        message.send_to = order.user_id
        if status == "1":
            order.status = "2"
            message.message = "商家已收到您的订单，正在为您准备菜品"
        elif status == "2":
            order.status = "3"
            message.message = "您的外卖正在配送中，请注意外卖骑手的通知"
        else:
            order.status = "4"
            message.message = "您的订单已完成，谢谢您的下次光临！"
        order.save()
        message.save()
        order_detail = OrderDetail.objects.filter(orderid_id=order_id)
        return render(request, "business_order_detail.html", {
            "order_detail": order_detail,
            "order": order
                                                              })


class BusinessMessageView(View):
    def get(self, request):
        businessid = request.session.get("bid", "")
        messages = BusinessMessage.objects.filter(send_to=businessid)
        unread_nums = BusinessMessage.objects.filter(has_read=False).count()
        return render(request, "business_message.html", {
            "messages": messages,
            "unread_nums": unread_nums
        })


class BusinessHomeView(View):
    def get(self, request, business_id):
        has_fav = False
        request.session['businessid'] = business_id
        userid = request.session.get("userid")
        if userid:
            if UserFavorite.objects.filter(fav_id=business_id, user_id=userid):
                has_fav = True
        business = Business.objects.get(id=int(business_id))
        all_menus = MenuInfo.objects.filter(business_id=int(business_id))
        all_types = []
        for menu in all_menus:
            type = menu.menu_type
            if type not in all_types:
                all_types.append(type)
        return render(request, "business-detail-homepage.html", {
            "business": business,
            "all_menus": all_menus,
            "all_types": all_types,
            "has_fav": has_fav
        })


class UserFavoriteView(View):
    def get(self, request):
        userid = request.session.get("userid", "")
        all_fav = UserFavorite.objects.filter(user_id=userid)
        all_business = []
        for item in all_fav:
            all_business.append(Business.objects.get(id=item.fav_id))
        return render(request, "favorite.html", {
            "all_fav": all_business
                                                 })

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        data = {}
        business = Business.objects.get(id=fav_id)
        userid = request.session.get('userid')
        if userid is None:
            data['status'] = "fail"
            data["msg"] = "用户未登录"
            return HttpResponse(json.dumps(data), content_type="application/json")
        try:
            exist_record = UserFavorite.objects.get(user_id=userid, fav_id=int(fav_id))
        except Exception as e:
            exist_record = None
        if exist_record is None:
            user_fav = UserFavorite()
            if int(fav_id) > 0:
                business.fav_nums = business.fav_nums + 1
                business.save()
                user_fav.fav_id = int(fav_id)
                user_fav.user_id = userid
                user_fav.save()
                data['status'] = "success"
                data["msg"] = "已收藏"
                return HttpResponse(json.dumps(data), content_type="application/json")
            else:
                data['status'] = "fail"
                data["msg"] = "收藏出错"
                return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            business.fav_nums = business.fav_nums - 1
            business.save()
            exist_record.delete()
            data['status'] = "success"
            data["msg"] = "收藏"
            return HttpResponse(json.dumps(data), content_type="application/json")


class UserAddOrderView(View):
    def get(self, request):
        # 获取用户信息
        userid = request.session.get("userid", "")
        # 根据用户id查找订单记录
        all_order = Ordering.objects.filter(user_id=userid)
        # 获取订单数量
        count = all_order.count()
        # 分页
        pagintor = Paginator(all_order, 5)
        page = request.GET.get('page')
        try:
            all_order = pagintor.page(page)
        except PageNotAnInteger:
            all_order = pagintor.page(1)
        except EmptyPage:
            all_order = pagintor.page(pagintor.num_pages)
        return render(request, "order-list.html", {
            "all_order": all_order,
            "all_nums": count
        })

    def post(self, request):
        userid = request.session.get("userid")
        businessid = request.session.get("businessid")
        if userid is None:
            return HttpResponseRedirect('/user_login/')
        # 获取用户和商家信息
        user = UserInfo.objects.get(id=userid)
        business = Business.objects.get(id=businessid)
        business.hit_nums = business.hit_nums + 1
        business.save()
        # 实例化订单对象
        order = Ordering()
        order.user_id = userid
        order.address = user.address
        order.bid = business.id
        order.bimage = business.bimage
        order.bname = business.bname
        order.save()
        count = 0
        i = 1
        total = 0
        menu = "hello"
        for temp in request.POST:
            count = count + 1
            # 获取用户订单号，向订单详情中添加数据
        orderid = Ordering.objects.order_by("-add_time")[0].id
        while i < int(count/3):
            menu = request.POST.get("item_name_{0}".format(i))
            quantity = request.POST.get("quantity_{0}".format(i))
            try:
                menu = MenuInfo.objects.get(business_id=businessid, mname=menu)
            except Exception as e:
                menu = None
            if menu:
                order_detail = OrderDetail()
                order_detail.orderid_id = orderid
                order_detail.name = menu.mname
                order_detail.count = quantity
                order_detail.price = menu.mprice
                order_detail.discount = menu.discount
                order_detail.image = menu.mimage
                order_detail.save()
                total = total + menu.mprice * float(quantity)
            i = i + 1
        order = Ordering.objects.get(id=orderid)
        order.total = total
        order.save()
        all_menus = OrderDetail.objects.filter(orderid_id=orderid)
        return render(request, "checkout.html", {
            "all_menu": all_menus,
            "user": user,
            "order": order
        })


class UserCheckoutView(View):
    def post(self, request, order_id):
        order = Ordering.objects.get(id=order_id)
        order.is_pay = True
        order.status = "1"
        order.save()
        message = Message()
        message.send_to = order.bid
        message.message = "您有新的订单了，请注意查收"
        message.save()
        return render(request, "pay_success.html")








