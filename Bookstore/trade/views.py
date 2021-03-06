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
        carts = ShoppingCart.objects.filter(user=request.user)
        carts_ret = []  # 返回给前端的购物车，添加一些信息
        for item in carts:
            # 更新每本书的库存量是否充足
            if Books.objects.get(id=item.book_id).stock_count < item.book_count:
                item.now_available = False
            else:
                item.now_available = True
            item.save()
            # 补充图书详情信息到carts_ret
            book = Books.objects.get(id=item.book_id)
            # print("url: "+book.image.url)
            # print("name: "+book.image.name)
            info = {'book_id': book.id,
                    'book_name': book.name,
                    'book_author': book.author,
                    'book_price': book.price,
                    'book_count': item.book_count,
                    'book_available': item.now_available,
                    'book_img': book.image.url,
                    'book_intro': book.description}
            carts_ret.append(info)

        # json_data = json.loads(serializers.serialize('json', carts))
        response = {"data": carts_ret, "message": "success", "error_num": 0}
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
        # 查询存不存在必须用filter方法，因为get如果不存在会报错！
        item_exist = ShoppingCart.objects.filter(user=request.user, book=Books.objects.get(id=book_id)).first()
        if item_exist is None:
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
def new_order_single_book(request):
    """从商品详情页面创建新订单，不涉及购物车！
    :param book_id: 所选图书
    :param memo: 订单备注
    :param address: 收货地址
    :param contact_name: 联系人
    :param contact_phone: 联系电话
    :return message, error_num
    :author 朱穆清
    """
    try:
        book_id = request.POST.get("book_id")
        book_count = int(request.POST.get("book_count"))
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
        new_order = OrderInfo(user=request.user, memo=memo, address=address, contact_name=contact_name,
                              contact_phone=contact_phone, order_sn=order_sn)
        new_order.save()

        book = Books.objects.get(id=book_id)  # 根据id取出图书详情项
        book.stock_count -= book_count  # 下单后库存量--
        book.sold_count += book_count  # 下单后销售量++
        book.save()

        new_order.amount_price = book.price*book_count  # 统计订单总金额
        order_books = OrderBooks(order=new_order, book=book, book_count=book_count)
        order_books.save()
        new_order.save()
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": "所选的图书id不存在于购物车！"+str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["POST"])
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
        book_list = request.POST.get("book_list")
        book_list = json.loads(book_list)
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
                item = ShoppingCart.objects.get(book_id=book_id, user_id=userid)
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


# @require_http_methods(["GET"])
# # @login_required(login_url='/api/account/login/')
# def ret_unreceived_orders(request):
#     """返回当前用户未收货的订单
#     :param None
#     :return message, error_num
#     :author 宋子龙
#     """
#     try:
#         order = OrderInfo.objects.filter(user=request.user, is_signed=False)
#         json_data = json.loads(serializers.serialize("json", order))
#         response = {"data": json_data, "message": "success", "error_num": 0}
#     except Exception as e:
#         response = {"message": str(e), "error_num": 1}
#     return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


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
        order.is_signed = True
        order.save()
        response = {"message": "success", "error_num": 0}
    except Exception as e:
        response = {"message": str(e), "error_num": 1}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


# @require_http_methods(["POST"])
# # @login_required(login_url='/api/login/')
# def ret_order_details(request):
#     """返回当前订单详情
#     :param order_id:
#     :return JSON
#     :author 宋子龙
#     """
#     try:
#         order_id = request.POST.get("order_id")
#         orderbooks = OrderBooks.objects.filter(order_id=order_id)
#         json_data1 = json.loads(serializers.serialize("json", orderbooks))
#         order = OrderInfo.objects.filter(id=order_id)
#         json_data2 = json.loads(serializers.serialize("json", order))
#         response = {"data1": json_data1, "data2": json_data2, "message": "success", "error_num": 0}
#     except Exception as e:
#         response = {"message": str(e), "error_num": 1}
#     return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def all_orders_with_details(request):
    """返回当前用户所有订单的所有详情
        :param None
        :return data, message, error_num
        :author 朱穆清
    """
    try:
        # 调用自定义SQL语句实现多表查询
        # 失败：不能返回list+dict+list+dict的形式
        # orders_with_details = OrderInfo.diy_objects.order_full_info(request.user.id)

        orders = OrderInfo.objects.filter(user_id=request.user.id)
        orders_with_details = []
        for order in orders:
            # 把订单所有信息从两个表中封装到一个dict里面
            book_list = order.orderbooks_set.all()
            book_info_list = []
            for book in book_list:
                book_full = Books.objects.get(id=book.book_id)  # 从Books表中找到包含这本书的全部信息的对象，并转化存在dict中
                book_info = {'book_id':book.book_id, 'book_count': book.book_count, 'book_name': book_full.name, 'book_price': book_full.price, 'book_image': book_full.image.url}
                # 或使用python自带的对象转字典的方法__dict__
                book_info_list.append(book_info)
            order_full = {'id': order.id, 'order_sn': order.order_sn, 'address': order.address,
                          'add_time': order.add_time, 'amount_price': order.amount_price,
                          'contact_name': order.contact_name, 'contact_phone': order.contact_phone,
                          'is_payed': order.is_payed, 'is_signed': order.is_signed, 'memo': order.memo,
                          'book_list': book_info_list}
            orders_with_details.append(order_full)
        response = {"data": orders_with_details, "message": "success", "error_num": 0}

    except Exception as e:
        response = {"message": str(e), "error_num": 1}

    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
