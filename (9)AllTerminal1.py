import networkx as nx
import numpy as np
import pandas as pd

def evaluar_conectividad(sbs_vector, grafo_original):
    resultados = []
    
    for n_upla in sbs_vector:
        subgrafo = nx.Graph()
        subgrafo.add_nodes_from(grafo_original.nodes)

        for (edge, is_active) in zip(grafo_original.edges, n_upla):
            if is_active == 1:
                subgrafo.add_edge(*edge)
        
        if nx.is_connected(subgrafo):
            resultados.append(1)
        else:
            resultados.append(0)
    
    return resultados

G = nx.Graph()
nodos = ["A", "B", "C", "D", "E", "F", "G", "H"]
conexiones = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "E"),
    ("C", "F"), ("D", "E"), ("D", "G"), ("E", "H"), ("F", "G"),
    ("F", "H"), ("G", "H"), ("A", "F"), ("B", "G"), ("C", "H")
]
G.add_nodes_from(nodos)
G.add_edges_from(conexiones)

num_edges = len(G.edges)
k = 256  
sbs_configurations = np.random.choice([0, 1], size=(k, num_edges), p=[1/2, 1/2])
sbs_vector = sbs_configurations.tolist()

resultados = evaluar_conectividad(sbs_vector, G)

data = {
    "n_upla": sbs_vector,
    "resultado": resultados
}
df = pd.DataFrame(data)
df.to_csv("sbs9.csv", index=False)