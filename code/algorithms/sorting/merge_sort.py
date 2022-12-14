import random

# Сортировка слиянием - это алгоритм сортировки, который использует принцип "разделяй и властвуй"
# Основная идея - сортировка слиянием разбивает массив на две части, и рекурсивно сортирует каждую
# часть. Далее сливает две отсортированные части в один массив.

def merge_sort(array):
    ''' Сортировка слиянием '''
    if len(array) <= 1: # Базовый случай
        return array # Массив из одного элемента уже отсортирован
    middle = len(array) // 2 # Находим середину массива
    left = merge_sort(array[:middle]) # Рекурсивно вызываем merge_sort для левой части
    right = merge_sort(array[middle:]) # Рекурсивно вызываем merge_sort для правой части
    return merge(left, right) # Объединение двух массивов

def merge(left, right):
    ''' Слияние двух массивов '''
    result = []  # Массив для результата
    i, j = 0, 0 # Индексы для обхода массивов
    while i < len(left) and j < len(right): # Пока не дошли до конца обоих массивов
        if left[i] <= right[j]: # Если элемент в левом массиве меньше или равен элементу в правом
            result.append(left[i]) # Добавляем элемент в результат
            i += 1 # Переходим к следующему элементу в левом массиве
        else: # Если элемент в правом массиве меньше
            result.append(right[j]) # Добавляем элемент в результат
            j += 1 # Переходим к следующему элементу в правом массиве
    result += left[i:] # Добавляем оставшиеся элементы в левом массиве
    result += right[j:] # Добавляем оставшиеся элементы в правом массиве
    return result # Возвращаем результат

if __name__ == "__main__":
    # Тест функции merge_sort
    array = [random.randint(0, 100) for _ in range(100)]
    assert merge_sort(array) == sorted(array)