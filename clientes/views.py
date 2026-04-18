from django.shortcuts import render
from .models import Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})
