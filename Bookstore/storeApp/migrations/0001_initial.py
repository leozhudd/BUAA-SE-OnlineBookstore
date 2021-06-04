# Generated by Django 3.2 on 2021-06-01 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookcategories',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
            ],
            options={
                'db_table': 'bookcategories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=60)),
                ('description', models.CharField(db_column='Description', max_length=1000)),
                ('price', models.IntegerField(db_column='Price')),
                ('imgpath', models.CharField(blank=True, db_column='ImgPath', max_length=1000, null=True)),
                ('category', models.ForeignKey(db_column='BookCategory_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.bookcategories')),
            ],
            options={
                'db_table': 'books',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orderheaders',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('memberid', models.CharField(blank=True, db_column='MemberId', max_length=1000, null=True)),
                ('contactname', models.CharField(db_column='ContactName', max_length=40)),
                ('contactphoneno', models.CharField(db_column='ContactPhoneNo', max_length=40)),
                ('contactaddress', models.CharField(db_column='ContactAddress', max_length=1000)),
                ('totalprice', models.IntegerField(db_column='TotalPrice')),
                ('memo', models.CharField(blank=True, db_column='Memo', max_length=1000, null=True)),
                ('buyon', models.DateTimeField(db_column='BuyOn')),
            ],
            options={
                'db_table': 'orderheaders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'roles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=128, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=256, null=True)),
                ('emailconfirmed', models.TextField(db_column='EmailConfirmed')),
                ('passwordhash', models.CharField(blank=True, db_column='PasswordHash', max_length=1000, null=True)),
                ('securitystamp', models.CharField(blank=True, db_column='SecurityStamp', max_length=1000, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=1000, null=True)),
                ('phonenumberconfirmed', models.TextField(db_column='PhoneNumberConfirmed')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Userclaims',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('claimtype', models.CharField(blank=True, db_column='ClaimType', max_length=1000, null=True)),
                ('claimvalue', models.CharField(blank=True, db_column='ClaimValue', max_length=1000, null=True)),
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.users')),
            ],
            options={
                'db_table': 'userclaims',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('price', models.IntegerField(db_column='Price')),
                ('amount', models.IntegerField(db_column='Amount')),
                ('book', models.ForeignKey(db_column='Book_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.books')),
                ('orderheader', models.ForeignKey(db_column='OrderHeader_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.orderheaders')),
            ],
            options={
                'db_table': 'orderdetails',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Migrationhistory',
            fields=[
                ('migrationid', models.CharField(db_column='MigrationId', max_length=150, primary_key=True, serialize=False)),
                ('contextkey', models.CharField(db_column='ContextKey', max_length=300)),
                ('model', models.CharField(db_column='Model', max_length=1000)),
                ('bookversion', models.CharField(db_column='BookVersion', max_length=32)),
            ],
            options={
                'db_table': '_migrationhistory',
                'managed': True,
                'unique_together': {('migrationid', 'contextkey')},
            },
        ),
        migrations.CreateModel(
            name='Userroles',
            fields=[
                ('userid', models.OneToOneField(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='storeApp.users')),
                ('roleid', models.ForeignKey(db_column='RoleId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.roles')),
            ],
            options={
                'db_table': 'userroles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Userlogins',
            fields=[
                ('loginprovider', models.CharField(db_column='LoginProvider', max_length=128, primary_key=True, serialize=False)),
                ('providerkey', models.CharField(db_column='ProviderKey', max_length=128)),
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.users')),
            ],
            options={
                'db_table': 'userlogins',
                'managed': True,
                'unique_together': {('loginprovider', 'providerkey', 'userid')},
            },
        ),
    ]
