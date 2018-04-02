from django.contrib import admin

# Register your models here.
from .models import UserInfo, EmailVerifyRecord, Message


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'password', 'gender', 'mobile', 'address', 'email']
    search_fields = ['nick_name',  'gender', 'mobile', 'address', 'email']
    list_filter = ['nick_name',  'gender', 'mobile', 'address', 'email']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_time', 'send_type']
    search_fields = ['code', 'email', 'send_time', 'send_type']
    list_filter = ['code', 'email', 'send_time', 'send_type']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['send_to', 'message']
    list_filter = ['send_to', 'message']
    search_fields = ['send_to', 'message']


admin.site.site_header = "好吃网后台管理"
admin.site.site_title = "好吃网"
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Message, MessageAdmin)


