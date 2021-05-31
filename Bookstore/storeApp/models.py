from django.db import models


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=1000)  # Field name made lowercase.
    bookversion = models.CharField(db_column='BookVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        db_table = '_migrationhistory'
        unique_together = (('migrationid', 'contextkey'),)


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


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class StoreappBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'storeapp_book'


class StoreappUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = 'storeapp_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)