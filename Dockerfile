FROM python:3.11-slim

WORKDIR /app

# Copia primeiro o requirements (pra cache funcionar)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Porta da API
EXPOSE 8080

# Comando correto
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]