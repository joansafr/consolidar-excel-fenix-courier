# Consolidar la data de los archivos excel del Courier Fenix Perú

### Instrucciones para ejecutar el proyecto

## Requisitos previos

1. Asegúrate de tener instalado [Python](https://www.python.org/downloads/).
2. Instala las dependencias necesarias ejecutando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución del proyecto

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu_usuario/consolidar_excel.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd consolidar_excel
    mkdir data
    mkdir output
    ```
3. Pon los archivos excel en la carpeta data.

4. Ejecuta el script principal:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python src/consolidate_excel.py
    ```

## Notas adicionales

- Asegúrate de tener los archivos de entrada necesarios en el directorio especificado.

¡Listo! Ahora deberías poder ejecutar el proyecto sin problemas.