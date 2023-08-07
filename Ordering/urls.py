from django.urls import path
from Ordering.views import *
from Ordering import views


urlpatterns = [
    path('',views.order, name = 'order'),
    path('customers/',views.customer_CR, name= 'customers'),
    path('customers/<int:pk>/',views.customer_UD, name= 'customersid'),
]