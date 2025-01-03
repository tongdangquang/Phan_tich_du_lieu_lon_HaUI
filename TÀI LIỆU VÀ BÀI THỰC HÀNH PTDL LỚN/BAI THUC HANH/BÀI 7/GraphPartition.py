from community import community_louvain, modularity
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()
partition = community_louvain.best_partition(G)
modu = modularity(graph=G, partition=partition)

pos = nx.spring_layout(G)
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()