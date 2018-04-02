from django.contrib import admin
from .models import MenuInfo, MenuType
# Register your models here.


class MenuInfoAdmin(admin.ModelAdmin):
    list_filter = ['business', 'menu_type',  'mname', 'mprice', 'discount', 'add_time']
    list_display = ['business', 'menu_type', 'mname', 'mprice', 'discount', 'add_time', 'mimage']
    search_fields = ['business', 'menu_type', 'mname', 'mprice', 'discount', 'add_time']


class MenuTypeAdmin(admin.ModelAdmin):
    list_filter = ['type']
    list_display = ['type']
    search_fields = ['type']


admin.site.register(MenuInfo, MenuInfoAdmin)
admin.site.register(MenuType, MenuTypeAdmin)