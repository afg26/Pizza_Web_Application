from django.contrib import admin
from django.urls import path, include
from user_login import views as v
#from Create_your_own import views as create






urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/' , v.sign_up, name= 'sign_up'),
    path('', include ('main_core.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    #path('Create_your_own/', create.customize_pizza, name='create_your_own'),

    
]
