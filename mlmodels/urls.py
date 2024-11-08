from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_list, name='model_list'),
    path('create/', views.model_create, name='model_create'),
]