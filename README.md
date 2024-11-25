
# Gestor de Paquetes para Librerías de Python

Este es un proyecto desarrollado en Python con una interfaz gráfica utilizando `customtkinter`. 
El programa permite gestionar librerías de Python instaladas con `pip` de manera sencilla, 
ofreciendo funcionalidades como instalación, desinstalación, actualización, búsqueda y más.

## Funcionalidades

- **Instalar Librería:** Instala una librería utilizando su nombre, desde un archivo `requirements.txt`, 
  o con un solo clic para librerías populares.
- **Desinstalar Librería:** Permite desinstalar una librería seleccionada.
- **Actualizar Librería:** Actualiza a la última versión una librería instalada.
- **Ver Librerías Instaladas:** Lista todas las librerías instaladas actualmente en el entorno.
- **Buscar Librerías:** Permite buscar información sobre librerías en el índice oficial de PyPI.
- **Instalar desde `requirements.txt`:** Instala todas las librerías listadas en un archivo de requisitos.
- **Salir:** Cierra la aplicación.

## Uso

1. **Instalar Librería:** Haz clic en "Instalar" y escribe el nombre de la librería o selecciona 
   una opción rápida para instalar librerías populares.
2. **Desinstalar Librería:** Selecciona una librería de la lista y haz clic en "Desinstalar".
3. **Actualizar Librería:** Selecciona una librería de la lista y haz clic en "Actualizar".
4. **Ver Librerías Instaladas:** Haz clic en "Mostrar librerías" para visualizar todas las librerías instaladas.
5. **Buscar Librerías:** Escribe el nombre de una librería y haz clic en "Buscar" para obtener información de PyPI.
6. **Instalar desde `requirements.txt`:** Haz clic en "Cargar archivo", selecciona tu archivo de requisitos y sigue las instrucciones.
7. **Salir:** Haz clic en "Salir" para cerrar la aplicación.

## Requisitos

- Python 3.x
- `customtkinter` (puedes instalarlo ejecutando `pip install customtkinter`)
- `requests` (puedes instalarlo ejecutando `pip install requests`)
- `pip` (herramienta de gestión de paquetes de Python)

## Instalación y Ejecución

1. Clona este repositorio:

   ```bash
   git clone https://github.com/markbus-ai/gestor-de-paquetes
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd gestor-de-paquetes
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```bash
   pythonw gestor.pyw
   ```

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor crea un pull request explicando los cambios propuestos.

## Licencia

Este proyecto está bajo la licencia MIT License.
