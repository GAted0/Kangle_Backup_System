from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': '用户名'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': '密码'}
    ))
    captcha = CaptchaField(label='验证码')


class ApiAddUser(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)
    node_name = forms.CharField(max_length=30)


class ApiDelUser(forms.Form):
    username = forms.CharField(max_length=20)


class DownloadRequest(forms.Form):
    username = forms.CharField(max_length=30)
    download_path = forms.CharField(max_length=256)


class ApiUnzip(forms.Form):
    node_name = forms.CharField(max_length=20)
