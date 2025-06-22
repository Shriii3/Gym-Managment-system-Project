from django.urls import path 
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index ,name = 'index'),
    path('signup/',signup,name='SignUp'),
    path('login/',user_login,name='Login'),
    path('logout/',user_logout,name = 'logout'),
    path('about/', about , name = 'about'),
    path('contact/' , contact , name = 'contact'),
    path('offer/' , offer , name = 'offer'),
    path('price/' , price , name = 'price'),
    path('trainer/' , trainer , name = 'trainer'),
    path('join/' , Join , name = 'join'),
    path('review/' , review , name = 'review'),
    path('payment/<str:pay>/' , Payment , name = 'payment'),
    path('Demo/' , demo , name = 'demo'),
   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
