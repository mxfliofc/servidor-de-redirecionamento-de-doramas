# Use a imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Crie um ambiente virtual
RUN python -m venv /opt/venv

# Ative o ambiente virtual e instale as dependências do Python
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta em que a aplicação estará rodando
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
