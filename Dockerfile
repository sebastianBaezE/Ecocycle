FROM python:3.10.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Recoge los archivos estáticos
RUN python3 manage.py collectstatic --no-input

# Define el comando por defecto para ejecutar cuando se levante el contenedor
CMD ["sh", "-c", "python3 manage.py migrate && \
                   python3 manage.py seed_database && \
                   python3 manage.py create_superuser && \
                   python -m gunicorn ecocycle.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000"]