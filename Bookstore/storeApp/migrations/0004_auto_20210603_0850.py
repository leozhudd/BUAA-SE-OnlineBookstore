# Generated by Django 3.2 on 2021-06-03 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0003_auto_20210602_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ForeignKey(db_column='BookCategory_Id', on_delete=django.db.models.deletion.CASCADE, to='storeApp.bookcategories'),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(db_column='Price', decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Userlogins',
        ),
    ]
