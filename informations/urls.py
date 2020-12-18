from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('search', views.search, name='search')
    #path('', views.index, {'searchitem': ''}, name='home'),
    #path('<str:searchitem>', views.index, name='index'),
]

