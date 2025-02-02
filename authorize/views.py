from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from authorize.models import AuthUser
from django.contrib import messages
import tkinter.messagebox #弹窗库
from tkinter import *
from django.contrib.auth.hashers import check_password

# Create your views here.
def showAuth(request):
    return render(request, "login.html", locals())

class UserInfo:
    islogin = False
    isVip = False
    username = ''
    password = ''



# def login_auth(request):
#     UserInfo.username = request.GET.get('username')
#     UserInfo.password = request.GET.get('password')
#     # return render(request,'index.html')
#     return HttpResponse("username or password is incorrect{},{}".format(username, password))

def login_site(request):
    UserInfo.username = request.GET.get('username')
    UserInfo.password = request.GET.get('password')

    request.session['username'] = UserInfo.username
    request.session['password'] = UserInfo.password

    user = auth.authenticate(username=UserInfo.username, password=UserInfo.password)  # 使用 Django 的 authenticate 方法来验证
    if user is not None:
        auth.login(request, user)
        UserInfo.islogin = True
        ans = AuthUser.objects.values('username','is_staff')
        for i in range(len(ans)):
            if ans[i]['username'] == UserInfo.username:
                UserInfo.isVip = ans[i]['is_staff']
                request.session['isVip'] = UserInfo.isVip
                break
        # messages.error(request, '登录成功')
        return render(request, 'index.html', {'username': UserInfo.username,'islogin':UserInfo.islogin,'isVip':UserInfo.isVip})
    else:
        # messages.error(request, '用户名或密码不正确')
        # return render(request, 'login.html', {
        #     'login_err': 'Please recheck your username or password !'
        # })
        return HttpResponse("username or password is incorrect {},{}".format(UserInfo.username,UserInfo.password))
    # return render(request, 'index.html')

def logout_site(request):
    UserInfo.islogin = False
    UserInfo.isVip = False
    logout(request)     # <==
    return HttpResponseRedirect('已退出登录')