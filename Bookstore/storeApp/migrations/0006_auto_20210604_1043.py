# Generated by Django 3.2 on 2021-06-04 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0005_alter_books_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookcategories',
            new_name='BookCategory',
        ),
        migrations.DeleteModel(
            name='Migrationhistory',
        ),
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'managed': True, 'verbose_name': '图书分类', 'verbose_name_plural': '图书分类'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'managed': True, 'verbose_name': '图书详情', 'verbose_name_plural': '图书详情'},
        ),
    ]
