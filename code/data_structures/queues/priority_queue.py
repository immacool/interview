# Очередь с приоритетом - это очередь, в которой элементы имеют определеенный приоритет (число), 
# представляющее собой значение, которое определяет порядок элементов в очереди.
# Элементы с наибольшим приоритетом находятся в начале очереди, с наименьшим приоритетом - в конце.

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, item, priority):
        ''' Добавление элемента в начало очереди '''
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        
    def remove(self):
        ''' Удаление элемента из начала очереди '''
        return self.queue.pop(0)
    
    def is_empty(self):
        ''' Возвращает True, если очередь пуста '''
        return self.queue == []
    
    def size(self):
        ''' Возвращает размер очереди '''
        return len(self.queue)
    
    def peek(self):
        ''' Возвращает первый элемент очереди '''
        return self.queue[0]
    
    def __contains__(self, item):
        ''' Проверка наличия элемента в очереди '''
        for i in self.queue:
            if i[0] == item:
                return True
        return False
    
if __name__ == "__main__":
    # Тест класса PriorityQueue
    pq = PriorityQueue()
    pq.add(10, 1)
    pq.add(20, 2)
    pq.add(50, 5)
    pq.add(40, 4)
    pq.add(30, 3)
    assert 20 in pq
    assert 40 in pq
    assert pq.size() == 5
    assert pq.peek() == (10, 1)
    assert pq.remove() == (10, 1)
    assert pq.size() == 4
    
        