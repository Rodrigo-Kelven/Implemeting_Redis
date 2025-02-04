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
