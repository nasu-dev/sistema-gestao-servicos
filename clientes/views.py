from django.shortcuts import render
from .models import Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def cadastrar_cliente(request):
    print(request.method)
    print(request.POST)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        if nome and telefone:
            Cliente.objects.create(nome=nome, telefone=telefone)
    return render(request, 'clientes/cadastrar.html')
