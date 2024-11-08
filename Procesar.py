import pandas as pd
import ast

file_path = "(7)hiperplano1.csv"

df = pd.read_csv(file_path)

# Convertir las n-uplas de strings a listas de enteros
df['n_upla'] = df['n_upla'].apply(ast.literal_eval)

print(df.head())
print(df['n_upla'].head())
print(df['n_upla'].iloc[0])

segunda_n_upla = df['n_upla'].iloc[1]  # Obtener la segunda n-upla
segunda_componente = segunda_n_upla[1]  # Obtener la segunda componente de esa n-upla

print("Segunda n-upla:", segunda_n_upla)
print("Segunda componente de la segunda n-upla:", segunda_componente)

'''
# Acceder a las 12-uplas y resultados individualmente
for index, row in df.iterrows():
    n_upla = row['n_upla']
    resultado = row['resultado']
    print(f"n_upla: {n_upla}, Resultado: {resultado}")
'''