from django.urls import path
from Ordering.views import *
from Ordering import views


urlpatterns = [
    path('customers/',views.customer_CR, name= 'customers'),
    path('customers/<int:pk>/',views.customer_UD, name= 'customersid'),
]