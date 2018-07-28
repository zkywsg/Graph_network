import networkx as nx
import matplotlib.pyplot as plt
import numpy

G = nx.read_gml('test1.gml')
# k_components = nx.k_components(G)
# print(k_components)

a = list(nx.articulation_points(G))
# print(a)
G.add_edge(3,7)
k_components = nx.k_components(G)
# print(k_components)
a = list(nx.articulation_points(G))
# print(a)
A=numpy.matrix([[0,1,1,0,0],
                [1,0,1,0,0],
                [1,1,0,1,1],
                [0,0,1,0,0],
                [0,0,1,0,0]])
H=nx.from_numpy_matrix(A)
k_components = nx.k_components(H)
print(k_components)
bicomponents = list(nx.biconnected_component_subgraphs(H))
print(bicomponents[0].nodes())


plt.show()
