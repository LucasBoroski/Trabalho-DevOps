# Imagem base do Python
FROM python:3.11-slim

# Diretório dentro do container
WORKDIR /app

# Copia todos os arquivos
COPY . .
RUN pip install -r requirements.txt
# Comando para rodar a aplicação
CMD ["python", "app.py"]
