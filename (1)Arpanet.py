'''
Descripcio: Modela la red ARPANET en 1973, con un grafo de 2 terminales y caida en aristas (la fuente es "MIT" y la terminal es "NASA").
Cantidad de componentes: 27
Probabilidad de operacion de cada componente: 4/5
Tamaño del data set: 16384
'''

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def evaluar_sbs(sbs_vector, grafo_original, nodo_inicio="MIT", nodo_destino="NASA"):
    resultados = []
    
    for n_upla in sbs_vector:

        subgrafo = nx.Graph()
        subgrafo.add_nodes_from(grafo_original.nodes)

        for (edge, is_active) in zip(grafo_original.edges, n_upla):
            if is_active == 1:
                subgrafo.add_edge(*edge)
        
        if nx.has_path(subgrafo, nodo_inicio, nodo_destino):
            resultados.append(1)
        else:
            resultados.append(0)
    
    return resultados

G = nx.Graph()

# principales nodos de ARPANET en 1973
nodos = [
    "UCLA", "Stanford", "Utah", "MIT", "Harvard", "BBN", 
    "RAND", "Lincoln Labs", "SDC", "CMU", "UCSB", 
    "ILLINOIS", "Case Western", "USC", "AMES", "NASA",
    "Arizona", "Purdue", "Michigan", "CARN", "RAND", 
    "Berkeley", "NBS", "NBS West", "Office Washington",
]

G.add_nodes_from(nodos)

# aristas según la topología conocida de ARPANET en 1973
conexiones = [
    ("UCLA", "Stanford"), ("UCLA", "RAND"), ("UCLA", "SDC"),
    ("Stanford", "Utah"), ("Stanford", "AMES"), ("AMES", "NASA"),
    ("UCSB", "UCLA"), ("RAND", "BBN"), ("BBN", "MIT"),
    ("MIT", "Harvard"), ("MIT", "Lincoln Labs"), ("BBN", "Case Western"),
    ("Case Western", "ILLINOIS"), ("ILLINOIS", "CMU"), ("ILLINOIS", "Purdue"),
    ("MIT", "CARN"), ("CARN", "CMU"), ("CARN", "USC"),
    ("NASA", "NBS"), ("Lincoln Labs", "Office Washington"), 
    ("Office Washington", "NBS West"), ("NBS", "Michigan"),
    ("Berkeley", "Utah"), ("Berkeley", "Arizona"),
    ("Purdue", "Michigan"), ("SDC", "RAND"), ("Arizona", "Berkeley"),
]

G.add_edges_from(conexiones)

# Dibujar el grafo
plt.figure(figsize=(12, 10))
nx.draw_networkx(
    G, with_labels=True, node_size=600, node_color="lightcoral",
    font_size=8, font_weight="bold", edge_color="gray"
)
plt.title("Red ARPANET (Versión Extendida, 1973)")
plt.show()

num_edges = 28
k =  16384 

sbs_configurations = np.random.choice([0, 1], size=(k, num_edges), p=[1/5, 4/5])
sbs_vector = sbs_configurations.tolist()

resultados = evaluar_sbs(sbs_vector, G)
 
data = {
    "n_upla": sbs_vector,
    "resultado": resultados
}
df = pd.DataFrame(data)

df.to_csv("sbs1.csv", index=False)