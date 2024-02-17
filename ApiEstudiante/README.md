# Ejemplo: FastAPI - Estudiante API - Uniminuto

## Autor
- [Jose Danilo Sanchez]

## Prerrequisitos
Para la instalación de esta solución se requiere la instalación de las siguientes aplicaciones en un sistema operativo WINDOWS o Linux:

- [Python](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe) - PYTHON v.3.10 (including PIP and adding to PATH)

## Instalación de las dependencias de la solución

Esta aplicación se basa en el uso de algunas bibliotecas (módulos) para llevar a cabo la ejecución del componente de interfaz gráfica relacionado con la iniciativa.

| Dependencies | Purpose |
| ------ | ------ |
| FastAPI| Microframework used for the management of APIs related to ELK components |
| Uvicorn | Library used to deploy the APIs related to the example from FAST API Framework |
| Requests | Library for handling HTTP request types in the software component |


A continuación, deben ejecutarse las siguientes instrucciones a través de la línea de comandos

Instalación de dependencias

```sh
  pip install -r requirements.txt
```

## Desplegar la solución

Una vez descargado el código fuente, se debe ejecutar la siguiente instrucción, ya sea desde el entorno de desarrollo integrado llamado Pycharm o directamente desde la carpeta raíz del proyecto, utilizando el siguiente comando:

```sh
 uvicorn main:estudiante_api --reload --port 9999
```
or

```sh
python3 -m uvicorn main:estudiante_api --reload --port 9999
```

Por defecto, el sistema utilizará la URL localhost(127.0.0.1) y el puerto 8000, sin embargo, para esta ocasión se utilizará el puerto 9999.

```sh
127.0.0.1:9999
```

## Ejecución y ejemplo

Para ejecutar la solución, debe utilizar la URL http://localhost:9999/docs


## Licencia
MIT
