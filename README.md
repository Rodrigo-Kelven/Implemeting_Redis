# FastAPI with SQLite and Redis

Este projeto é uma API RESTful construída com FastAPI, utilizando SQLite como banco de dados e Redis para caching. A API permite a criação e leitura de itens, armazenando dados em um banco de dados SQLite e utilizando Redis para melhorar a performance através de caching.

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido para construir APIs com Python 3.6+ baseado em tipos.
- **SQLite**: Um banco de dados leve e autônomo que armazena dados em um único arquivo.
- **Redis**: Um armazenamento de estrutura de dados em memória, usado como um sistema de caching.
- **SQLAlchemy**: Um ORM (Object Relational Mapper) para interagir com o banco de dados SQLite.
- **Pydantic**: Para validação de dados e serialização.


## Pré-requisitos

Antes de começar, você precisará ter o Docker e o Docker Compose instalados em sua máquina.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Rodrigo-Kelven/Implemeting_Redis
   cd Implemeting_Redis
   docker-compose up --build

   
## Endpoints
### Criar um Item

- URL: /items/

- Método: POST

## Corpo da Requisição:



    {

    "name": "Item 1",

    "description": "Descrição do Item 1"

    }

## Resposta:


    {

    "name": "Item 1",

    "description": "Descrição do Item 1"

    }

## Ler um Item

- URL: /items/{name}

- Método: GET

#### Parâmetros:
- name: O nome do item que você deseja recuperar.

### Resposta:



    {

    "name": "Item 1",

    "description": "Descrição do Item 1"

    }

# Testando a API

### Você pode usar ferramentas como Postman ou cURL para testar a API.
#### Exemplo de Requisição com cURL
### Criar um Item


- curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"name": "Item 1", "description": "Descrição do Item 1"}'

### Ler um Item

- curl -X GET "http://localhost:8000/items/Item%201"

# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
