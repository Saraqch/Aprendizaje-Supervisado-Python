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
`python -m venv venv`.


### Este comando crea un entorno virtual en una carpeta llamada venv dentro de tu proyecto.

4. Activar el Entorno Virtual
En Windows, usa el siguiente comando:

bash
Copiar código
venv\Scripts\activate
Verás que la terminal muestra (venv) al inicio de la línea, lo que indica que el entorno virtual está activado.

5. Instalar las Dependencias
Con el entorno virtual activado, instala las bibliotecas necesarias ejecutando el siguiente comando:

bash
Copiar código
pip install scikit-learn pandas seaborn matplotlib
Estas bibliotecas son esenciales para el procesamiento de datos, el entrenamiento del modelo y la visualización de resultados.

Escribir y Configurar el Código
1. Crear el Archivo de Código
Dentro de tu carpeta de proyecto, crea un archivo llamado AprendizajeSupervisado.py.

2. Escribir el Código
Abre AprendizajeSupervisado.py en VS Code y copia el código que se encuentra en este repositorio con el nombre AprendizajeSupervisado.py.
3. Guardar el Archivo
Una vez que hayas copiado el código, guarda el archivo presionando Ctrl + S o Cmd + S en tu teclado.
4. Crear el Archivo de Datos
Crea un archivo en la misma carpeta donde está tu programa AprendizajeSupervisado.py, con el nombre datos_errores.csv.
Copia el contenido del archivo datos_errores.csv de este repositorio y pégalo en el archivo que acabas de crear, luego guarda los cambios con Ctrl + S.
Ejecutar el Proyecto
1. Ejecutar el Código en la Terminal de VS Code
Asegúrate de que el entorno virtual esté activado (deberías ver (venv) en la terminal). Luego, ejecuta el script con el siguiente comando:

bash
Copiar código
python AprendizajeSupervisado.py
2. Verificar los Resultados
En la terminal de VS Code, deberías ver las métricas de evaluación impresas:

Precisión (accuracy)
Precision
Recall
F1 Score
3. Visualizar la Matriz de Confusión
La matriz de confusión se mostrará en una ventana de Matplotlib, la cual visualiza cómo el modelo clasifica los errores de sintaxis y declaración. La matriz te permitirá verificar si el modelo está funcionando correctamente.


