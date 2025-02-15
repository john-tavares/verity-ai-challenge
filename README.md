# Verity AI Challenge
Este projeto é uma aplicação web desenvolvida com Streamlit que integra um agente SQL para responder a perguntas relacionadas aos dados. O fluxo da aplicação é definido utilizando a biblioteca LangGraph, que orquestra a execução de nós (nodes) no fluxo. A comunicação com o banco de dados PostgreSQL é realizada com base nas variáveis definidas no arquivo .env, e a API do OpenAI é utilizada para processar as perguntas.

## Pré-requisitos
- Docker
- API KEY da OpenAI

## Configuração
```bash
git clone <URL_DO_REPOSITÓRIO>
```
Crie um arquivo chamado ```.env``` na raiz do projeto e adicione as seguintes variáveis:
``` bash
OPENAI_API_KEY="<insert-here>"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
POSTGRES_USER="admin"
POSTGRES_PASSWORD="Postgres2025!"
POSTGRES_DATABASE="banco_roxinho"
```
Atenção: Substitua <insert-here> pela sua chave de API do OpenAI e ajuste os demais valores conforme necessário para o seu ambiente.

## Execução
Execute o comando abaixo para iniciar o banco de dados (opcional):

```bash
docker compose up -d
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Execute o Streamlit:
```bash
streamlit run main.py
```