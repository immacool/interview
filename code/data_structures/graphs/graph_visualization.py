from code.data_structures.graphs.graph import Graph

def visualize_graph(graph: Graph, node_labels=None, node_colors=None, edge_colors=None, edge_labels=None, node_size=1000, edge_size=1, figsize=(10, 10)):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for node in graph.nodes:
        G.add_node(node.value)
    for edge in graph.edges:
        G.add_edge(edge[0].value, edge[1].value)

    pos = nx.spring_layout(G, k=0.5, iterations=50)

    if node_labels is None:
        node_labels = {node.value: node.value for node in graph.nodes}
    if node_colors is None:
        node_colors = ["red" for _ in graph.nodes]
    if edge_colors is None:
        edge_colors = ["black" for _ in graph.edges]
    if edge_labels is None:
        edge_labels = {(edge[0].value, edge[1].value): "" for edge in graph.edges}
        
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_colors)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edges(G, pos, width=edge_size, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.axis("off")
    plt.show()
    

if __name__ == '__main__':
    graph = Graph()
    graph.fill_graph(10, 15)
    visualize_graph(graph)