from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')

        if not nome or not telefone:
            return render(request, 'clientes/cadastrar.html', {
                'erro': 'Preencha todos os campos',
                'nome': nome,
                'telefone': telefone
            })
        if nome and telefone:
            Cliente.objects.create(nome=nome, telefone=telefone)
            return redirect('listar_clientes')
    return render(request, 'clientes/cadastrar.html')

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')

        if not nome or not telefone:
            return render(request, 'clientes/editar.html', {
                'cliente': cliente,
                'erro': 'Preencha todos os campos',
                'nome': nome,
                'telefone': telefone
            })
        cliente.nome = nome
        cliente.telefone = telefone
        cliente.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/editar.html', {'cliente': cliente})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('listar_clientes')
