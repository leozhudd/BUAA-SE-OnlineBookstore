import json
import time

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.http import require_http_methods

from storeApp.models import Books
from trade.models import ShoppingCart, OrderInfo, OrderBooks
from django.http import JsonResponse


# Create your views here.
@require_http_methods(["GET"])
def show_shoppingcart(request):
    """返回当前用户的购物车中的全部商品，并根据库存量更新状态
    :param None
    :return data, message, error_num
    :author 朱穆清
    """
    try:
        # username = request.POST.get("username")
        # print(username)
        carts = ShoppingCart.objects.filter(user=request.user)
        # print(request.user)
        # 更新每本书的库存量是否充足
        for item in carts:
            if Books.objects.get(id=item.book_id).stock_count < item.book_count:
                item.now_available = False
            else:
                item.now_available = True
            item.save()
        json_data = json.loads(serializers.serialize('json', carts))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
# @login_required(login_url='/api/account/login/')
def add_to_shoppingcart(request):
    """添加某本书到购物车，若该书已经存在则修改购买数量
    :param book_id
    :param book_count
    :return message, error_num
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
# @login_required(login_url='/api/account/login/')
def del_from_shoppingcart(request):
    """从当前用户的购物车中删除选定的图书
    :param book_id
    :return message, error_num
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
# @login_required(login_url='/api/account/login/')
def edit_shoppingcart(request):
    """编辑购物车内某本图书的购买数量
    :param book_id
    :param book_count
    :return message, error_num
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
# @login_required(login_url='/api/account/login/')
def selected_books_preview(request):
    """在购物车选取要下单的书后在订单预览页面调用此函数，返回所有的书的信息
    :param book_list: 所选择的图书id的列表
    :return message, error_num
    :return data: 包含每个书的id和count的列表
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
                # if Books.objects.get(id=book_id).stock_count < item.book_count:
                #     raise Exception("库存量不足，无法下单！")
                book_objs.append(item)
            json_data = json.loads(serializers.serialize('json', book_objs))
            response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

    
@require_http_methods(["GET"])
# @login_required(login_url='/api/account/login/')
def ret_all_orders(request):
    """返回当前用户所有订单
    :return data: 用户所有订单
    :return message, error_num
    :author 宋子龙
    """
    try:
        orders = OrderInfo.objects.filter(user=request.user)
        json_data = json.loads(serializers.serialize("json", orders))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
# @login_required(login_url='/api/account/login/')
def creat_new_order(request):
    """创建新订单并把所选图书从购物车删除（调用即下单成功，销售量++，库存量--）
    :param book_list: 所选图书列表
    :param memo: 订单备注
    :param address: 收货地址
    :param contact_name: 联系人
    :param contact_phone: 联系电话
    :return message, error_num
    :author 朱穆清
    """
    try:
        book_list = request.POST.getlist("book_list")
        memo = request.POST.get("memo")
        address = request.POST.get("address")
        contact_name = request.POST.get("contact_name")
        contact_phone = request.POST.get("contact_phone")
        # 生成订单唯一编号
        # 当前时间 + userid + 随机数(2位)
        import random
        # 当前时间，eg: '20200329152308'
        now_time = time.strftime("%Y%m%d%H%M%S")
        userid = request.user.id
        ranstr = "%.3d" % (random.randint(1, 99))
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=now_time, userid=userid, ranstr=ranstr)
        if not book_list:
            response = {"message": "前端传来的列表中没有图书，不能预览！", "error_num": 1}
        else:
            new_order = OrderInfo(user=request.user, memo=memo, address=address, contact_name=contact_name,
                                  contact_phone=contact_phone, order_sn=order_sn)
            new_order.save()
            for book_id in book_list:
                item = ShoppingCart.objects.get(book_id=book_id)
                book = Books.objects.get(id=book_id)  # 根据id取出图书的购物车项和详情项
                book.stock_count -= item.book_count  # 下单后库存量--
                book.sold_count += item.book_count  # 下单后销售量++
                book.save()
                new_order.amount_price += book.price*item.book_count  # 统计订单总金额
                order_books = OrderBooks(order=new_order, book=book, book_count=item.book_count)
                order_books.save()
                item.delete()  # 把生成了订单的这些书从购物车中删除
            new_order.save()
            response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": "所选的图书id不存在于购物车！"+str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
# @login_required(login_url='/api/account/login/')
def ret_unreceived_orders(request):
    """返回当前用户未收货的订单
    :param None
    :return message, error_num
    :author 宋子龙
    """
    try:
        order = OrderInfo.objects.filter(user=request.user, is_signed=False)
        json_data = json.loads(serializers.serialize("json", order))
        response = {"data": json_data, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
# @login_required(login_url='/api/login/')
def set_order_received(request):
    """修改某订单状态为已收货
    :param id:
    :return JSON
    :author 宋子龙
    """
    try:
        id = request.POST.get("id")
        order = OrderInfo.objects.get(id=id)
        order.update(is_signed=True)
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
# @login_required(login_url='/api/login/')
def ret_order_details(request):
    """返回当前订单详情
    :param order_id:
    :return JSON
    :author 宋子龙
    """
    try:
        order_id = request.POST.get("order_id")
        orderbooks = OrderBooks.objects.filter(order_id=order_id)
        json_data1 = json.loads(serializers.serialize("json", orderbooks))
        order = OrderInfo.objects.filter(id=order_id)
        json_data2 = json.loads(serializers.serialize("json", order))
        response = {"data1": json_data1, "data2": json_data2, "message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


