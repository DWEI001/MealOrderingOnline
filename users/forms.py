# _*_ coding: utf-8 _*_
__date__ = '2018/3/24 14:13'
from .models import UserInfo
from django import forms


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image']