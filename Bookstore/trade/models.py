from django.db import models, connection
from django.contrib.auth import get_user_model
from datetime import datetime
from storeApp.models import Books

# 自定义模型查询方法（SQL）
# class OrderInfoManager(models.Manager):
#     def order_full_info(self, userid):
#         cursor = connection.cursor()
#         cursor.execute("""
#             SELECT trade_OrderInfo.id, trade_OrderInfo.order_sn, trade_OrderInfo.address,
#                           trade_OrderInfo.add_time, trade_OrderInfo.amount_price,
#                           trade_OrderInfo.contact_name, trade_OrderInfo.contact_phone,
#                           trade_OrderInfo.is_payed, trade_OrderInfo.is_signed, trade_OrderInfo.memo,
#                           storeApp_Books.name, storeApp_Books.price, storeApp_Books.image
#             FROM trade_OrderInfo, storeApp_Books, trade_OrderBooks
#             WHERE trade_OrderBooks.order_id=trade_OrderInfo.id AND storeApp_Books.id=trade_orderbooks.book_id
#             AND trade_OrderInfo.user_id=%s
#         """, [userid])
#         return cursor.fetchall()


class ShoppingCart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="用户")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="图书")
    book_count = models.IntegerField(verbose_name="购买数量", default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="加入购物车时间")
    now_available = models.BooleanField(verbose_name="现在库存量充足", default=True)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s * %d".format(self.book.name, self.book_count)


class OrderInfo(models.Model):
    order_sn = models.CharField(verbose_name="订单编号", max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="用户")
    amount_price = models.DecimalField(verbose_name="订单总金额", max_digits=10, decimal_places=2, default=0)
    is_payed = models.BooleanField(verbose_name="支付状态", default=False)
    is_signed = models.BooleanField(verbose_name="签收状态", default=False)
    memo = models.CharField(verbose_name="订单备注", max_length=255, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="订单创建时间")
    # 收货信息
    address = models.CharField(verbose_name="收货地址", max_length=255)
    contact_name = models.CharField(verbose_name="联系人姓名", max_length=255)
    contact_phone = models.CharField(verbose_name="联系人电话", max_length=255)

    # 自定义查询函数
    # objects = models.Manager()
    # diy_objects = OrderInfoManager()

    class Meta:
        verbose_name = "订单属性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id.__str__()


class OrderBooks(models.Model):
    # 一个订单对应多个商品
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单属性")
    # 两个外键形成一张关联表
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="图书")
    book_count = models.IntegerField(verbose_name="购买数量", default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单中的商品清单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s * %d".format(self.book.name, self.book_count)
