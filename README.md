# Desafio Técnico - Python/Django

## Sobre o Projeto

Projeto criado para o desafio técnico da TechnoTech Sistemas, para a vaga de estágio em Python/Django.

## Variáveis de Ambiente

- Crie um arquivo ```.env``` na raiz do projeto e preencha com os valores necessários.
- Use ```.env.example``` como referência.

## Executando com Docker

### Requisitos
- Docker + Docker Compose instalados.

### Passos

1. Clone o repositório:

    ```
    git clone https://github.com/alfredoherculano/academia-dev-python
    cd academia-dev-python
    ```

2. Inicie os serviços:

    ```docker compose up --build```

3. Rode as migrações (somente na primeira execução):

    ```docker compose run django-web python manage.py migrate```

4. Acesse a aplicação:

    ```http://127.0.0.1:8000```