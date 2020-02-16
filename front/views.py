from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .for_file import get_sql_file_size_list, get_web_file_size_list, unzip_file
from . import models
from . import forms
import hashlib
import os
import datetime


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'front/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(username=username)
            except:
                message = '用户不存在！'
                return render(request, 'front/login.html', locals())
            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_node_name'] = user.node_name
                request.session['user_username'] = user.username
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'front/login.html', locals())
        else:
            return render(request, 'front/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'front/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        redirect('/login/')
    request.session.flush()
    return redirect("/login/")


@csrf_exempt
def add_user(request):
    if request.method == 'GET':
        return redirect('/index/')
    if request.method == 'POST':
        api_forms = forms.ApiAddUser(request.POST)
        if api_forms.is_valid():
            username = api_forms.cleaned_data.get('username')
            password = api_forms.cleaned_data.get('password')
            node_name = api_forms.cleaned_data.get('node_name')
            try:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    return HttpResponse('Fail，已经存在同名用户')
                else:
                    new_user = models.User()
                    new_user.username = username
                    new_user.password = hash_code(password)
                    new_user.node_name = node_name
                    new_user.save()
                    return HttpResponse('Success')
            except:
                return HttpResponse('Fail，数据库连接错误！')


@csrf_exempt
def del_user(request):
    if request.method == 'GET':
        return redirect('/index/')
    if request.method == 'POST':
        api_forms = forms.ApiDelUser(request.POST)
        if api_forms.is_valid():
            username = api_forms.cleaned_data.get('username')
            password = api_forms.cleaned_data.get('password')
            try:
                user = models.User.objects.get(username=username)
            except:
                return HttpResponse('Fail，用户不存在')
            models.User.objects.get(username=username).delete()
            return HttpResponse('Success，已删除该用户！')
        else:
            return HttpResponse('Fail，提交的数据格式验证错误！')


@csrf_exempt
def download(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'GET':
        if not request.session.get('is_login', None):
            return redirect('/login/')
        username = request.session.get('user_username')
        node_name = request.session.get('user_node_name')
        web_backups = get_web_file_size_list(username, node_name)
        sql_backups = get_sql_file_size_list(username, node_name)
        context = {
            'web_backups': web_backups,
            'sql_backups': sql_backups
        }
        return render(request, 'front/download.html', context=context)
    if request.method == 'POST':
        if not request.session.get('is_login', None):
            return HttpResponse('还没登陆你搞毛呢？')
        download_forms = forms.DownloadRequest(request.POST)
        if download_forms.is_valid():
            username = download_forms.cleaned_data.get('username')
            file_path = download_forms.cleaned_data.get('download_path')
            filename = os.path.basename(file_path)
            request_file_head = filename.split('.')[0]
            if username != request_file_head:
                return HttpResponse(' 非法请求！')
            try:
                file = open(file_path, 'rb')
                response = FileResponse(file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename={}'.format(filename)
                return response
            except:
                return HttpResponse('系统错误，请马上联系管理员修复')
        return HttpResponse('提交数据验证错误，请重试！')


@csrf_exempt
def unzip(request):
    if request.method == 'GET':
        return redirect('/index/')
    if request.method == 'POST':
        unzip_form = forms.ApiUnzip(request.POST)
        if unzip_form.is_valid():
            node_name = unzip_form.cleaned_data.get('node_name')
            try:
                unzip_file(node_name)
                return HttpResponse('文件解压成功')
            except:
                return HttpResponse('文件解压失败！')
        return HttpResponse('节点名验证错误！')
    return HttpResponse('我也不知道你是个什么东西')


def hash_code(s, salt='Ah=d78has24j-72cSdsh.*/'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
