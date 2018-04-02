from django.contrib import admin
from .models import Business, City, UserFavorite, BusinessMessage
# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['bname', 'bphone', 'bemail', 'baddress', 'bstatus', 'bcreate_time']
    search_fields = ['bname', 'bphone', 'bemail', 'baddress', 'bstatus', 'bcreate_time']
    list_filter = ['bname', 'bphone', 'bemail', 'baddress', 'bstatus', 'bcreate_time']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'fav_id', 'add_time']
    list_filter = ['user', 'fav_id']
    search_fields = ['user', 'fav_id']


class BusinessMessageAdmin(admin.ModelAdmin):
    list_display = ['send_to', 'message']
    list_filter = ['send_to', 'message']
    search_fields = ['send_to', 'message']


admin.site.register(Business, BusinessAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(UserFavorite, UserFavoriteAdmin)
admin.site.register(BusinessMessage, BusinessMessageAdmin)