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
            # 用户已存在
            return JsonResponse({"message": "用户已存在，请直接登录", "error_num": 1})
        # 校验两次密码是否一致
        if new_password1 != new_password2:
            # 两次密码不一致
            return JsonResponse({"message": "两次密码不一致！", "error_num": 1})
        else:
            # 注册成功，创建新用户
            new_user = User.objects.create_user(new_username, new_email, new_password1)
            new_user.save()
            return JsonResponse({"message": "success", "error_num": 0})
    else:
        # 非POST请求，注册失败，重新注册
        return JsonResponse({"message": "注册失败！请使用POST请求提交表单！", "error_num": 1})


@require_http_methods(["POST"])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Password correct, login success
        auth.login(request, user)
        response = {"message": "登录成功", "error_num": 0}
    else:
        # Login failed...
        response = {"message": "用户名或密码错误！", "error_num": 1}
    return JsonResponse(response)


@require_http_methods(["POST"])
def chg_pw(request):
    password = request.POST.get('password')
    new_password = request.POST.get('new_password')
    user = auth.authenticate(username=request.user.username, password=password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        response = {'message': 'success', 'error_num': 0}
    else:
        response = {'message': '旧密码错误', 'error_num': 1}
    return JsonResponse(response)


@require_http_methods(["GET"])
def logout(request):
    auth.logout(request)
    return JsonResponse({'message': 'success', 'error_num': 0})


# 图书管理模块
@require_http_methods(["POST"])
def add_book(request):
    try:
        book_name = request.POST.get("book_name")
        book_description = request.POST.get("book_description")
        book_price = request.POST.get("book_price")
        book_imgpath = request.POST.get("book_imgpath")
        book_category = request.POST.get("book_category")
        book_category_obj = Bookcategories.objects.get(name=book_category)
        new_book = Books(name=book_name, description=book_description, price=book_price, imgpath=book_imgpath, bookcategory=book_category_obj)
        new_book.save()
        response = {'message': 'success', 'error_num': 0}
    except Exception as e:
        response = {'message': '图书已经存在！错误信息'+str(e), 'error_num': 1}

    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def show_books(request):
    try:
        books = Books.objects.all()
        # 此时books是QuerySet对象，若要要转成json格式返回，使用serialize
        json_data = json.loads(serializers.serialize('json', books))
        response = {'list': json_data, 'message': 'success', 'error_num': 0}
    except Exception as e:
        response = {'message': str(e), 'error_num': 1}

    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
def update_book(request):
    try:
        book_name = request.POST.get("book_name")
        target_book = Books.objects.get(name=book_name)
        target_book.description = request.POST.get("book_description")
        target_book.price = request.POST.get("book_price")
        target_book.imgpath = request.POST.get("book_imgpath")
        target_book.bookcategory = Bookcategories.objects.get(name=request.POST.get("book_category"))
        target_book.save()
        response = {'message': 'success', 'error_num': 0}
    except Exception as e:
        response = {'message': str(e), 'error_num': 1}

    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
def delete_book(request):
    try:
        book_name = request.POST.get("book_name")
        target_book = Books.objects.get(name=book_name)
        target_book.delete()
        response = {'message': 'success', 'error_num': 0}
    except Exception as e:
        response = {'message': '图书删除失败，请检查图书名是否正确', 'error_num': 1}

    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})