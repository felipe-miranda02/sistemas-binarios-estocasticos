'''
Descripcio: Modela una simplificacion de la red de trenes de Paris, con un grafo de 2 terminales y caida en aristas (la fuente es "Saint-Lazare" y la terminal es "Place d'Italie").
Cantidad de componentes: 19
Probabilidad de operacion de cada componente: 4/5
Tamaño del data set: 1024
'''

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def evaluar_sbs(sbs_vector, grafo_original, nodo_inicio="Saint-Lazare", nodo_destino="Place d'Italie"):
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

# Principales estaciones del Metro de París
estaciones = [
    "Gare du Nord", "Châtelet", "Gare de Lyon", "Montparnasse", "Saint-Lazare",
    "Charles de Gaulle - Étoile", "Nation", "Bastille", "Opéra", "République",
    "Concorde", "Invalides", "La Défense", "Bercy", "Les Halles",
    "Place d'Italie", "Porte d'Orléans"
]
G.add_nodes_from(estaciones)

# Conexiones entre las estaciones
conexiones = [
    ("Gare du Nord", "Châtelet"),
    ("Gare du Nord", "République"),
    ("Châtelet", "Opéra"),
    ("Châtelet", "Les Halles"),
    ("Châtelet", "Gare de Lyon"),
    ("Gare de Lyon", "Bastille"),
    ("Gare de Lyon", "Nation"),
    ("Montparnasse", "Invalides"),
    ("Montparnasse", "Saint-Lazare"),
    ("Saint-Lazare", "Opéra"),
    ("Saint-Lazare", "Charles de Gaulle - Étoile"),
    ("Charles de Gaulle - Étoile", "La Défense"),
    ("Invalides", "Concorde"),
    ("Concorde", "Opéra"),
    ("Les Halles", "République"),
    ("République", "Place d'Italie"),
    ("Place d'Italie", "Porte d'Orléans"),
    ("Bercy", "Nation"),
    ("Bastille", "Place d'Italie"),
]
G.add_edges_from(conexiones)

# Dibujar el grafo
plt.figure(figsize=(12, 10))
nx.draw_networkx(
    G, with_labels=True, node_size=600, node_color="lightblue",
    font_size=10, font_weight="bold", edge_color="gray"
)
plt.title("Red Simplificada del Metro de París")
plt.show()

num_edges = 19
k = 1024  

sbs_configurations = np.random.choice([0, 1], size=(k, num_edges), p=[1/5, 4/5])
sbs_vector = sbs_configurations.tolist()

resultados = evaluar_sbs(sbs_vector, G)

data = {
    "n_upla": sbs_vector,
    "resultado": resultados
}
df = pd.DataFrame(data)
df.to_csv("sbs5.csv", index=False)