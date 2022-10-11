from hash_table import HashTable
from hash_function import codes_sum

# Хэш-сет - это структура данных, которая позволяет хранить уникальные значения.
# Хэш-сет использует хэш-таблицу для хранения значений.
# Хэш-сет должен обеспечивать следующие операции:
# 1. Добавление элемента в хэш-сет
# 2. Удаление элемента из хэш-сета
# 3. Проверка наличия элемента в хэш-сете

class HashSet(HashTable):
    ''' Реализация Хэш-сета '''
    def __init__(self, size=10, hash_func=None):
        super().__init__(size, hash_func)
        
    def add(self, key, value):
        ''' Добавление элемента в хэш-сет '''
        if key in self:
            return False
        
        self.put(key, value)
        return True
    
    def pop(self, key):
        ''' Удаление элемента из хэш-сета '''
        if not key in self:
            return False
        
        self.remove(key)
        return True
    
    
if __name__ == "__main__":
    # Создание хэш-сета
    hash_set = HashSet(hash_func=codes_sum)
    
    # Добавление элементов в хэш-сет
    hash_set.add("key1", "value1")
    hash_set.add("key2", "value2")
    hash_set.add("key3", "value3")
    
    # Проверка наличия элементов в хэш-сете
    print("key1" in hash_set)
    print("key2" in hash_set)
    print("key3" in hash_set)
    print("key4" in hash_set)
    
    # Удаление элементов из хэш-сета
    hash_set.pop("key1")
    hash_set.pop("key2")
    hash_set.pop("key3")
    
    # Проверка наличия элементов в хэш-сете
    print("key1" in hash_set)
    print("key2" in hash_set)
    print("key3" in hash_set)
    print("key4" in hash_set)