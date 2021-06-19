from django.urls import path
from trade import views


urlpatterns = [
    path('show_shoppingcart/', views.show_shoppingcart),
    path('add_to_shoppingcart/', views.add_to_shoppingcart),
    path('del_from_shoppingcart/', views.del_from_shoppingcart),
    path('edit_shoppingcart/', views.edit_shoppingcart),
    path('creat_new_order/', views.creat_new_order),
    path('set_order_received/', views.set_order_received),
    # path('ret_order_details/', views.ret_order_details),
    path('ret_all_orders/', views.ret_all_orders),
    # path('ret_unreceived_orders/', views.ret_unreceived_orders),
    path('all_orders_with_details/', views.all_orders_with_details),
    path('new_order_single_book/', views.new_order_single_book),
]
