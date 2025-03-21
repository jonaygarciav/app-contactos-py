# Contactos App

## Descripción

Aplicación CRUD en Flask con MySQL y Bootstrap que muestra una tabla con los contactos almacenados en la base de datos. No permite insertar, editar ni eliminar contactos en esta versión.

## Requisitos
- Python 3.9+
- MySQL
- Docker (opcional para despliegue)

## Instalación y ejecución manual

### Crear entorno virtual e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Configurar la base de datos

Editar el fichero `config.py` con los datos de conexión a MySQL.

### Ejecutar la aplicación

## En la terminal:

```bash
python3 app.py
```

## Ejecución con Docker

### Construcción de la imagen

```bash
docker build -t app-contactos-py .
```

### Ejecución del contenedor

```bash
docker run -d -p 5000:5000 \
    -e DB_USER="contactos_user" \
    -e DB_PASSWORD="ChangeMe!" \
    -e DB_HOST="localhost" \
    -e DB_NAME="contactos_db" \
    --name app-contactos-py app-contactos-py
```

## Ejecución con Docker Compose

```bash
docker-compose up -d
```

Para borrar la caché de Docker Compose:

```bash
docker-compose stop
docker-compose rm
docker-compose down --volumes --rmi all
```

## Pruebas unitarias (testing)

Para ejecutar las pruebas unitarias:

```bash
python3 test_app.py
```

## Probar la aplicación en local

Acceder a la URL http://localhost:5000 a través del navegador web.

A travé de la terminal ejecutar el comando `curl`:

```bash
curl http://localhost:5000
```

