import random
from typing import List
from code.data_structures.graphs.graph import Graph, Node

# Поиск в ширину - это алгоритм поиска, который использует принцип "разделяй и властвуй".
# Основная идея - создать очередь, в которой хранятся все вершины, которые нужно посетить.
# После этого мы извлекаем из очереди первый элемент и добавляем его соседей в очередь.
# Если мы ищем элемент, который находится в глубине дерева, то мы сначала посетим все вершины,
# которые находятся на одном уровне с корнем, а затем перейдем к вершинам, которые находятся
# на уровне ниже и так далее, пока не найдем искомый элемент.
# Поиск в ширину можно использовать для поиска кратчайшего пути в графе.
# Сложонсть: O(V + E), где V - количество вершин, а E - количество ребер.

def breadth_first_search(graph: Graph, start: Node, end: Node) -> List[Node]:
    """Поиск в ширину"""
    # Создаем очередь, в которую будем добавлять вершины, которые нужно посетить.
    queue = []
    # Добавляем в очередь начальную вершину.
    queue.append(start)
    # Создаем словарь, в котором будем хранить вершины и их родителей.
    # Это нужно для того, чтобы восстановить путь.
    parents = {}
    # Добавляем в словарь начальную вершину и ее родителя.
    parents[start.value] = None
    # Пока в очереди есть элементы.
    while len(queue) > 0:
        # Извлекаем первый элемент из очереди.
        current = queue.pop(0)
        # Если текущая вершина - искомая, то возвращаем ее.
        if current == end:
            return parents
        # Добавляем в очередь все соседние вершины.
        for neighbor in graph.get_neighbours(current):
            # Если вершина еще не посещена.
            if neighbor.value not in parents:
                # Добавляем ее в очередь.
                queue.append(neighbor)
                # Добавляем в словарь вершину и ее родителя.
                parents[neighbor.value] = current
    # Если искомый элемент не найден, возвращаем None.
    return None
    
if __name__ == "__main__":
    import networkx as nx
    import matplotlib.pyplot as plt
    # Создаем граф.
    graph = Graph()
    graph.fill_graph(10, 15) 

    # Применяем алгоритм поиска в ширину.
    start = random.choice(graph.nodes)
    end = random.choice([node for node in graph.nodes if node != start])
    path = breadth_first_search(graph, start, end)
    
    # Визуализируем граф и путь на нем.
    # Реконструием путь если он найден.
    if path is not None:
        path_list = []
        current = end
        while current is not None:
            path_list.append(current)
            current = path[current.value]
        path_list.reverse()
    else:
        path_list = []
    
    # Создаем граф networkx.
    G = nx.Graph()
    for node in graph.nodes:
        G.add_node(node.value)
    for edge in graph.edges:
        G.add_edge(edge[0].value, edge[1].value)
    
    # Визуализируем граф и путь на нем.
    # Начало и конец помечаем красным и путь зеленым. Обычные вершины - бесцветные.
    edgelist = [(edge[0].value, edge[1].value) for edge in graph.edges]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=[node.value for node in graph.nodes], node_color='c')
    nx.draw_networkx_nodes(G, pos, nodelist=[node.value for node in path_list], node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=[start.value], node_color='r')
    nx.draw_networkx_nodes(G, pos, nodelist=[end.value], node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=edgelist, width=1)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    plt.axis('off')
    plt.show()
    
    