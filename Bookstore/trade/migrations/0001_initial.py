# Generated by Django 3.2 on 2021-06-06 13:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storeApp', '0009_auto_20210606_2152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_count', models.IntegerField(default=1, verbose_name='购买数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='加入购物车时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.books', verbose_name='图书')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总金额')),
                ('is_payed', models.BooleanField(default=False, verbose_name='支付状态')),
                ('memo', models.CharField(max_length=255, verbose_name='订单备注')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='订单创建时间')),
                ('address', models.CharField(max_length=255, verbose_name='收货地址')),
                ('contact_name', models.CharField(max_length=255, verbose_name='联系人姓名')),
                ('contact_phone', models.CharField(max_length=255, verbose_name='联系人电话')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单属性',
                'verbose_name_plural': '订单属性',
            },
        ),
        migrations.CreateModel(
            name='OrderBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_count', models.IntegerField(default=1, verbose_name='购买数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.books', verbose_name='图书')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.orderinfo', verbose_name='订单属性')),
            ],
            options={
                'verbose_name': '订单中的商品清单',
                'verbose_name_plural': '订单中的商品清单',
            },
        ),
    ]
