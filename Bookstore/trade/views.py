import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.http import require_http_methods

from storeApp.models import Books
from trade.models import ShoppingCart, OrderInfo, OrderBooks
from django.http import HttpResponse, JsonResponse


# Create your views here.
@require_http_methods(["GET"])
@login_required(login_url='/api/login/')
def show_shoppingcart(request):
    try:
        carts = ShoppingCart.objects.filter(user=request.user)
        json_data = json.loads(serializers.serialize('json', carts))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def add_to_shoppingcart(request):
    try:
        book_id = request.POST.get('book_id')
        book_count = request.POST.get('book_count')
        # 判断这本书是否已经存在于购物车，如果已经有了，就不新建条目，而是直接修改数量
        item_exist = ShoppingCart.objects.get(user=request.user, book=Books.objects.get(id=book_id))
        if not item_exist:
            sc_new = ShoppingCart(user=request.user, book=Books.objects.get(id=book_id), book_count=book_count)
            sc_new.save()
        else:
            item_exist.book_count += int(book_count)
            item_exist.save()
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def del_from_shoppingcart(request):
    """从当前用户的购物车中删除选定的图书
    :param book_id
    :return JSON
    :author 朱穆清
    """
    book_id = request.POST.get('book_id')
    try:
        item = ShoppingCart.objects.get(user=request.user, book=Books.objects.get(id=book_id))
        item.delete()
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def edit_shoppingcart(request):
    """编辑购物车内某本图书的购买数量
    :param book_id
    :param book_count
    :return JSON
    :author 朱穆清
    """
    book_id = request.POST.get('book_id')
    book_count = request.POST.get('book_count')
    try:
        item = ShoppingCart.objects.get(user=request.user, book=Books.objects.get(id=book_id))
        item.book_count = book_count
        item.save()
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

@require_http_methods(["GET"])
@login_required(login_url='/api/login/')
def ret_allorders(request):
    """返回当前用户所有订单
    :return JSON
    :author 宋子龙
    """
    try:
        orders = OrderInfo.objects.filter(user=request.user)
        json_data = json.loads(serializers.serialize("json", orders))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

@require_http_methods(["GET"])
@login_required(login_url='/api/login/')
def ret_unreceivedorders(request):
    """返回当前用户未收货的订单
    :return JSON
    :author 宋子龙
    """
    try:
        order = OrderInfo.objects.filter(user=request.user, is_signed=False)
        json_data = json.loads(serializers.serialize("json", order))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

