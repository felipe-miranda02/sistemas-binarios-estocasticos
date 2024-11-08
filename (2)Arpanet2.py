import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def evaluar_sbs(sbs_vector, grafo_original, nodo_inicio="Stanford", nodo_destino="CARN"):
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

num_edges = 28
k =  16384 

sbs_configurations = np.random.choice([0, 1], size=(k, num_edges), p=[1/3, 2/3])
sbs_vector = sbs_configurations.tolist()

resultados = evaluar_sbs(sbs_vector, G)
 
data = {
    "n_upla": sbs_vector,
    "resultado": resultados
}
df = pd.DataFrame(data)

df.to_csv("sbs2.csv", index=False)