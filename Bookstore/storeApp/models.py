from django.db import models


class Aspnetroles(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        db_table = 'aspnetroles'


class Aspnetuserclaims(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    claimtype = models.CharField(db_column='ClaimType', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.CharField(db_column='ClaimValue', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'aspnetuserclaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=128)  # Field name made lowercase.
    providerkey = models.CharField(db_column='ProviderKey', max_length=128)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        db_table = 'aspnetuserlogins'
        unique_together = (('loginprovider', 'providerkey', 'userid'),)


class Aspnetuserroles(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        db_table = 'aspnetuserroles'


class Aspnetusers(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.TextField(db_column='EmailConfirmed')  # Field name made lowercase. This field type is a guess.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.CharField(db_column='SecurityStamp', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.TextField(db_column='PhoneNumberConfirmed')  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'aspnetusers'


class Bookcategories(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'bookcategories'


class Books(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    bookcategory = models.ForeignKey(Bookcategories, models.DO_NOTHING, db_column='BookCategory_Id')  # Field name made lowercase.

    class Meta:
        db_table = 'books'


class Orderdetails(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    orderheader = models.ForeignKey('Orderheaders', models.DO_NOTHING, db_column='OrderHeader_Id')  # Field name made lowercase.
    book = models.ForeignKey(Books, models.DO_NOTHING, db_column='Book_Id')  # Field name made lowercase.

    class Meta:
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
        db_table = 'orderheaders'