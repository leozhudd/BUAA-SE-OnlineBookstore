from django.urls import path, re_path
from storeApp import views

urlpatterns = [
    path('show_books/', views.show_books),
    path('book_info/', views.book_info),
    path('keywords_search/', views.keywords_search),
    path('logout/', views.logout),
    path('chg_pw/', views.chg_pw),
    path('login/', views.login),
    path('register/', views.register),
]