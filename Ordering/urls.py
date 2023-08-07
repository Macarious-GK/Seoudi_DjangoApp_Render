from django.urls import path
from Ordering.views import *
from Ordering import views


urlpatterns = [
    path('',views.order, name = 'order'),
]