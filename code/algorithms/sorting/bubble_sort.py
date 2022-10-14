import random

# Сортировка пузырьком - это алгоритм сортировки, в котором сравниваются два соседних элемента
# и меняются местами, если они не отсортированы. Этот процесс повторяется до тех пор, пока массив
# не будет отсортирован. Сложность: O(n^2)

def bubble_sort(array):
    """Сортировка пузырьком"""
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
if __name__ == "__main__":
    # Тест функции bubble_sort
    array = [random.randint(0, 100) for _ in range(100)]
    assert bubble_sort(array) == sorted(array)
