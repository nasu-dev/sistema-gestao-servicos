from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Verifique os campos em vermelho')

    else:
        form = ClienteForm()

    return render(request, 'clientes/form.html', {
        'form': form,
        'titulo': 'Cadastrar Clientes'
    })

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Verifique os campos em vermelho')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Editar Cliente'})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, 'Cliente excluído com sucesso!')
    return redirect('listar_clientes')
