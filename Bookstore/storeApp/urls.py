from django.urls import path, re_path
from storeApp import views

urlpatterns = [


    re_path('add_book/', views.add_book),
    re_path('show_books/', views.show_books),
]