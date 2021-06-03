from django.urls import path, re_path
from storeApp import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('show_books/', views.show_books),
    path('update_book/', views.update_book),
    path('delete_book/', views.delete_book),
    path('logout/', views.logout),
    path('chg_pw/', views.chg_pw),
    path('login/', views.login),
    path('register/', views.register),
]