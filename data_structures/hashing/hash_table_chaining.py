from hash_table import HashTable
from hash_function import codes_sum

# Хэш-таблица с цепочками - это структура данных, которая позволяет хранить пары ключ-значение.
# Отличие от хэш-таблицы заключается в том, что в хэш-таблице с цепочками каждый элемент
# хэш-таблицы является связным списком, в котором хранятся все элементы, которые были
# добавлены в хэш-таблицу с одинаковым хэш-значением.
# Хэш-таблица с цепочками должна обеспечивать следующие операции:
# - добавление элемента в хэш-таблицу
# - удаление элемента из хэш-таблицы
# - поиск элемента в хэш-таблице

# Хэш-функция для хэш-таблицы с цепочками
# В качестве хэш-функции для хэш-таблицы с цепочками используется функция codes_sum,
# которая возвращает сумму кодов символов строки.


class HashTableChaining:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.hash_table)

    def add(self, key, value):
        hash_value = codes_sum(key, self.size)
        key_exists = False
        bucket = self.hash_table[hash_value]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_value = codes_sum(key, self.size)
        bucket = self.hash_table[hash_value]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
        return None

    def delete(self, key):
        hash_value = codes_sum(key, self.size)
        key_exists = False
        bucket = self.hash_table[hash_value]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Ключ {} найден'.format(key))
        else:
            print('Ключ {} не найден'.format(key))


if __name__ == '__main__':
    # Создаем хэш-таблицу с цепочками
    hash_table = HashTableChaining(256)

    # Добавляем элементы в хэш-таблицу
    hash_table.add('cat', '#ff0000')
    hash_table.add('dog', '#00ff00')
    hash_table.add('fish', '#0000ff')

    # Выводим хэш-таблицу на экран
    print(hash_table)

    # Получаем значение элемента из хэш-таблицы
    print(hash_table.get('dog'))

    # Удаляем элемент из хэш-таблицы
    hash_table.delete('dog')

    # Выводим хэш-таблицу на экран
    print(hash_table)

    # Получаем значение элемента из хэш-таблицы
    print(hash_table.get('dog'))