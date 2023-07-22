from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home Page'),
    path('Menu_Page/', views.MenuPage, name='Menu Page'),
    path('create/', views.create, name='Customize Pizza'),
    path('cart/', views.view_cart, name='View Cart'),
    path('remove_from_cart/', views.remove_from_cart, name='Remove From Cart'),
]
