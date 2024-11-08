import numpy as np
import pandas as pd

n = 10  
k = 6   
num_configurations = 512  

configurations = np.random.choice([0, 1], size=(num_configurations, n), p=[1/2, 1/2])
config_vector = configurations.tolist()

results = [1 if sum(upla) >= k else 0 for upla in config_vector]

data = {
    "n_upla": config_vector,
    "resultado": results
}
df = pd.DataFrame(data)
df.to_csv("sbs3.csv", index=False)