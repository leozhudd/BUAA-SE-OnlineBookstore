from django.urls import path
from trade import views


urlpatterns = [
    path('show_shoppingcart/', views.show_shoppingcart),
    path('add_to_shoppingcart/', views.add_to_shoppingcart),
    path('del_from_shoppingcart/', views.del_from_shoppingcart),
    path('edit_shoppingcart/', views.edit_shoppingcart),
    path('selected_books_preview/', views.selected_books_preview),
    path('creat_new_order/', views.creat_new_order),
    path('ret_all_orders/', views.ret_all_orders),
    path('ret_unreceived_orders/', views.ret_unreceived_orders)
]
