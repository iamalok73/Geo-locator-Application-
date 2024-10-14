from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_country/', views.get_country, name='get_country'),
]
