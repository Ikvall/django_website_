from django.urls import path
from . import views


urlpatterns = [
    path('', views.etheria, name='etheria'),
    path('firstpage/', views.firstpage, name = 'firstpage'),
]