import random

# Граф - это набор вершин и ребер, соединяющих эти вершины между собой
# Вершина - это узел графа, ребро - это связь между двумя вершинами.

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node):
        ''' Добавляет ребро между двумя вершинами '''
        self.edges.append(node)

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return f"Node({self.value})"
    
    def __eq__(self, other):
        return self.value == other.value
    
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        
    def add_node(self, value):
        ''' Добавляет вершину в граф '''
        self.nodes.append(Node(value))
        
    def add_edge(self, node1, node2):
        ''' Добавляет ребро между двумя вершинами '''
        node1.add_edge(node2)
        node2.add_edge(node1)
        self.edges.append((node1, node2))
        
    def get_neighbours(self, node):
        ''' Возвращает список смежных вершин для вершины node '''
        return node.edges
    
    def get_by_value(self, value):
        ''' Возвращает вершину с заданным значением '''
        for node in self.nodes:
            if node.value == value:
                return node
        
    def fill_graph(self, n, m):
        ''' Заполняет граф n вершинами и m ребрами '''
        for i in range(n):
            self.add_node(i)
        for i in range(m):
            node1 = random.choice(self.nodes)
            node2 = random.choice(self.nodes)
            self.add_edge(node1, node2)
        
    def __repr__(self):
        return f"Graph({self.nodes}, {self.edges})"
    
    def __str__(self):
        return f"Graph({self.nodes}, {self.edges})"
 
    # Список смежности - это структура данных, которая представляет собой массив списков.
    # Каждый список представляет собой список смежных вершин для соответствующей вершины.
    # Сложность: O(V + E), где V - количество вершин, E - количество ребер
    def adjacency_list(self):
        adj_list = []
        for node in self.nodes:
            adj_list.append([node.value] + [edge.value for edge in node.edges])
        return adj_list # adj_list[0] = node, adj_list[1:] = edges

if __name__ == "__main__":
    # Создание графа
    graph = Graph()
    
    # Заполнение графа
    graph.fill_graph(5, 10)
    
    # Вывод графа
    print(graph)
    
    # Вывод списка смежности
    print(graph.adjacency_list())