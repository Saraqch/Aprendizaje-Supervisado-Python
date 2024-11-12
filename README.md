# Clasificador de Errores de Sintaxis en Código Python

Este proyecto está diseñado para clasificar errores de sintaxis y errores de declaración en fragmentos de código. Utiliza un modelo de Machine Learning (Random Forest) entrenado con características extraídas de fragmentos de código.

## Requisitos Previos

### 1. Instalar Python
Si aún no tienes Python instalado, sigue estos pasos:

- Descarga Python desde [python.org](https://www.python.org/).
- Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"** para poder ejecutarlo desde la terminal.

### 2. Instalar Visual Studio Code
Si no tienes Visual Studio Code instalado, puedes obtenerlo desde [code.visualstudio.com](https://code.visualstudio.com/).

- Una vez instalado, asegúrate de instalar la extensión **"Python"** de Microsoft para tener soporte completo de Python.

---

## Crear el Proyecto y Configurar el Entorno Virtual

### 1. Crear una Carpeta para el Proyecto
- Abre Visual Studio Code.
- Crea o selecciona una carpeta para tu proyecto, por ejemplo, `ClasificadorErrores`.

### 2. Abrir la Terminal en VS Code
- En VS Code, selecciona **Terminal > New Terminal** para abrir la terminal integrada.

### 3. Crear un Entorno Virtual
Es recomendable usar un entorno virtual para manejar las dependencias del proyecto. Para crearlo, ejecuta el siguiente comando en la terminal:

```bash
python -m venv venv

