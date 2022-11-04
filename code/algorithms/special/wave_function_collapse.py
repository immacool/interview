# Коллапс волновой функции - это алгоритм, который генерирует случайные паттерны на основе набора правил.
# Это позволяет создавать уникальные структуры в разном количестве измерений.
# Суть алгоритма: 
# Создается карта, в которой ключ - определенный паттерн, а значение - элементы, рядом с которыми он может находиться.
# Потом, на какую-то плоскость помещается начальный элемент, и на основе правил, которые мы задали, от него 
# генерируются все возможные варианты, которые могут находиться рядом с ним, до тех пор, пока не будет достигнут
# лимит генерации, либо вся плоскость не заполнена.

import enum, rich
from rich.prompt import Prompt
from typing import Any, Tuple
import numpy as np
from collections import defaultdict


def restore_plane(plane, pattern_to_number):
    new_plane = []
    for row in plane:
        new_row = []
        for element in row:
            for pattern, number in pattern_to_number.items():
                if number == element:
                    new_row.append(pattern)
        new_plane.append(new_row)
    return new_plane


def wave_function_collapse(rules: dict, size: Tuple[int, int], initial_element: Any, limit=1000):
    '''
    :rules: Словарь, в котором ключ - паттерн, а значение - элементы, рядом с которыми он может находиться.
    :size: Размер плоскости, на которой будет происходить генерация.
    :initial_element: Начальный элемент, с которого начнется генерация.
    :limit: Лимит генерации.
    :return: Сгенерированная плоскость.
    '''
    
    # Создаем словарь, соотносящий каждому значению паттерна - число
    # Это неоходимо для того, чтобы пользоваться методами numpy.
    pattern_to_number = {pattern: i + 1 for i, pattern in enumerate(rules.keys())}
    # Переписть правила с использованием чисел.
    int_rules = defaultdict(dict)
    for pattern, variants in rules.items():
        new_pattern = pattern_to_number[pattern]
        for variant in variants:
            int_rules[new_pattern][pattern_to_number[variant]] = rules[pattern][variant]
    
    print(int_rules)
    # Создаем плоскость, заполненную нулями.
    plane = np.zeros(size)
    
    # Заполняем начальный элемент.
    plane[0, 0] = pattern_to_number[initial_element]
            
    # Заполняем плоскость пока не достигнем лимита из аргумента
    # или пока не заполним всю плоскость.
    while np.count_nonzero(plane) < size[0] * size[1]:
        # Получам все заполненные элементы.
        filled_elements = np.argwhere(plane)
        # Получаем пустые элементы вокруг заполненных.
        empty_elements = []
        filled_nearby = []
        for x, y in filled_elements:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if 0 <= x + dx < size[0] and 0 <= y + dy < size[1] and plane[x + dx, y + dy] == 0:
                    empty_elements.append((x + dx, y + dy))
                    filled_nearby.append((x, y))
                    
        # Если пустых элементов нет, то генерация закончена.
        if not empty_elements:
            break
        
        # Проходим по всем пустым элементам.
        for idx, (x, y) in enumerate(empty_elements):
            print(f'\rCurrent position: {x}, {y} | '
                  f'Filled: {np.count_nonzero(plane)} / {size[0] * size[1]} | '
                  f'Last match {plane[empty_elements[idx-1]]}', end='')
            # Получаем все возможные варианты для данного элемента.
            variants = set(int_rules[plane[filled_nearby[idx]]])
            # Если вариантов нет, то генерация закончена.
            if not variants:
                break
            # Обновляем варианты, исходя из того, что уже заполнено вокруг.
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if 0 <= x + dx < size[0] and 0 <= y + dy < size[1] and plane[x + dx, y + dy] != 0:
                    variants &= set(int_rules[plane[x + dx, y + dy]])
            # Выбираем случайный вариант из оставшихся с учетом вероятностей.
            probabilities = [int_rules[plane[filled_nearby[idx]]][variant] for variant in variants]
            probabilities = np.array(probabilities) / sum(probabilities)
            # Заполняем элемент.
            plane[x, y] = np.random.choice(list(variants), p=probabilities)
            # Если достигнут лимит, то генерация закончена.
            if np.count_nonzero(plane) == size[0] * size[1]:
                break

    # Восстанавливаем плоскость с использованием паттернов.
    new_plane = restore_plane(plane, pattern_to_number)
    
    return new_plane

    
class Pattern(enum.Enum):
    SEA = '~'
    LAND = ' '
    TREE = 'T'
    MOUNTAIN = '^'
    
    
def main():
    # Создаем словарь, в котором ключ - паттерн, а значение - элементы, рядом с которыми он может находиться, и вероятность
    # их появления.
    rules = {
        Pattern.SEA: {Pattern.SEA: 0.6, Pattern.LAND: 0.4},
        Pattern.LAND: {Pattern.SEA: 0.25, Pattern.LAND: 0.25, Pattern.TREE: 0.25, Pattern.MOUNTAIN: 0.25},
        Pattern.TREE: {Pattern.LAND: 0.5, Pattern.TREE: 0.5},
        Pattern.MOUNTAIN: {Pattern.LAND: 0.5, Pattern.MOUNTAIN: 0.5}
    }
    # Задаем размерность карты.
    size = (20, 50)
    # Генерируем паттерн.
    plane = wave_function_collapse(rules, size, initial_element=Pattern.SEA)
    # Выводим паттерн.
    def colored(pattern) -> str:
        match pattern:
            case Pattern.SEA:
                return f'[white on blue]{pattern.value}[/]'
            case Pattern.LAND:
                return f'[dim green on green]{pattern.value}[/]'
            case Pattern.TREE:
                return f'[dim green on green]{pattern.value}[/]'
            case Pattern.MOUNTAIN:
                return f'[white on black]{pattern.value}[/]'
    print('\nPattern:')
    for row in plane:
        rich.print(''.join([colored(i) for i in row]))
        

if __name__ == '__main__':
    main()
    main()
    main()
    main()
    
        
