import random

# Стек - это структура данных, которая работает по принципу LIFO (last in, first out).
# Основная идея - использовать список, но операции вставки и удаления будут происходить
# с одного конца списка. То есть вставка будет происходить в конец списка, а удаление -
# из конца списка.

class Stack:
    ''' Основной класс стека '''

    def __init__(self):
        self.items = []

    def is_empty(self):
        ''' Возвращает True, если стек пуст '''
        return self.items == []

    def push(self, item):
        ''' Добавление элемента в конец списка '''
        self.items.append(item)

    def pop(self):
        ''' Удаление элемента из конца списка '''
        return self.items.pop()

    def peek(self):
        ''' Возвращает последний элемент списка '''
        return self.items[len(self.items)-1]

    def size(self):
        ''' Возвращает размер стека '''
        return len(self.items)
    
if __name__ == "__main__":
    # Тест класса Stack
    s = Stack()
    for _ in range(100):
        s.push(random.randint(0, 100))
    assert s.size() == 100
    for _ in range(100):
        s.pop()
    assert s.size() == 0
    assert s.is_empty() == True