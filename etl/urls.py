from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('upload/', views.dataset_upload, name='dataset_upload'),
]