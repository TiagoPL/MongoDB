FROM python:3.10
WORKDIR /app
COPY . /app

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]