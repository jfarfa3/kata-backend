# Cine Reservation Management System

## Descripción

Este proyecto es un sistema de gestión de reservas para un cine, desarrollado con FastAPI y PostgreSQL.

## Requisitos

- Docker
- Docker Compose
- Python 3.9+
- pip

## Instrucciones de Arranque

### Usando Docker

1. Clonar el repositorio:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd middle-cloud-challenge-2/backend
    ```

2. Crear un archivo `.env` en el directorio `backend` con las siguientes variables de entorno:

    ```env
    DATABASE_URL=postgres://postgres:password@db:5432/postgres
    MAILERSEND_API_KEY=your_mailersend_api_key
    ```

3. Construir y levantar los contenedores de Docker:

    ```sh
    docker-compose up --build
    ```

4. La aplicación estará disponible en `http://localhost:8080`.

### Usando Python directamente

1. Clonar el repositorio:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd middle-cloud-challenge-2/backend
    ```

2. Crear un entorno virtual y activarlo:

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instalar las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Crear un archivo `.env` en el directorio `backend` con las siguientes variables de entorno:

    ```env
    DATABASE_URL=postgres://postgres:password@localhost:5436/postgres
    MAILERSEND_API_KEY=your_mailersend_api_key
    ```

5. Iniciar la aplicación:

    ```sh
    fastapi dev app/main.py --port 8080
    ```

6. La aplicación estará disponible en `http://localhost:8080`.

## Endpoints

- `GET /health`: Verifica el estado de la aplicación.
- `GET /`: Verifica el estado de la aplicación.

## Notas

- Asegúrese de tener Docker y Docker Compose instalados en su máquina.
- El archivo `init-db.sql` se ejecutará automáticamente al iniciar el contenedor de la base de datos para inicializar la base de datos.