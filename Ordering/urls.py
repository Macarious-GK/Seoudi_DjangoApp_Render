from django.urls import path
from Ordering.views import *
from Ordering import views


urlpatterns = [
    path('customers/',views.customer_CR, name= 'customers'),
    path('customers/<int:pk>/',views.customer_UD, name= 'customersid'),
    path('items/',views.item_CR, name= 'item-cr'),
    path('items/<int:pk>/',views.item_UD, name= 'item-ud'),
    path('orders/',views.order_CR, name= 'order-cr'),
    path('orders/<int:pk>/',views.order_UD, name= 'order-ud'),
    path('status/<int:pk>/',views.status_R, name= 'status-get'),

]