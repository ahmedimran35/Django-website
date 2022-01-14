
from django.contrib import admin
from django.urls import path,include
from home import views
#from portfolio.home.views import skills

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path ("educations",views.educations,name='educations'),
    path ("services",views.services,name='services'),
    path ("works",views.works,name='works'),
    path ("contact",views.contact,name='contact')

]
