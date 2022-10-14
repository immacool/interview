from code.data_structures.trees.tree import Tree

def visualize_graph(graph: Tree, node_labels=None, node_colors=None, edge_colors=None, edge_labels=None, node_size=300, edge_size=1, figsize=(10, 10)):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_nodes_from(graph.get_nodes())
    edges = []
    for node in graph.get_nodes():
        for child in graph.get_children(node):
            edges.append((node, child))
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, k=0.5, iterations=50)

    if node_labels is None:
        node_labels = {node: node for node in graph.get_nodes()}

    if node_colors is None:
        node_colors = {node: 'c' for node in graph.get_nodes()}

    if edge_colors is None:
        edge_colors = {edge: 'black' for edge in edges}

    if edge_labels is None:
        edge_labels = {edge: '' for edge in edges}

    nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()), node_size=node_size)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=list(edge_colors.values()), width=edge_size)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    

if __name__ == '__main__':
    tree = Tree()
    tree.fill_tree(10, 15, 0.6)
    visualize_graph(tree)
    