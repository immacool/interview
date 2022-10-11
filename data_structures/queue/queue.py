import random

# Очередь - это структура данных, которая работает по принципу FIFO (first in - first out)
# Основная идея - использовать список, но операции вставки и удаления
# будут происходить с других концов списка. То есть вставка будет происходить
# в конец списка, а удаление - с начала списка.

class Queue:
    ''' Основной класс очереди '''
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        ''' Проверка на пустоту очереди '''
        return self.items == []

    def enqueue(self, item):
        ''' Добавление элемента в конец списка '''
        self.items.append(item)

    def dequeue(self):
        ''' Удаление элемента из начала списка '''
        return self.items.pop(0)

    def size(self):
        ''' Возвращает размер очереди '''
        return len(self.items)
    
if __name__ == "__main__":
    # Тест класса Queue
    q = Queue()
    for _ in range(100):
        q.enqueue(random.randint(0, 100))
    assert q.size() == 100
    for _ in range(100):
        q.dequeue()
    assert q.size() == 0
