from django.contrib import admin
from storeApp.models import *

# Register your models here.


# 定义管理页面的显示格式
class BooksAdmin(admin.ModelAdmin):
    # fields 属性定义了新建对象时要显示的字段。
    fields = ('name', 'description', 'price', 'category', 'imgpath')
    # list_display 定义在列表中显示更多的栏目
    list_display = ('name', 'description', 'price', 'category')
    # 显示搜索栏
    search_fields = ('name',)


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Books, BooksAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
