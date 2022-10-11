import random

# Linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers.
# A linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

# Связный список - линейная структура данных, в которой элементы не хранятся в последовательных ячейках памяти.
# Элементы в связном списке связаны с помощью указателей.
# Связный список состоит из узлов, в которых каждый узел содержит поле данных и ссылку на следующий узел в списке.


class Node:
    ''' Класс узла, в котором хранится значение и ссылка на следующий узел '''

    def __init__(self, data):
        ''' Инициализация узла '''
        self.data = data
        self.next = None


class LinkedList:
    ''' Класс связного списка '''

    def __init__(self):
        ''' Инициализация связного списка '''
        self.head = None

    def insert(self, data):
        ''' Вставка элемента в начало связного списка '''
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        ''' Вставка элемента в конец связного списка '''
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def delete(self, key):
        ''' Удаление элемента из связного списка '''
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        ''' Вывод связного списка '''
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverse(self):
        ''' Реверс связного списка '''
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_recursive(self):
        ''' Реверс связного списка рекурсивно '''

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def tail(self):
        ''' Возвращает последний элемент связного списка '''
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.data


def create_example_list(size=10):
    ''' Создание примера связного списка '''
    llist = LinkedList()
    rnd_list = [i for i in range(size)]
    random.shuffle(rnd_list)
    for i in rnd_list:
        llist.append(i)
    return llist


if __name__ == '__main__':
    # Тестирование связного списка и его фукнций по отдельности
    random.seed(42)

    # Создание связного списка
    # [ 7 3 2 8 5 6 9 4 0 1 ]
    llist = create_example_list()
    assert llist.head.data == 7

    # Вставка элемента в начало связного списка
    llist.insert(10)
    assert llist.head.data == 10

    # Вставка элемента в конец связного списка
    llist.append(11)
    assert llist.tail() == 11

    # Удаление элемента из связного списка
    llist.delete(10)
    assert llist.head.data == 7

    # Реверс связного списка
    llist.reverse()
    assert llist.head.data == 11

    # Реверс связного списка рекурсивно
    llist.reverse_recursive()
    assert llist.head.data == 7

    # Вывод связного списка
    llist.print_list()
    # 7 3 2 8 5 6 9 4 0 1
