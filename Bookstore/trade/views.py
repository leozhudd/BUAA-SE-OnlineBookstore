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
    """返回购物车中全部商品
    :param book_id
    :param book_count
    :return JSON
    :author 朱穆清
    """
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
    """添加某本书到购物车，若该书已经存在则修改购买数量
    :param book_id
    :param book_count
    :return JSON
    :author 朱穆清
    """
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


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def selected_books_preview(request):
    """在购物车选取要下单的书后在订单预览页面调用此函数，返回所有的书的信息
    :param request:
    :param book_list: 图书id的列表
    :return 包含每个书的id和count的列表
    todo: 是否需要返回这本书的所有详细信息？包括书名和图片
    :author 朱穆清
    """
    try:
        book_list = request.POST.getlist("book_list")
        if not book_list:
            response = {"message": "前端传来的列表中没有图书，不能预览！", "error_num": 1}
        else:
            book_objs = []
            # 把list中每一本书的实例加入要返回的列表book_objs中
            for book_id in book_list:
                item = ShoppingCart.objects.get(book_id=book_id)
                book_objs.append(item)
            json_data = json.loads(serializers.serialize('json', book_objs))
            response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def creat_new_order(request):
    """把所选图书从购物车删除并创建新订单
    :param book_list:
    :param memo:
    :param address:
    :param contact_name:
    :param contact_phone:
    :return JSON
    :author 朱穆清
    """
    try:
        book_list = request.POST.getlist("book_list")
        memo = request.POST.get("memo")
        address = request.POST.get("address")
        contact_name = request.POST.get("contact_name")
        contact_phone = request.POST.get("contact_phone")
        if not book_list:
            response = {"message": "前端传来的列表中没有图书，不能预览！", "error_num": 1}
        else:
            new_order = OrderInfo(user=request.user, memo=memo, address=address, contact_name=contact_name,
                                  contact_phone=contact_phone)
            new_order.save()
            amount = 0
            for book_id in book_list:
                item = ShoppingCart.objects.get(book_id=book_id)
                book = Books.objects.get(id=book_id)  # 根据id取出图书的购物车项和详情项
                new_order.amount_price += book.price*item.book_count  # 统计订单总金额
                order_books = OrderBooks(order=new_order, book=book, book_count=item.book_count)
                order_books.save()
                item.delete()  # 把生成了订单的这些书从购物车中删除
            new_order.save()
            response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
