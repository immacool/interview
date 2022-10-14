import random
from code.data_structures.graphs.graph import Graph

# Поиск в ширину - это алгоритм поиска, который использует принцип "разделяй и властвуй".
# Основная идея - создать очередь, в которой хранятся все вершины, которые нужно посетить.
# После этого мы извлекаем из очереди первый элемент и добавляем его соседей в очередь.
# Если мы ищем элемент, который находится в глубине дерева, то мы сначала посетим все вершины,
# которые находятся на одном уровне с корнем, а затем перейдем к вершинам, которые находятся
# на уровне ниже и так далее, пока не найдем искомый элемент.
# Поиск в ширину можно использовать для поиска кратчайшего пути в графе.
# Сложонсть: O(V + E), где V - количество вершин, а E - количество ребер.

def breadth_first_search(graph, start, end):
    # Создаем очередь, в которую помещаем начальную вершину.
    queue = [start]
    # Создаем словарь, в котором будем хранить вершины, которые мы посетили.
    visited = {start: None}
    # Пока в очереди есть вершины, извлекаем из нее первую.
    while queue:
        current = queue.pop(0)
        # Если текущая вершина - искомая, то возвращаем путь.
        if current == end:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]
        # Добавляем соседей текущей вершины в очередь.
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    return None


if __name__ == "__main__":
    # Создаем граф.
    graph = Graph()
    graph.fill_graph(10, 15)

    # Применяем алгоритм поиска в ширину.
    start = random.choice(list(graph.get_vertices()))
    end = random.choice(list(graph.get_vertices()))
    path = breadth_first_search(graph, start, end)
    print(f"Path from {start} to {end}: {path}")