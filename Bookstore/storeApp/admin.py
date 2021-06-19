from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from storeApp.models import *
# Register your models here.


# 定义管理页面的显示格式
class BooksAdmin(admin.ModelAdmin):
    # fields 属性定义了新建对象时要显示的字段。
    fields = ('name', 'description', 'price', 'category', 'image', 'stock_count', 'author', 'publisher')
    # list_display 定义在列表中显示更多的栏目
    list_display = ('name', 'description', 'price', 'category', 'sold_count', 'stock_count', 'author', 'publisher', 'image_data')
    # 显示搜索栏
    search_fields = ('name',)
    # 可以直接在列表编辑
    # list_editable = ['description', 'price', 'category', 'stock_count', ]

    readonly_fields = ('image_data',)  #必须加这行 否则访问编辑页面会报错

    def image_data(self, obj):
        return format_html('< img src="%s" width="100px" />' % obj.image.url)
    # 页面显示的字段名称
    image_data.short_description = '品牌图片'


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Books, BooksAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
