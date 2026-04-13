import pandas as pd

# Diccionario de Python: clave = nombre de columna, lista = datos
datos = {
    'reactor': ['R1', 'R1', 'R1', 'R2', 'R2', 'R2', 'R3', 'R3'],
    'turno': ['manana', 'tarde', 'noche', 'manana', 'tarde', 'noche', 'manana', 'tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}

# pd.DataFrame() convierte el diccionario en tabla
df = pd.DataFrame(datos)

#Una sola columna (Devuelve una Serie - como una lista con etiquetas)
print(df['temperatura'])

#Dos columnas a la vez (devuelve un DataFrame)
print("\n")
print(df[['reactor', 'eficiencia']])

#Ver solo las primeras 3 filas:
print("\n")
print(df.head(3))

#Imprime solo la tolumna 'turno'
print("\n")
print(df['turno'])

#Imprime las columas 'reactor' e 'incidentes' juntas:
print("\n")
print(df[['reactor', 'incidentes']])

# Quiero las filas donde temperatura supera 88.
# df['temperatura'] > 88 produce True/False para cada fila.
# df[ ... ] conserva solo las filas donde el resultado es True.
calientes = df[ df['temperatura'] > 88 ]

print("\n")
print('Mediciones con temperatura mayor a 88:')
print(calientes)

#Filtro 1: filas donde el turno es exactamente 'manana'
print("\n")
manana = df[df['turno'] == "manana"]
print("Turno manana:")
print (manana)

#Filtro 2: filas donde no hubo ningun incidente (incidentes == 0)
print("\n")
sinIncidentes = df[df['incidentes'] == 0]
print("Sin incidentes:")
print (sinIncidentes)

# Temperatura promedio de cada reactor:
promedio_temp = df.groupby('reactor')['temperatura'].mean()

print('Temperatura promedio por reactor:')
print(promedio_temp)

#Eficiencia PROMEDIO por turno (manana, tarden noche):
#groupby 'turno;, columna 'eficiencia, funcion .mean()
efTurno = df.groupby('turno')['eficiencia'].mean()
print(efTurno)

#Total de incidentes por reactor:
# groupby 'reactor', columna 'incidentes', funcion .sum()
incReactor = df.groupby('reactor')['incidentes'].sum()
print (incReactor)