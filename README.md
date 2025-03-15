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
python -m venv .venv
source .venv/bin/activate  # En Windows usar: venv\Scripts\activate
pip install -r requirements.txt
```

### Configurar la base de datos

Editar el fichero `config.py` con los datos de conexión a MySQL.

### Ejecutar la aplicación

Para desarrollo:

```bash
python app.py
```

```bash
FLASK_ENV=development python app.py
```

Para producción:

```bash
FLASK_ENV=production python app.py
```

## Ejecución con Docker

### Construcción de la imagen

```bash
docker build -t contactos-app .
```

### Ejecución del contenedor

En desarrollo:

```bash
docker run -d -p 5000:5000 \
    -e DB_USER="contactos_user" \
    -e DB_PASSWORD="ChangeMe!" \
    -e DB_HOST="localhost" \
    -e DB_NAME="contactos_db" \
    --name contactos-container contactos-app
```


```bash
docker run -d -p 5000:5000 \
    -e FLASK_ENV=development \
    -e DB_USER="contactos_user" \
    -e DB_PASSWORD="ChangeMe!" \
    -e DB_HOST="localhost" \
    -e DB_NAME="contactos_db" \
    --name contactos-container contactos-app
```

En producción:

```bash
docker run -d -p 5000:5000 \
    -e FLASK_ENV=production \
    -e DB_USER="contactos_user" \
    -e DB_PASSWORD="ChangeMe!" \
    -e DB_HOST="localhost" \
    -e DB_NAME="contactos_db" \
    --name contactos-container contactos-app
```

## Ejecución con Docker Compose

En desarrollo:

```bash
docker-compose up -d
```

En producción, primero descomentar la línea 28 del fichero docker-compose.yaml y ejecutar:

Esto ejecutará un contenedor de MySQL y la aplicación Flask con la configuración correcta.

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
python test_app.py
```
