import random

# Хэш-функция - это некий алгоритм, который преобразует ключ (строку) в индекс (число).
# Хэш-функция должна быть:
# - однозначной, т.е. для одного ключа всегда должен возвращаться один и тот же индекс.
# - быстрой, т.е. для одного ключа должно выполняться за константное время.
# - равномерной, т.е. для разных ключей должны получаться разные индексы.


def codes_sum(key, size):
    # Реализация хэш-функции: сумма кодов символов ключа по модулю размера таблицы.
    # Сложность: O(n).
    return sum(ord(char) for char in key) % size


def polynomial_hash(key, size):
    # Реализация хэш-функции: полиномиальный хэш.
    # Сложность: O(n).
    hash = 0
    for char in key:
        hash = (hash * 31 + ord(char)) % size
    return hash


if __name__ == "__main__":
    size = 100
    keys = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
    # Разброс хэш-функции codes_sum.
    print("Разброс хэш-функции codes_sum:")
    for key in keys:
        print(f"key = {key}, hash = {codes_sum(key, size)}")
    # Разброс хэш-функции polynomial_hash.
    print("Разброс хэш-функции polynomial_hash:")
    for key in keys:
        print(f"key = {key}, hash = {polynomial_hash(key, size)}")
