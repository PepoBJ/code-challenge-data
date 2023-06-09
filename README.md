# Data Engineering Coding Challenge

Este repositorio contiene un challenge de código de ingeniería de datos.

<br>

![Badge](https://github.com/PepoBJ/code-challenge-data/workflows/Deploy%20to%20Azure/badge.svg)

## Índice
---
1. [Estructura del proyecto](#estructura-del-proyecto)
2. [Configuración del entorno](#configuración-del-entorno)
3. [Comandos de migración con Docker](#comandos-de-migración-con-docker)
4. [Ejecución de los test unitario (Dockerfile)](#ejecución-de-las-pruebas)
5. [Ejecución del proyecto con Docker (Dockerfile)](#ejecución-del-proyecto-con-docker-dockerfile)
6. [Documentación de API](#documentación-de-api)
7. [Despliegue en Azure](#despliegue-en-azure)
8. [Licencia](#licencia)

<br>

## 1. Estructura del proyecto <a name="estructura-del-proyecto"></a>
---

La estructura de carpetas del proyecto es la siguiente:

```
├─── .github
├─── src
├─── test
├─── .env.template
├─── Dockerfile
├─── Dockerfile.tests
└─── requirements.txt
```

El proyecto contiene las siguientes carpetas y archivos importantes:

- `.github`: Contiene los archivos de configuración para acciones y flujos de trabajo de GitHub.
- `src`: Carpeta que contiene el código fuente del proyecto.
- `test`: Carpeta que contiene las pruebas unitarias del proyecto.
- `.env.template`: Plantilla del archivo `.env` para facilitar la configuración.
- `Dockerfile`: Archivo de configuración para construir la imagen del contenedor principal.
- `Dockerfile.tests`: Archivo de configuración para construir la imagen del contenedor de pruebas.
- `requirements.txt`: Archivo que contiene las dependencias del proyecto en formato `pip`.

<br>

## 2. Configuración del entorno <a name="configuración-del-entorno"></a>

---

Para ejecutar el proyecto y las pruebas, se requiere la configuración del entorno. Asegúrate de tener las siguientes variables de entorno configuradas:

- `HOST`: La dirección IP o el nombre de host donde se ejecutará la aplicación.
- `DEBUG`: Indicador para habilitar o deshabilitar el modo de depuración de la aplicación.
- `CONNECTION_STRING_AZURE_SQL`: Cadena de conexión para la base de datos Azure SQL.
- `PORT`: El número de puerto en el que la aplicación estará escuchando.

<br>

## 3. Comandos de migración con Docker <a name="comandos-de-migración-con-docker"></a>

---

Puedes ejecutar los siguientes comandos de migración de base de datos utilizando Docker:

```bash
docker build -t code-challenge .
docker run --rm code-challenge python src/app.py db_init
docker run --rm code-challenge python src/app.py db_clean
docker run --rm code-challenge python src/app.py db_procedure_init
docker run --rm code-challenge python src/app.py db_procedure_clean
```

- `db_init`: Este comando inicia la migración de la base de datos. Crea las tablas y procedimientos almacenados necesarios para el funcionamiento del proyecto.

- `db_clean`: Este comando limpia la base de datos, eliminando todas las tablas y procedimientos almacenados creados anteriormente.

- `db_procedure_init`: Este comando inicializa los procedimientos almacenados de métricas en la base de datos. Estos procedimientos se utilizan para calcular métricas específicas del proyecto.

- `db_procedure_clean`: Este comando elimina los procedimientos almacenados de métricas de la base de datos.


<br>

## 4. Ejecución de los test unitario (Dockerfile) <a name="ejecución-de-las-pruebas"></a>

---

El proyecto incluye pruebas unitarias que se pueden ejecutar mediante Docker. Asegúrate de tener Docker instalado en tu sistema antes de ejecutar las pruebas.

Para ejecutar las pruebas, sigue los siguientes pasos:

1. Abre una terminal en la carpeta raíz del proyecto.
2. Ejecuta el siguiente comando para construir la imagen del contenedor de pruebas:

   ```shell
   docker build -t code-challenge-test-image -f Dockerfile.tests .
   ```

3. Después de que se construya la imagen, ejecuta el siguiente comando para ejecutar el contenedor de pruebas:

   ```shell
   docker run -it --rm code-challenge-test-image
   ```

4. Verifica la salida de la ejecución de las pruebas en la terminal. Si todas las pruebas pasan, se mostrará un mensaje indicando que las pruebas han sido exitosas.

Si alguna prueba falla, se mostrará un mensaje de error correspondiente y se puede investigar la causa del fallo.

<br>

## 5. Ejecución del proyecto con Docker (Dockerfile) <a name="ejecución-del-proyecto-con-docker-dockerfile"></a>

---

Puedes ejecutar el proyecto utilizando Docker con los siguientes pasos:

1. Construir la imagen Docker:
```
docker build -t code-challenge .
```

2. Ejecutar el contenedor Docker:
```
docker run -d -p 5000:5000 --name code-challenge-container code-challenge
```

Esto creará un contenedor Docker a partir de la imagen `code-challenge` y expondrá el puerto 5000 paraacceder a la aplicación.)
Una vez que el contenedor esté en ejecución, podrás acceder a la aplicación en `http://localhost:5000`.


<br>

## 6. Documentación de API <a name="documentación-de-api"></a>

---

El proyecto utiliza Swagger para generar y proporcionar documentación de la API. Después de iniciar la aplicación, se puede acceder a la documentación de los endpoints a través de la siguiente URL local:

```
http://localhost:5000/swagger
```

Asegúrate de reemplazar `localhost` y `5000` con la dirección IP y el puerto correspondientes si has configurado valores diferentes en tu entorno.


<br>

## 7. Despliegue en Azure <a name="despliegue-en-azure"></a>

---

El despliegue del proyecto en Azure se realiza automáticamente cuando se realizan cambios en la rama `master` y todas las pruebas unitarias pasan con éxito.

El archivo `.github/workflows/pipeline-deploy-azure.yml` contiene la configuración para el despliegue automatizado en Azure. Aquí se realiza la construcción de la imagen del contenedor principal, se ejecutan las pruebas unitarias y, si todas las pruebas pasan, se publica la imagen en Azure Container Registry.

El despliegue en Azure requiere la configuración de las siguientes variables de entorno y secretos:

- `CONNECTION_STRING_AZURE_SQL`: Cadena de conexión para la base de datos Azure SQL.
- `ACR_USERNAME` y `ACR_PASSWORD`: Credenciales de inicio de sesión para Azure Container Registry.


<br>

## 8. Licencia <a name="licencia"></a>

---

Este proyecto está bajo la Licencia [MIT](LICENSE). Si deseas obtener más información, consulta el archivo LICENSE.
