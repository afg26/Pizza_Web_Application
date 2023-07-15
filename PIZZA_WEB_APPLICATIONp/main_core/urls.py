from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name= "Home Page"),
    path('Menu_Page/', views.MenuPage,  name= 'Menu Page'),
    
          
]