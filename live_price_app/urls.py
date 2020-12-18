from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from informations.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^search/', search),
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    path('', include('informations.urls')),
]
