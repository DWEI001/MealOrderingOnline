"""MealOrderingOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views
from django.views.static import serve
from MealOrderingOnline.settings import MEDIA_ROOT
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^user_login/$', views.UserLoginView.as_view(), name="user_login"),
    url(r'^user_register/$', views.UserRegisterView.as_view(), name="user_register"),
    url(r'^active/(?P<active_code>.*)/$', views.UserActiveView.as_view(), name="user_active"),
    url(r'^user_forget/$', views.UserForgetView.as_view(), name="user_forget"),
    url(r'^user_reset/(?P<active_code>.*)/$', views.UserResetView.as_view(), name="user_reset"),
    url(r'^user_modify/$', views.UserModifyView.as_view(), name="user_modify"),
    url(r'^user_logout/$', views.UserLogoutView.as_view(), name="user_logout"),
    url(r'^user_info/$', views.UserInfoView.as_view(), name="user_info"),
    url(r'^user_uploadimage/$', views.UploadImageView.as_view(), name="user_uploadimage"),
    url(r'^user_updatepwd/$', views.UpdatePwdView.as_view(), name="user_updatepwd"),
    url(r'^update_email/$', views.UpdateEmailView.as_view(), name="update_email"),
    url(r'^message/$', views.UserMessageView.as_view(), name="user_message"),
    url(r'^business/', include('business.urls', namespace="business")),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),

]
