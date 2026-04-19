from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar'),
]
