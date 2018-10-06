from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='financeiro-home'),
    path('cliente', views.cliente, name='financeiro-cliente'),
    path('empresa', views.empresa, name='financeiro-empresa'),
    path('fornecedor', views.fornecedor, name='financeiro-fornecedor'),
]