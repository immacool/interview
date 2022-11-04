
# Алгоритм Хеллсинга - поиск максимального паросочетания в двудольном графе (бипартитном графе)
# Он может быть использован для решения задачи о назначениях, где каждому работнику назначается одна работа
# и каждая работа назначается одному работнику (все работники и все работы различны) - это и есть двудольный граф

from code.data_structures.graphs.graph import Graph

def is_bipartite(graph: Graph):
    # Проверка на двудольность графа
    for node in graph.nodes:
        for edge in node.edges:
            if node in edge.node2.edges:
                return False

    return True

def hellings(graph: Graph):
    # Проверка на двудольность графа
    if not is_bipartite(graph):
        return None

    # Находим максимальное паросочетание
    matching = []
    for node in graph.nodes:
        if node not in matching:
            for edge in node.edges:
                if edge.node2 not in matching:
                    matching.append(node)
                    matching.append(edge.node2)
                    break

    return matching


if __name__ == '__main__':
    # Создаем двудольный граф
    graph = Graph()
    graph.fill_graph(10, 20)
    
    # Выводим максимальное паросочетание
    print(hellings(graph))
    
    