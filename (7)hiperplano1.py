'''
Descripcio: SBS construido a partir de un hiperplano separador aleatorio.
Cantidad de componentes: 10
Probabilidad de operacion de cada componente: 1/2
Tamaño del data set: 256
'''

import numpy as np
import pandas as pd

num_components = 10  
num_configurations = 256  

coefficients = np.random.rand(num_components)  
alpha = sum(x for x in coefficients) / 2 
configurations = np.random.choice([0, 1], size=(num_configurations, num_components), p=[1/2, 1/2])
config_vector = configurations.tolist()

results = []
for upla in config_vector:
    suma = sum(c * u for c, u in zip(coefficients, upla))
    results.append(1 if suma > alpha else 0)

data = {
    "n_upla": config_vector,
    "resultado": results
}
df = pd.DataFrame(data)
df.to_csv("sbs7.csv", index=False)

#print("Coeficientes:", coefficients)
#print("Alfa:", alpha)