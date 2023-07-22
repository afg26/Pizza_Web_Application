from django.contrib import admin
from django.urls import path, include
from user_login import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/' , v.sign_up, name= 'sign_up'),
    path('', include ('main_core.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    
]
