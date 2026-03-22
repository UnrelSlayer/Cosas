import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# 1. CARGAR DATOS
# Usamos el dataset 'Iris': medidas de pétalos y sépalos de 3 tipos de flores
iris = datasets.load_iris()
X = iris.data  # Las características (números: ancho, alto, etc.)
y = iris.target # La respuesta correcta (0, 1 o 2 según el tipo de flor)

print(f"Datos cargados: {X.shape[0]} flores con {X.shape[1]} características cada una.")

# 2. DIVIDIR DATOS (Split)
# Separamos: 80% para estudiar (train) y 20% para el examen final (test)
# random_state=42 es para que siempre salga la misma división (es un número 'semilla')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. ENTRENAR EL MODELO
# Usamos un algoritmo simple: K-Nearest Neighbors (K-Vecinos más cercanos)
# Busca las 3 flores más parecidas a la nueva para decidir qué es.
#modelo = KNeighborsClassifier(n_neighbors=6)
# Activamos el nuevo: Árbol de Decisión
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train) # Aquí ocurre el aprendizaje

# 4. PREDECIR Y EVALUAR
predicciones = modelo.predict(X_test)

# Comparamos lo que dijo el modelo vs. la realidad
precision = accuracy_score(y_test, predicciones)

print("------------------------------------------------")
print(f"Precisión del modelo: {precision * 100:.2f}%")
print("------------------------------------------------")

# Probemos con una flor inventada
flor_misteriosa = np.array([[5.1, 3.5, 1.4, 0.2]])
prediccion_nueva = modelo.predict(flor_misteriosa)
nombre_flor = iris.target_names[prediccion_nueva][0]

print(f"La flor misteriosa es una: {nombre_flor}")

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# 1. Crear el gráfico de la matriz
# Le pasamos el modelo entrenado, los datos de prueba y los nombres reales de las flores
disp = ConfusionMatrixDisplay.from_estimator(
    modelo, 
    X_test, 
    y_test, 
    display_labels=iris.target_names,
    cmap=plt.cm.Blues # Esto es solo para que se vea azul y bonito
)

# 2. Ponerle título y mostrarlo
disp.ax_.set_title("Matriz de Confusión")
print("Generando gráfico...")
plt.show() 

#esto de abajo tiene que ver con el decision tree

# Configurar el tamaño del dibujo
plt.figure(figsize=(10,8))

# Dibujar el árbol
# Dibujar el árbol
plot_tree(modelo, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Así tomó las decisiones tu IA")
plt.savefig('visualizacion_arbol.png') # Guardamos la imagen
print("Gráfico del árbol guardado como 'visualizacion_arbol.png'")
plt.show()