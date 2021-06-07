from django.urls import path
from trade import views


urlpatterns = [
    path('show_shoppingcart/', views.show_shoppingcart),
    path('add_to_shoppingcart/', views.add_to_shoppingcart),
    path('del_from_shoppingcart/', views.del_from_shoppingcart),
    path('edit_shoppingcart/', views.edit_shoppingcart),
    path('ret_allorders/', views.ret_allorders),
    path('ret_unreceivedorders/', views.ret_unreceivedorders)
]