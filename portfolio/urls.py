
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

    
]
