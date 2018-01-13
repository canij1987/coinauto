from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {'username': '아이디', 'password': '비밀번호', 'email': '이메일'}
        help_texts = {'username': '영문자, 숫자, _만 입력, 최소 3자이상 입력하세요'}


class UserProfileInfoForm(forms.ModelForm):
    secret_key = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfileInfo
        fields = ('connect_key', 'secret_key')