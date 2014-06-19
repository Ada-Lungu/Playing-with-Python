
import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
nx.draw_circular(G)

G.add_nodes_from([2,8,14])
G.add_edges_from([(1,2),(1,3),(4,5)])

nx.draw(G)