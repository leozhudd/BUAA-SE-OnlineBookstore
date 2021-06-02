import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import auth


# Create your views here.
from django.views.decorators.http import require_http_methods

from storeApp.models import Books, Bookcategories


def index(request):
    return render(request, 'index.html')


def register(request):
    # 如果用户提交了注册表单：
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')
        new_email = request.POST.get('email')

        # 校验用户是否已经存在
        if User.objects.filter(username=new_username):
            return HttpResponse("用户已存在！")
            # return render(request, 'register.html', {'message': '用户已存在！'})
        # 校验两次密码是否一致
        if new_password1 != new_password2:
            return HttpResponse("两次密码不一致！")
            # return render(request, 'register.html', {'message' '两次密码不一致！'})
        else:
            # 注册成功，创建新用户
            new_user = User.objects.create_user(new_username, new_email, new_password1)
            new_user.save()
            return HttpResponse("注册成功！")
            # return render(request, 'index.html', {'message': '注册成功！'})
    else:
        # 非POST请求，注册失败，重新注册
        return HttpResponse("注册失败！请使用POST请求提交表单！")
        # return render(request, 'register.html', {})


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Password correct, login success
        auth.login(request, user)
        return HttpResponse("登录成功！")
    else:
        # Login failed...
        return HttpResponse("用户名或密码错误！")


def chg_pw(request):
    password = request.POST.get('password')
    new_password = request.POST.get('new_password')
    user = auth.authenticate(username=request.user.username, password=password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        return HttpResponse("密码修改成功！")
    else:
        return HttpResponse("旧密码错误！")


def logout(request):
    auth.logout(request)
    return HttpResponse("登出成功！")


# 图书管理模块
@require_http_methods(["POST"])
def add_book(request):
    book_name = request.POST.get("book_name")
    book_description = request.POST.get("book_description")
    book_price = request.POST.get("book_price")
    book_imgpath = request.POST.get("book_imgpath")
    book_category = request.POST.get("book_category")
    book_category_obj = Bookcategories.objects.get(name=book_category)
    new_book = Books(name=book_name, description=book_description, price=book_price, imgpath=book_imgpath, bookcategory=book_category_obj)
    new_book.save()

    response = {'message': 'success', 'error_num': 0}
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    books = Books.objects.all()
    # 此时books是QuerySet对象，若要要转成json格式返回，使用serialize
    json_data = json.loads(serializers.serialize('json', books))
    response = {'list': json_data, 'message': 'success', 'error_num': 0}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})