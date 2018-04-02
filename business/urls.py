# _*_ coding: utf-8 _*_
__date__ = '2018/3/19 15:52'
from django.conf.urls import url
from .views import BusinessHomeView, UserFavoriteView, UserAddOrderView, UserCheckoutView, BusinessLoginView
from .views import BusinessLogoutView, BusinessMenuView, MenuDetailView, AddMenuView, BusinessInfoView, UploadBusinessImageView, UploadMenuImageView
from .views import UpdatePwdView, UpdateBusEmailView, BusinessRegisterView, BusinessActiveView, BusinessForgetView, BusinessModifyView,BusinessResetView
from .views import BusinessOrderView, BusinessOrderDetailView, BusinessCheckoutView, BusinessMessageView
urlpatterns = [
    url(r'^login/$', BusinessLoginView.as_view(), name="login"),
    url(r'^register/$', BusinessRegisterView.as_view(), name="register"),
    url(r'^active/(?P<active_code>.*)/$', BusinessActiveView.as_view(), name="active"),
    url(r'^logout/$', BusinessLogoutView.as_view(), name="logout"),
    url(r'^forget/$', BusinessForgetView.as_view(), name="forget"),
    url(r'^reset/(?P<active_code>.*)/$', BusinessResetView.as_view(), name="reset"),
    url(r'^modify/$', BusinessModifyView.as_view(), name="modify"),
    url(r'^all_menu/$', BusinessMenuView.as_view(), name="all_menu"),
    url(r'^detail/(?P<business_id>\d+)/$', BusinessHomeView.as_view(), name="business_detail"),
    url(r'^menu_detail/(?P<menu_id>\d+)/$', MenuDetailView.as_view(), name="menu_detail"),
    url(r'^add_fav/$', UserFavoriteView.as_view(), name="add_fav"),
    url(r'^add_menu/$', AddMenuView.as_view(), name="add_menu"),
    url(r'^add_order', UserAddOrderView.as_view(), name="add_order"),
    url(r'^order_list', BusinessOrderView.as_view(), name="order_list"),
    url(r'^order_detail/(?P<order_id>\d+)/$', BusinessOrderDetailView.as_view(), name="order_detail"),
    url(r'^business_checkout/(?P<order_id>\d+)/$', BusinessCheckoutView.as_view(), name="business_checkout"),
    url(r'^updateemail/$', UpdateBusEmailView.as_view(), name="updateemail"),
    url(r'^business_message/$', BusinessMessageView.as_view(), name="business_message"),
    url(r'^updatePwd/$', UpdatePwdView.as_view(), name="updatePwd"),
    url(r'^uploadmenuimage/(?P<menu_id>\d+)/$', UploadMenuImageView.as_view(), name="uplaodmenuimage"),
    url(r'^uploadbusinessimage/$', UploadBusinessImageView.as_view(), name="uplaodbusinessimage"),
    url(r'^businessinfo/$', BusinessInfoView.as_view(), name="businessinfo"),
    url(r'^checkout/(?P<order_id>\d+)$', UserCheckoutView.as_view(), name="checkout"),
]
