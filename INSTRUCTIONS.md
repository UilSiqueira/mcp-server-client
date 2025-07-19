# 🐳 Setup Instructions

## 🚀 Como executar o projeto

### 1️⃣ Pré-requisitos

- Docker
- Docker Compose
- Chave da OpenAI (GPT-4o ou outro modelo)

---

### 2️⃣ Configuração

Crie um arquivo `.env`  na raiz do projeto com: 
```bash
OPENAI_API_KEY=sk-your-api-key
```
---
📦 Passo a passo

## 1. Clone o repositório

```bash
git clone git@github.com:UilSiqueira/mcp-server-client.git
cd mcp-server-client
```


## 2. Suba os containers

```bash
docker-compose up -d --build
```


## 3. Aplique as migrações

```bash
docker-compose exec server alembic upgrade head
```

## 5. Popule o banco de dados

```bash
docker-compose exec server env PYTHONPATH=/app python app/seed.py

```

## 6. Faça o teste

```bash
docker-compose run --rm client

```

✅ Pronto!

Se tudo estiver certo, o mcp server estará pronto para processar requisições.
