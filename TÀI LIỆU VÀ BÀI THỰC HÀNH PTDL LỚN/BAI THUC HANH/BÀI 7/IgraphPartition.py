import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
from networkx.algorithms import community
import community as community_louvain
# Bước 1: Đọc dữ liệu Karate từ networkx
karate_graph = nx.karate_club_graph()

# Bước 2: Hiển thị đồ thị
plt.figure(figsize=(8, 6))
nx.draw(karate_graph, with_labels=True, node_color='lightblue', node_size=400, font_size=10)
plt.title("Đồ thị Karate")
plt.show()

# Bước 3: Phân cụm dữ liệu bằng edge betweenness theo thuật toán Girvan Newman
def girvan_newman(graph):
    G = ig.Graph.Adjacency(nx.to_numpy_array(graph).tolist())
    dendrogram = G.community_edge_betweenness()
    clusters = dendrogram.as_clustering()
    return clusters

clusters_girvan_newman = girvan_newman(karate_graph)
print("Phân cụm bằng edge betweennes:",clusters_girvan_newman)
# Bước 4: In đồ thị đã được phân cụm
plt.figure(figsize=(8, 6))
nx.draw(karate_graph, with_labels=True, node_color='lightblue', node_size=400, font_size=10)
plt.title("Đồ thị đã phân cụm bằng Girvan-Newman")
plt.show()

# Bước 5: Phân cụm dữ liệu bằng thuật toán tham lam greedy của Newman, maximize modularity
greedy_communities = list(community.greedy_modularity_communities(karate_graph))

# Bước 6: In kết quả phân cụm
print("Kết quả phân cụm bằng thuật toán tham lam greedy:")
for i, community_nodes in enumerate(greedy_communities):
    print(f"Cụm {i + 1}: {community_nodes}")

# Bước 7: Tạo biểu đồ mới dựa trên kết quả phân cụm
clustered_graph = nx.Graph()
for i, community_nodes in enumerate(greedy_communities):
    for node in community_nodes:
        clustered_graph.add_node(node, cluster=i)

for edge in karate_graph.edges():
    cluster1 = None
    cluster2 = None
    for i, community_nodes in enumerate(greedy_communities):
        if edge[0] in community_nodes:
            cluster1 = i
        if edge[1] in community_nodes:
            cluster2 = i
        if cluster1 is not None and cluster2 is not None:
            break
    if cluster1 != cluster2:
        clustered_graph.add_edge(edge[0], edge[1])

# Bước 8: Hiển thị đồ thị đã phân cụm
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(clustered_graph)
node_colors = [clustered_graph.nodes[node]['cluster'] for node in clustered_graph.nodes()]
nx.draw(clustered_graph, pos, node_size=50, cmap=plt.get_cmap('jet'), node_color=node_colors)
plt.title("Đồ thị đã phân cụm bằng Greedy Modularity")
plt.show()

"""
Flow của đoạn code trên:
B1:Đọc dữ liệu Karate từ networkx: Bước này sử dụng thư viện NetworkX để tạo một đồ thị Karate từ dữ liệu có sẵn trong thư viện.

B2:Hiển thị đồ thị: Sử dụng Matplotlib để vẽ và hiển thị đồ thị Karate lên màn hình.

B3:Phân cụm dữ liệu bằng edge betweenness theo thuật toán Girvan Newman: Bước này sử dụng thư viện iGraph để phân cụm đồ thị bằng thuật toán Girvan Newman dựa trên edge betweenness. Đầu tiên, đồ thị NetworkX được chuyển đổi thành định dạng phù hợp với iGraph, sau đó thuật toán Girvan Newman được áp dụng để tìm các cụm.

B4:In đồ thị đã được phân cụm: Sử dụng Matplotlib để vẽ và hiển thị đồ thị đã phân cụm bằng thuật toán Girvan Newman lên màn hình.

B5:Phân cụm dữ liệu bằng thuật toán tham lam greedy của Newman, maximize modularity: Bước này sử dụng thư viện NetworkX và thư viện community để phân cụm đồ thị bằng thuật toán tham lam greedy của Newman dựa trên việc tối đa hóa modularity.

B6:In kết quả phân cụm: Hiển thị kết quả phân cụm bằng thuật toán tham lam greedy trên màn hình.

B7:Tạo biểu đồ mới dựa trên kết quả phân cụm: Tạo một đồ thị mới dựa trên kết quả phân cụm của thuật toán tham lam greedy. Mỗi nút trong đồ thị mới thuộc vào một cụm cụ thể.

B8:Hiển thị đồ thị đã phân cụm: Sử dụng Matplotlib để vẽ và hiển thị đồ thị đã phân cụm bằng thuật toán tham lam greedy lên màn hình.
    
"""