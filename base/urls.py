from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mixed/', views.mixed_fraction, name='mixed'),
    path('random/', views.random_simple, name='random'),
    path('random/mixed/', views.random_mixed, name='random_mixed'),
    path('convertor/', views.convertor, name='convertor')
]