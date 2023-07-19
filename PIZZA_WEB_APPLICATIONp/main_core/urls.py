from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name= "Home Page"),
    path('Menu_Page/', views.MenuPage,  name= 'Menu Page'),
    path('about_page/', views.About_Page, name= 'About')
    
          
]