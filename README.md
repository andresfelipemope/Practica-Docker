# Practica Docker - Aplicación de Notas

Proyecto de contenedorización con FastAPI y Docker Compose.

## Requisitos
- Python 3.13
- Docker
- Docker Compose

## Estructura
- `app/main.py`: API FastAPI que guarda notas en `notas.txt`
- `Dockerfile`: imagen basada en `python:3.13-alpine`
- `docker-compose.yaml`: servicio `api` con volumen `./data:/data`
- `app/requirements.txt`: dependencias necesarias
- `data/`: carpeta local donde se persisten las notas

## Comandos locales
1. Crear y activar entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Instalar dependencias:
```bash
python3 -m pip install --upgrade pip
pip install -r app/requirements.txt
```
3. Ejecutar la aplicación:
```bash
cd app
python3 main.py
```
4. Probar con curl:
```bash
curl -X POST http://localhost:8000/nota -d "Mi primera nota"
curl http://localhost:8000/
```

## Comandos con Docker
1. Construir imagen:
```bash
docker compose build
```
2. Levantar el servicio:
```bash
docker compose up
```
3. Verificar nota:
```bash
curl -X POST http://localhost:8000/nota -d "Mi primera nota"
curl http://localhost:8000/
```
4. Detener:
```bash
docker compose down
```

## Persistencia
La nota se guarda en el archivo `data/notas.txt`.
En Docker el volumen está montado con `./data:/data`, por lo que los datos persisten en el host.
