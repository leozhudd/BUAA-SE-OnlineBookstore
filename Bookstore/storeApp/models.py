from django.db import models


# Create your models here.
class User(models.Model):
    # primary_key = ID（自动生成）
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)


class Book(models.Model):
    book_name = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
