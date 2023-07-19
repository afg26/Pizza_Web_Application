from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home Page'),
    path('Menu_Page/', views.MenuPage, name='Menu Page'),
    path('create/', views.create, name='Customize_Pizza'),  # Corrected URL pattern name
    path('cart/', views.view_cart, name='View Cart'),
    path('cart/remove/<int:pizza_id>/', views.remove_from_cart, name='remove_from_cart'),
]