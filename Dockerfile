FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /sge_dmaster

# Copiar requirements primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do projeto
COPY . .

# Criar diretórios necessários
RUN mkdir -p /sge_dmaster/staticfiles /sge_dmaster/media

# Expor a porta 8000
EXPOSE 8000

# O comando será sobrescrito pelo docker-compose