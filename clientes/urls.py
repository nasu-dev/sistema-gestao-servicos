from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_clientes, name='Listar_clientes'),
]