import random

# Быстрая сортировка - это алгоритм сортировки, который использует принцип "разделяй и властвуй"
# Основная идея - выбрать опорный элемент, и разделить массив на две части - элементы меньше
# опорного и элементы больше опорного. Далее рекурсивно сортируем каждую часть массива.

def quick_sort(array):
    if len(array) <= 1: # Если массив состоит из одного элемента
        return array # Возвращаем его
    else: # Иначе
        q = random.choice(array) # Выбираем случайный опорный элемент
        l_nums = [n for n in array if n < q] # Меньшие опорного
        e_nums = [q] * array.count(q) # Равные опорному
        b_nums = [n for n in array if n > q] # Большие опорного
        # Возвращаем отсортированный массив. Рекурсивно вызываем функцию для каждой части массива
        return quick_sort(l_nums) + e_nums + quick_sort(b_nums)
    
if __name__ == "__main__":
    # Тест функции quick_sort
    array = [random.randint(0, 100) for _ in range(100)]
    assert quick_sort(array) == sorted(array)
