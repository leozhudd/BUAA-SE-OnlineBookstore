from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from trade.models import ShoppingCart, OrderInfo, OrderBooks


class ShoppingCartAdmin(admin.ModelAdmin):
    # fields 属性定义了新建对象时要显示的字段。
    # fields = ()
    # list_display 定义在列表中显示更多的栏目
    list_display = ('user', 'book', 'book_count')
    # 显示搜索栏
    # search_fields = ('user', )
    # 可以直接在列表编辑
    # list_editable = ['description', 'price', 'category', 'stock_count', ]


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ("order_sn", "user", "address", "is_payed", "is_signed", "memo", "amount_price",
                    "add_time")
    # search_fields = ('user',)


admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
