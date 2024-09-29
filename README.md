# Projeto API Django - Filmes

Este é um projeto Django que implementa uma API REST para gerenciar filmes, gêneros, atores e reviews. O projeto contém um CRUD completo para cada uma das entidades mencionadas, utilizando os recursos do Django Rest Framework.

## Funcionalidades Principais

- **Apps:**
  - Filmes
  - Gêneros
  - Atores
  - Reviews
  
- **CRUDs:**
  - Cada app possui operações de Create, Read, Update e Delete, implementadas usando os **generics** do Django Rest Framework.

- **Validações:**
  - Validações de dados implementadas nos **serializers** para garantir a integridade das informações.
  
- **Campos Calculados:**
  - Alguns campos são calculados diretamente nos **serializers**, como a média de avaliações (reviews) de um filme.

- **Token JWT**
  - A API itliza um token JWT para liberar o uso dos endpoints. Para gerar ele basta ter um usuario cadastrado e passar o token gerado via "Barer Token"

## Documentação da API

A API possui documentação acessível nos seguintes endpoints:

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc UI:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Passo a Passo para Instalação e Execução do Projeto

Siga os passos abaixo para instalar e executar o projeto localmente:

### 1. Clonar o Repositório
Clone o repositório para sua máquina local usando o seguinte comando:
```bash
git clone https://github.com/VitorMonteiroVianna/Filmes_python_api.git
```

### 2. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:
```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
Navegue até o diretório do projeto e instale as dependências listadas no arquivo `requirements.txt:`
```bash
cd <caminho_do_projeto>
pip install -r requirements.txt
```

### 4. Aplicar as Migrações
Após instalar as dependências, você precisa aplicar as migrações para configurar o banco de dados:
```bash
python manage.py migrate
```

### 5. Criar Superusuário
Crie um superusuario, para poder usar o endpoint de Authentication e acessar os endpoints da API:
```bash
python manage.py createsuperuser
```

### 6. Executar o Projeto
Finalmente, execute o servidor de desenvolvimento do Django. Quando o comando rodar, ja vai ser possivel acessar o projeto:
```bash
python manage.py runserver
```

