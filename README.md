# Python-API-V1
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/GabrielSS187Python_API-V1/blob/main/LICENSE) 

# Sobre o projeto

### API Documentação: [Python-API-V1-DOC](https://documenter.getpostman.com/view/18692384/2s93eeRpud)

#### OBS: API construida para fins de meus estudos com Python.

A API: ``Python-API-V1``, consiste em ser uma api rest facíl de sí usar. Para gerenciar qualquer tipo de produtos.
``CRUD`` completo, onde você pode criar, buscar, editar e deletar produtos e clientes criados. Também é possível
que os clientes cadastrados / registrados no sistema, contratarem os produtos disponíveis, caso ele esteja autenticado.

## Rotas

### User
- 1 - ``SIGN-UP`` : ``POST`` http://localhost:8000/user/sign-up
- 2 - ``SIGN-IN`` : ``POST`` http://localhost:8000/user/sign-in

### Product
- 1 - ``CREATE-PRODUCT`` : ``POST`` http://localhost:8000/product
- 2 - ``EDIT-PRODUCT`` : ``PATCH`` http://localhost:8000/product/:id
- 3 - ``DELETE-PRODUCT`` : ``DELETE`` http://localhost:8000/product/:id
- 4 - ``GET-PRODUCT`` : ``GET`` http://localhost:8000/product/:id
- 5 - ``GET-ALL-PRODUCT`` : ``GET`` http://localhost:8000/product
- 6 - ``GET-ALL-CATEGORIES`` : ``GET`` http://localhost:8000/product/categories

## Modelagem Conceitual de Dados
![Captura de Tela (372)](https://github.com/GabrielSS187/Python-API-V1/assets/86306877/172c3b4d-b587-4d2a-90a0-2e198b817f48)

## Competências
- Boas Práticas
- Clean Code

# Tecnologias utilizadas

## Banco de dados
- MySQL

## ORM
- SQLAlchemy

## Outras Tecnologias
- Python
- alembic
- Flask
- Flask-Cors
- Flask-JWT-Extended
- Flask-SQLAlchemy
- mysqlclient
- python-dotenv

# Como executar o projeto na sua máquina 💻💻

#### Pré-requisitos: Python / MySQL URL
#### É preencher as variáveis de ambiente do .env

#### ===============================================================================

#### Passo 1
- Clone o repositório
```bash
# Clonar
git clone https://github.com/GabrielSS187/Python-API-V1.git

# Entre na pasta 
cd Python-API-V1
```

#### Passo 2
- Crie seu ambiente virtual
``` bash
# Criar ambiente virtual
python -m venv env

# Ativar ambiente virtual Linux ou Mac
source env/bin/activate

# Ativar ambiente virtual Windows
env\Scripts\activate
```

#### Passo 3
- Instale todas as dependências
```bash
# Instalar
pip install -r ./requirements.txt
```
- Depois de terminado de instalar todas as dependências, de um `reload / restart` no seu editor de códigos.

#### Passo 4
##### Preencher as variáveis de ambiente no arquivo `.env` e depois cole á sua `URL` de conexão com o `MySQL` no arquivo `alembic.ini` 👇👇👇
-  1 - `.env` : Tire o nome `.exemple` do arquivo `.env.exemple` e preencha todas as variáveis de ambiente necessárias.
-  2 - `alembic.ini` : Entre nesse arquivo e navegue até o nome `sqlalchemy.url =` depois do sinal de igual, cole sua `URL` de
-  conexão com o `MySQL`.

#### Passo 5
- Depois de ter feito tudo isso, rode o comando para subir todas as migrações para seu banco de dados
```bash
alembic upgrade head
```

#### Passo 6 - Final
- Por fim, entre na pasta `infra`, e rode o comando para iniciar o servidor
```bash
# Entrar na pasta infra
cd infra

# Iniciar o servidor
flask run
```
#### =================================================================================

### Caso nada de errado o projeto vai esta rodando na rota: http://127.0.0.1:5000

# Autor

Gabriel Silva Souza

https://www.linkedin.com/in/gabriel-silva-souza-developer

