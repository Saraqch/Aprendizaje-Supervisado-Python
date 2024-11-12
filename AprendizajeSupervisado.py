# Importar bibliotecas necesarias
import matplotlib
matplotlib.use('Agg')  # Cambia a un backend no interactivo
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Paso 1: Cargar y preparar el conjunto de datos
df = pd.read_csv('datos_errores.csv')  # Cargar los datos desde el archivo CSV

# Paso 2: Preprocesamiento de datos
# Características adicionales para mejorar la precisión del modelo
df['length'] = df['code'].apply(len)  # Longitud del código
df['operators_count'] = df['code'].apply(lambda x: x.count('=') + x.count('>') + x.count('<'))  # Cantidad de operadores
df['keywords_count'] = df['code'].apply(lambda x: sum(x.count(word) for word in ['int', 'String', 'public', 'class', 'System']))  # Contar palabras clave
df['variables_count'] = df['code'].apply(lambda x: x.count('int') + x.count('String'))  # Contar declaraciones de variables

# Separar características (X) y etiquetas (y)
X = df[['length', 'operators_count', 'keywords_count', 'variables_count']]
y = df['error_type']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Entrenar el modelo Random Forest
model = RandomForestClassifier(n_estimators=300, max_depth=7, random_state=42)
model.fit(X_train, y_train)

# Paso 4: Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Paso 5: Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Precisión:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Paso 6: Mostrar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Error de Sintaxis', 'Error de Declaración'],
            yticklabels=['Error de Sintaxis', 'Error de Declaración'])
plt.xlabel('Predicción')
plt.ylabel('Actual')
plt.title('Matriz de Confusión')

# Guardar la figura como un archivo (por ejemplo, 'matriz_confusion.png')
plt.savefig('matriz_confusion.png')  # Puedes cambiar el nombre y formato aquí

# ---------------------------------------------
# Nuevas funciones para permitir ingreso desde consola
def preprocesar_input(code):
    """
    Función para preprocesar el código ingresado.
    Calcula la longitud del código, la cantidad de operadores y palabras clave.
    """
    length = len(code)
    operators_count = code.count('=') + code.count('>') + code.count('<')
    keywords_count = sum(code.count(word) for word in ['int', 'String', 'public', 'class', 'System'])
    variables_count = code.count('int') + code.count('String')
    
    return np.array([[length, operators_count, keywords_count, variables_count]])

def predecir_error(code):
    """
    Función para predecir el tipo de error (Sintaxis o Declaración) de un fragmento de código.
    """
    # Preprocesar el código
    input_data = preprocesar_input(code)
    
    # Realizar la predicción
    prediction = model.predict(input_data)
    
    # Imprimir el resultado
    if prediction == 0:
        print(f"El código ingresado tiene un Error de Sintaxis.")
    else:
        print(f"El código ingresado tiene un Error de Declaración.")

# ---------------------------------------------
# Interfaz de consola para ingresar código y hacer predicciones
while True:
    # Solicitar al usuario que ingrese un fragmento de código
    code_input = input("Introduce un fragmento de código (o 'salir' para terminar): ")
    
    if code_input.lower() == 'salir':
        print("Terminando el programa.")
        break
    else:
        predecir_error(code_input)
