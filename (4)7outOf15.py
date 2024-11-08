'''
Descripcio: SBS 7 out of 15, donde se evalua 1 si la cantidad de componentes activos es mayor o igual a 7, 0 en caso contrario.
Cantidad de componentes: 15
Probabilidad de operacion de cada componente: 1/2
Tamaño del data set: 1024
'''

import numpy as np
import pandas as pd

n = 15  
k = 7   
num_configurations = 1024  

configurations = np.random.choice([0, 1], size=(num_configurations, n), p=[1/2, 1/2])
config_vector = configurations.tolist()

results = [1 if sum(upla) >= k else 0 for upla in config_vector]

data = {
    "n_upla": config_vector,
    "resultado": results
}
df = pd.DataFrame(data)
df.to_csv("sbs4.csv", index=False)