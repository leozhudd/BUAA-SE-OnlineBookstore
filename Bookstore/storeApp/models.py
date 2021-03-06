from django.db import models


class BookCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=20, verbose_name="类别名")  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookcategories'
        verbose_name = "图书类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(verbose_name="书名", db_column='Name', max_length=20, unique=True)  # Field name made lowercase.
    description = models.CharField(verbose_name="图书描述", db_column='Description', max_length=1000)  # Field name made lowercase.
    price = models.DecimalField(verbose_name="价格", db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sold_count = models.IntegerField(verbose_name="销量", default=0)
    image = models.ImageField(verbose_name="封面图", upload_to="book_image", null=True, blank=True)
    stock_count = models.IntegerField(verbose_name="库存量", default=100)
    author = models.CharField(verbose_name="作者", max_length=20)
    publisher = models.CharField(verbose_name="出版社", max_length=20)

    # 商品分类:商品: 1:N
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name="类别", db_column='BookCategory_Id')  # Field name made lowercase.

    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# todo: 用户收货地址模型，暂时先不设计这个功能，用户每次都需要手动填地址。