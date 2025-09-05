

import networkx as nx
import matplotlib.pyplot as plt

# Carrega o grafo
G = nx.karate_club_graph()

# Visualiza o grafo original
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True)
plt.title('Grafo Original')
plt.show()

def edge_to_remove(graph):
	# Calcula a centralidade das arestas
	G_dict = nx.edge_betweenness_centrality(graph)
	edge = ()
	# Seleciona a aresta com maior centralidade
	for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse=True):
		edge = key
		break
	return edge

def girvan_newman(graph):
	# Enquanto o grafo for conexo, remove a aresta de maior centralidade
	sg_count = nx.number_connected_components(graph)
	while sg_count == 1:
		edge = edge_to_remove(graph)
		graph.remove_edge(edge[0], edge[1])
		sg_count = nx.number_connected_components(graph)
	return nx.connected_components(graph)

# Executa o algoritmo Girvan-Newman
G_mod = G.copy()
communities = girvan_newman(G_mod)

# Agrupa os nós das comunidades
node_groups = []
for c in communities:
	node_groups.append(list(c))

# Plota as comunidades no grafo modificado
color_map = []
for node in G_mod:
	if node in node_groups[0]:
		color_map.append('blue')
	else:
		color_map.append('green')

plt.figure(figsize=(8,6))
nx.draw(G_mod, node_color=color_map, with_labels=True)
plt.title('Comunidades detectadas (Girvan-Newman)')
plt.show()