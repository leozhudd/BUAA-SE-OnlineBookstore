# Generated by Django 3.2 on 2021-06-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0011_alter_bookcategory_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '图书信息', 'verbose_name_plural': '图书信息'},
        ),
        migrations.RemoveField(
            model_name='books',
            name='click_count',
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(default=1, max_length=20, verbose_name='作者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.CharField(default=3, max_length=20, verbose_name='出版社'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(db_column='Name', max_length=20, unique=True, verbose_name='书名'),
        ),
        migrations.AlterModelTable(
            name='books',
            table=None,
        ),
    ]
