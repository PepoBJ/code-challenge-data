# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido de la carpeta src al directorio de trabajo del contenedor
COPY ./src /app/src

# Copia el archivo requirements.txt al directorio de trabajo del contenedor
COPY ./requirements.txt /app/requirements.txt

# Instala las dependencias del proyecto y gettext-base para manejar las variables de entorno
RUN apt-get update && \
    apt-get install -y unixodbc-dev gettext-base && \
    pip install --no-cache-dir -r requirements.txt

# Copia el archivo .env al directorio de trabajo del contenedor
COPY .env /app/.env

# Instala el controlador ODBC de SQL Server
RUN apt-get update && \
    apt-get install -y gnupg2 && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Expone el puerto en el contenedor
EXPOSE 5000

# Ejecuta el comando para iniciar la aplicación
CMD ["python", "src/app.py"]
