import random
from hash_function import codes_sum, polynomial_hash

# Хеш-таблица - это структура данных, которая позволяет хранить пары ключ-значение.
# Ключи должны быть уникальными, а значения могут повторяться.
# Хеш-таблица использует хеш-функцию для вычисления индекса в массиве, в котором хранятся значения.
# Хеш-функция принимает ключ и возвращает индекс в массиве.

# Причина, по которой хеш-таблицы работают быстро, заключается в том, что хеш-функция позволяет нам
# найти значение для ключа за O(1) (в среднем). Среднее время O(1) достигается за счет того, что
# хеш-функция должна быть хорошо распределена. Если хеш-функция не хорошо распределена, то
# мы можем получить ситуацию, когда все значения хранятся в одном массиве, что приведет к
# худшему случаю O(n).

# В Python хеш-таблица реализована в виде словаря. Словарь - это хеш-таблица, в которой
# ключи и значения могут быть любого типа. В Python 3.6+ словари реализованы в виде хеш-таблиц,
# а в Python 3.5 и раньше - в виде деревьев. В Python 3.6+ словари стали более эффективными,
# чем деревья, поскольку хеш-таблицы работают быстрее.
# Однако ее можно реализовать и самостоятельно в виде класса. Ниже приведен пример реализации.

class HashTable:
    ''' Хеш-таблица '''
    def __init__(self, size=10, hash_func=None):
        self.size = size
        # Листы для хранения ключей и значений
        self.slots = [None] * self.size
        self.data = [None] * self.size
        # Хеш-функция
        if hash_func is None:
            self.hash_func = codes_sum
        else:
            self.hash_func = hash_func
            
    def rehash(self, old_hash):
        ''' Перехеширование '''
        return (old_hash + 1) % self.size
        
    def put(self, key: str, data):
        ''' Добавление пары ключ-значение '''
        # Получаем индекс в массиве
        hashvalue = self.hash_func(key, self.size)
        
        # Если в слоте нет значения, то добавляем ключ и значение
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # Если значение уже есть, то перезаписываем его
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # Если значение не совпадает с ключом, то ищем следующий свободный слот
                # и добавляем туда ключ и значение (линейное пробирование)
                # Линейное пробирование - это метод разрешения коллизий, при котором при
                # коллизии мы просто переходим к следующему слоту и проверяем его на пустоту.
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    # Пока не найдем пустой слот или слот с таким же ключом
                    # переходим к следующему слоту
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
                    
    def get(self, key):
        ''' Получение значения по ключу '''
        # Получаем индекс в листе
        startslot = self.hash_func(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = startslot
        # Пока не найдем значение или не дойдем до конца листа
        # (линейное пробирование)
        while self.slots[position] != None and not found and not stop:
            # Если ключ совпадает с ключом в слоте, то получаем значение
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # Если ключ не совпадает, то переходим к следующему слоту
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data
    
    def remove(self, key):
        ''' Удаление пары ключ-значение '''
        # Получаем индекс в листе
        startslot = self.hash_func(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = startslot
        # Пока не найдем значение или не дойдем до конца листа
        # (линейное пробирование)
        while self.slots[position] != None and not found and not stop:
            # Если ключ совпадает с ключом в слоте, то удаляем пару
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None
            else:
                # Если ключ не совпадает, то переходим к следующему слоту
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data
    
    def __contains__(self, key):
        ''' Проверка наличия ключа в словаре '''
        return self.get(key) != None
    
    def __getitem__(self, key):
        ''' Получение значения по ключу '''
        return self.get(key)
    
    def __setitem__(self, key: str, data):
        ''' Добавление пары ключ-значение '''
        self.put(key, data)
        
    

if __name__ == '__main__':
    # Создание хеш-таблиц
    h = HashTable(hash_func=codes_sum)
    h2 = HashTable(hash_func=polynomial_hash)
    
    print('Хеш-функция: codes_sum')
    # Вставка пар ключ-значение
    h['one'] = 1
    h['two'] = 2
    h['three'] = 3
    
    # Получение значения по ключу
    print(h['one'])
    print(h['two'])
    print(h['three'])
    
    # Перезапись значения
    h['one'] = 11
    print(h['one'])
    
    # Удаление пары ключ-значение
    h.remove('one')
    print(h['one'])
    
    print('Хеш-функция: polynomial_hash')
    # Вставка пар ключ-значение
    h2['one'] = 1
    h2['two'] = 2
    h2['three'] = 3
    
    # Получение значения по ключу
    print(h2['one'])
    print(h2['two'])
    print(h2['three'])
    
    # Перезапись значения
    h2['one'] = 11
    print(h2['one'])
    
    # Удаление пары ключ-значение
    h2.remove('one')
    print(h2['one'])
    
    
