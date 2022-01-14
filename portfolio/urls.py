
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings

from django.views.static import serve
from django.conf.urls import  url, urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
