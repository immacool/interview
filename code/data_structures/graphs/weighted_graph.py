
# Граф с весами - это граф, в котором каждое ребро имеет вес. 
# Вес ребра - это число, которое связывает ребро с его весом. 
# Вес графа - это сумма весов всех ребер в графе.

import random


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node, weight):
        ''' Добавляет ребро между двумя вершинами '''
        e = Edge(self, node, weight)
        self.edges.append(e)
        
    def remove_edge(self, node):
        ''' Удаляет ребро между двумя вершинами '''
        for edge in self.edges:
            if edge.node1 == node or edge.node2 == node:
                self.edges.remove(edge)
                break

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return f"Node({self.value})"
    
    def __eq__(self, other):
        return self.value == other.value
    

class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        
    def __repr__(self):
        return f"Edge({self.node1}, {self.node2}, {self.weight})"
    
    def __str__(self):
        return f"Edge({self.node1}, {self.node2}, {self.weight})"
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __hash__(self):
        return hash((self.node1, self.node2, self.weight))
    

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, value):
        ''' Добавляет вершину в граф '''
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2, weight):
        ''' Добавляет ребро между двумя вершинами '''
        edge = Edge(node1, node2, weight)
        self.edges.append(edge)
        node1.add_edge(node2, weight)
        node2.add_edge(node1, weight)

    def fill_graph(self, nodes_count, edges_count):
        ''' Заполняет граф случайными вершинами и ребрами '''
        for i in range(nodes_count):
            self.add_node(i)
        for _ in range(edges_count):
            node1 = random.choice(self.nodes)
            node2 = random.choice(self.nodes)
            weight = random.randint(1, 10)
            self.add_edge(node1, node2, weight)
            
    def adjacency_list(self):
        ''' Возвращает список смежности '''
        adjacency_list = []
        for node in self.nodes:
            adjacency_list.append([node.value, [(edge.node2.value, edge.weight) for edge in node.edges]])
        return adjacency_list

    def __repr__(self):
        return f"Graph({self.nodes}, {self.edges})"

    def __str__(self):
        return f"Graph({self.nodes}, {self.edges})"
    
    def __eq__(self, other):
        return self.nodes == other.nodes and self.edges == other.edges
    
    
if __name__ == '__main__':
    # Создание графа
    graph = Graph()
    
    # Заполнение графа
    graph.fill_graph(5, 10)
    
    # Вывод графа
    print(graph)
    
    # Вывод списка смежности
    print(graph.adjacency_list())
    
