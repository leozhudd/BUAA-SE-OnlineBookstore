# Generated by Django 3.2 on 2021-06-01 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspnetroles',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
            ],
            options={
                'db_table': 'aspnetroles',
            },
        ),
        migrations.CreateModel(
            name='Aspnetuserclaims',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('claimtype', models.CharField(blank=True, db_column='ClaimType', max_length=1000, null=True)),
                ('claimvalue', models.CharField(blank=True, db_column='ClaimValue', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'aspnetuserclaims',
            },
        ),
        migrations.CreateModel(
            name='Aspnetuserlogins',
            fields=[
                ('loginprovider', models.CharField(db_column='LoginProvider', max_length=128, primary_key=True, serialize=False)),
                ('providerkey', models.CharField(db_column='ProviderKey', max_length=128)),
            ],
            options={
                'db_table': 'aspnetuserlogins',
            },
        ),
        migrations.CreateModel(
            name='Aspnetusers',
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
                'db_table': 'aspnetusers',
            },
        ),
        migrations.CreateModel(
            name='Bookcategories',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
            ],
            options={
                'db_table': 'bookcategories',
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
                ('bookcategory', models.ForeignKey(db_column='BookCategory_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.bookcategories')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('price', models.IntegerField(db_column='Price')),
                ('amount', models.IntegerField(db_column='Amount')),
                ('book', models.ForeignKey(db_column='Book_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.books')),
            ],
            options={
                'db_table': 'orderdetails',
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
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='orderheader',
            field=models.ForeignKey(db_column='OrderHeader_Id', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.orderheaders'),
        ),
        migrations.AddField(
            model_name='aspnetuserlogins',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.aspnetusers'),
        ),
        migrations.AddField(
            model_name='aspnetuserclaims',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.aspnetusers'),
        ),
        migrations.CreateModel(
            name='Aspnetuserroles',
            fields=[
                ('userid', models.OneToOneField(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='storeApp.aspnetusers')),
                ('roleid', models.ForeignKey(db_column='RoleId', on_delete=django.db.models.deletion.DO_NOTHING, to='storeApp.aspnetroles')),
            ],
            options={
                'db_table': 'aspnetuserroles',
            },
        ),
        migrations.AlterUniqueTogether(
            name='aspnetuserlogins',
            unique_together={('loginprovider', 'providerkey', 'userid')},
        ),
    ]
