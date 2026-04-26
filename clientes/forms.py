from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'endereco', 'observacoes']
        error_messages = {
            'nome': {'required': 'Informe o nome do cliente'},
            'telefone': {'required': 'Informe o telefone'},
            'email': {'invalid': 'Digite um e-mail válido'}
        }