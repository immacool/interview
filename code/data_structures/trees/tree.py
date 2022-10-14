
# Дерево - это структура данных, которая состоит из узлов и связей между ними в виде дерева.
# По сути это граф, в котором нет циклов, имеющий структуру древа.
# Деревья используются для разных задач, например:
# - для хранения иерархических данных, например файловая система
# - для хранения данных с древовидной структурой, например HTML-документ
# - для хранения данных, которые легко представить в виде дерева, например выражения в арифметическом выражении
# - и т.д.

# Стандартный функционал, которым должен обладать класс дерева:
# - добавление узла в дерево
# - удаление узла из дерева
# - поиск узла в дереве
# - получение списка узлов дерева
# - получение списка детей узла
# - получение списка родителей узла

# Дерево может быть реализовано разными способами:
# - массивом
# - связным списком
# - двоичным деревом
# - кучей
# - красно-черным деревом
# - и т.д.

# В этом примере реализуется двоичное дерево.

import random


class Node:
    ''' Узел дерева. '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)
    
class Tree:
    ''' Двоичное дерево. '''
    def __init__(self):
        self.root = None
        
    def fill_tree(self, depth: int, width: int, node_chance: int):
        ''' Заполнение дерева случайными узлами. 
            depth - глубина дерева
            width - ширина дерева
            node_chance - вероятность появления узла в дереве (0..1)'''
        for _ in range(depth):
            for _ in range(width):
                if random.random() < node_chance:
                    self.add(random.randint(0, 100))
        
    def add(self, value):
        ''' Добавление узла в дерево. '''
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)
            
    def _add(self, value, node):
        ''' Добавление узла в дерево. '''
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
                
    def find(self, value):
        ''' Поиск узла в дереве. '''
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None
        
    def _find(self, value, node):
        ''' Поиск узла в дереве. '''
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)
        
    def delete_tree(self):
        ''' Удаление дерева. '''
        self.root = None
        
    def print_tree(self):
        ''' Печать дерева. '''
        if self.root is not None:
            self._print_tree(self.root)
            
    def _print_tree(self, node):
        ''' Печать дерева. '''
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)
            
    def get_nodes(self):
        ''' Получение списка узлов дерева. '''
        if self.root is not None:
            return self._get_nodes(self.root)
        else:
            return []
        
    def _get_nodes(self, node):
        ''' Получение списка узлов дерева. '''
        nodes = []
        if node.left is not None:
            nodes += self._get_nodes(node.left)
        nodes.append(node.value)
        
        if node.right is not None:
            nodes += self._get_nodes(node.right)
        return nodes
    
    def get_children(self, value):
        ''' Получение списка детей узла. '''
        if self.root is not None:
            return self._get_children(value, self.root)
        else:
            return []
        
    def _get_children(self, value, node):
        ''' Получение списка детей узла. '''
        children = []
        if value == node.value:
            if node.left is not None:
                children.append(node.left.value)
            if node.right is not None:
                children.append(node.right.value)
            return children
        elif value < node.value and node.left is not None:
            return self._get_children(value, node.left)
        elif value > node.value and node.right is not None:
            return self._get_children(value, node.right)
        
    def get_parents(self, value):
        ''' Получение списка родителей узла. '''
        if self.root is not None:
            return self._get_parents(value, self.root)
        else:
            return []
        
    def _get_parents(self, value, node):
        ''' Получение списка родителей узла. '''
        parents = []
        if value == node.value:
            return parents
        elif value < node.value and node.left is not None:
            parents.append(node.value)
            return parents + self._get_parents(value, node.left)
        elif value > node.value and node.right is not None:
            parents.append(node.value)
            return parents + self._get_parents(value, node.right)
        
    def get_height(self):
        ''' Получение высоты дерева. '''
        if self.root is not None:
            return self._get_height(self.root)
        else:
            return 0
        
    def _get_height(self, node):
        ''' Получение высоты дерева. '''
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))
        
    def get_width(self):
        ''' Получение ширины дерева. '''
        if self.root is not None:
            return self._get_width(self.root)
        else:
            return 0
        
    def _get_width(self, node):
        ''' Получение ширины дерева. '''
        if node is None:
            return 0
        else:
            return 1 + self._get_width(node.left) + self._get_width(node.right)
        
    def get_leaves(self):
        ''' Получение списка листьев дерева. '''
        if self.root is not None:
            return self._get_leaves(self.root)
        else:
            return []
        
    def _get_leaves(self, node):
        ''' Получение списка листьев дерева. '''
        leaves = []
        if node.left is not None:
            leaves += self._get_leaves(node.left)
        if node.right is not None:
            leaves += self._get_leaves(node.right)
        if node.left is None and node.right is None:
            leaves.append(node.value)
        return leaves
    
    def get_nodes_count(self):
        ''' Получение количества узлов дерева. '''
        if self.root is not None:
            return self._get_nodes_count(self.root)
        else:
            return 0
        
    def _get_nodes_count(self, node):
        ''' Получение количества узлов дерева. '''
        count = 1
        if node.left is not None:
            count += self._get_nodes_count(node.left)
        if node.right is not None:
            count += self._get_nodes_count(node.right)
        return count
    
    def get_level(self, value):
        ''' Получение уровня узла. '''
        if self.root is not None:
            return self._get_level(value, self.root)
        else:
            return 0
        
    def _get_level(self, value, node, level=1):
        ''' Получение уровня узла. '''
        if value == node.value:
            return level
        elif value < node.value and node.left is not None:
            return self._get_level(value, node.left, level + 1)
        elif value > node.value and node.right is not None:
            return self._get_level(value, node.right, level + 1)
    
if __name__ == '__main__':
    tree = Tree()
    tree.fill_tree(depth=3, width=3, node_chance=.5)
    
    # Визуализация дерева
    nodes = tree.get_nodes()
    for node in nodes:
        print(node, '->', tree.get_children(node))
    print('Высота дерева:', tree.get_height())
    print('Ширина дерева:', tree.get_width())
        
    