import pandas as pd
import matplotlib.pyplot as plt

# Dataframe Bloque 1
datos = {
    'reactor': ['R1', 'R1', 'R1', 'R2', 'R2', 'R2', 'R3', 'R3'],
    'turno': ['manana', 'tarde', 'noche', 'manana', 'tarde', 'noche', 'manana', 'tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos)

# Paso 1: calcular los datos a graficar con groupby
promedio_temp = df.groupby('reactor')['temperatura'].mean()

# Paso 2: crear el lienzo (7 pulgadas ancho, 4 alto)
plt.figure(figsize=(7, 4))

# Paso 3: dibujar barras
# .index son los nombres del eje X: R1, R2, R3
# .values son las alturas de las barras: los promedios
plt.bar(promedio_temp.index, promedio_temp.values, color='steelblue')

# Paso 4: etiquetas
plt.title('Temperatura promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Temperatura (C)')
plt.tight_layout()
plt.show()

#Scatter plot
plt.figure(figsize=(7, 4))

plt.scatter(df['temperatura'], df['eficiencia'], color='coral', s=80)

plt.title('Temperatura vs Eficiencia')
plt.xlabel('Temperatura (C)')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))

# ESCRIBE TU CODIGO - usa plt.plot()
# Usamos df.index para el eje X y df['eficiencia'] para el eje Y
plt.plot(df.index, df['eficiencia'], marker='o', linewidth=2)

plt.title('Eficiencia por medicion')
plt.xlabel('Numero de medicion')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()