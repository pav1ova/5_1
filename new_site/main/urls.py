from django.urls import path
from .import views

urlpatterns = [

    path('index', views.index),
    path('about', views.about),
    path('company', views.company),
    path('main',views.main, name = 'Main' )
]