from django.db import models
from django.contrib.auth import settings


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=1000)  # Field name made lowercase.
    bookversion = models.CharField(db_column='BookVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = '_migrationhistory'
        unique_together = (('migrationid', 'contextkey'),)


class Bookcategories(models.Model):
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookcategories'


class Books(models.Model):
    name = models.CharField(db_column='Name', max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bookcategory = models.ForeignKey(Bookcategories, on_delete=models.CASCADE, db_column='BookCategory_Id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'books'


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