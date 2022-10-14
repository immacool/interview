import timeit, random

from sorting.quick_sort import quick_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort

def benchmark_sorting(sorting_function):
    """ Оценка времени работы алгоритма сортировки """
    start = timeit.default_timer()
    for i in range(500):
        sorting_function([random.randint(0, 1000) for _ in range(i)])
    end = timeit.default_timer()
    return end - start

def main():
    """ Главная функция """
    print("Быстрая сортировка: ", benchmark_sorting(quick_sort))
    print("Сортировка выбором: ", benchmark_sorting(selection_sort))
    print("Сортировка слиянием: ", benchmark_sorting(merge_sort))
    print("Сортировка вставками: ", benchmark_sorting(insertion_sort))
    
if __name__ == "__main__":
    main()