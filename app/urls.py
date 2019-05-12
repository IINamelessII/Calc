from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
]