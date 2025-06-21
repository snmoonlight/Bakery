from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('sales', views.sales),
    path('menu', views.menu),
    path('enter', views.enter),
    path('registration', views.registration)
]