from django.db import models
from django.contrib.auth import settings


class BookCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookcategories'
        verbose_name = "图书类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(verbose_name="书名", db_column='Name', max_length=60, unique=True)  # Field name made lowercase.
    description = models.CharField(verbose_name="图书描述", db_column='Description', max_length=1000)  # Field name made lowercase.
    price = models.DecimalField(verbose_name="价格", db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sold_count = models.IntegerField(verbose_name="销量", default=0)
    image = models.ImageField(verbose_name="封面图", upload_to="resources/book_image", null=True, blank=True)
    click_count = models.IntegerField(verbose_name="点击量", default=0)
    stock_count = models.IntegerField(verbose_name="库存量", default=100)

    # 商品分类:商品: 1:N
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name="类别", db_column='BookCategory_Id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'books'
        verbose_name = "图书详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Orderdetails(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    orderheader = models.ForeignKey('Orderheaders', models.DO_NOTHING, db_column='OrderHeader_Id')  # Field name made lowercase.
    book = models.ForeignKey(Books, models.DO_NOTHING, db_column='Book_Id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'orderdetails'


class Orderheaders(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='MemberId', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=40)  # Field name made lowercase.
    contactphoneno = models.CharField(db_column='ContactPhoneNo', max_length=40)  # Field name made lowercase.
    contactaddress = models.CharField(db_column='ContactAddress', max_length=1000)  # Field name made lowercase.
    totalprice = models.IntegerField(db_column='TotalPrice')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    buyon = models.DateTimeField(db_column='BuyOn')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'orderheaders'


class Userclaims(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    claimtype = models.CharField(db_column='ClaimType', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.CharField(db_column='ClaimValue', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'userclaims'