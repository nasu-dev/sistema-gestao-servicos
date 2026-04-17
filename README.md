Sistema de Gestão de Serviços
=============================

Descrição
---------
Sistema de gestão de serviços em desenvolvimento com Django.
Atualmente permite cadastro de clientes com persistência em banco de dados e gerenciamento via painel administrativo.

Status atual
------------
- Cadastro de clientes
- Edição e exclusão de clientes
- Persistência com banco SQLite
- Acesso via painel administrativo do Django
- Validação CRUD de clientes via admin

Próximas implementações
-----------------------
- Interface própria para usuários (sem uso do admin)
- Módulo de serviços
- Sistema de agendamentos
- Controle financeiro

Tecnologias utilizadas
----------------------
- Python
- Django
- Git

Como executar
-------------
Clone o repositório:
git clone https://github.com/seu-usuario/sistema-gestao-servicos.git

Acesse a pasta:
cd sistema-gestao-servicos

Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Execute o projeto:
python manage.py runserver

Acesse no navegador:
http://127.0.0.1:8000/admin/

Autor
-----
Anderson Nasu