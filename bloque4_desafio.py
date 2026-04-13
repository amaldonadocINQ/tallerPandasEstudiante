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

# 2. Crear la columna 'estado' usando la función lambda
df['estado'] = df['temperatura'].apply(lambda t: 'critico' if t > 90 else 'normal')
tipoMedicion = df['estado'].value_counts()

print(df)
print(f"\n{tipoMedicion}")

promedio_efi = df.groupby('reactor')['eficiencia'].mean()
plt.bar(promedio_efi.index, promedio_efi.values, color=['green', 'blue', 'orange'])

plt.title('Eficiencia Promedio por Reactor')
plt.xlabel('Reactor')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
