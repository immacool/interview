from random import uniform
from tqdm import trange
from math import sqrt

import tkinter

# Оценка числа Пи методом Монте-Карло
# Метод Монте-Карло - это метод, который используется для приближенного вычисления численных интегралов
# Основная идея - сгенерировать случайные точки внутри заданной области, и подсчитать количество точек,
# которые попали в заданную область. Доля точек, которые попали в заданную область, будет приближенно
# равняться отношению площади заданной области к площади единичной окружности.

def estimate_pi(samples):
    points_inside = 0 # Количество точек, которые попали в круг
    for _ in trange(samples): # Генерируем заданное количество точек
        x, y = uniform(0, 1), uniform(0, 1) # Генерируем случайную точку
        if sqrt(x * x + y * y) < 1: # Проверяем, попал ли точка в единичную окружность
            points_inside += 1 # Если попал, увеличиваем счетчик точек внутри окружности
    return 4 * points_inside / samples # Возвращаем приближенное значение числа Пи


samples = 10 ** 5
points_inside = 0
sequence = []
for _ in trange(samples):
    x, y = uniform(-1, 1), uniform(-1, 1)
    sequence.append((x, y))
    if sqrt(x * x + y * y) < 1:
        points_inside += 1
pi = 4 * points_inside / samples
print(pi)

# разделение значений на цвета
colors = [sqrt(x * x + y * y) < 1 for x, y in sequence]

# создание окна
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()

# отрисовка точек
for (x, y), color in zip(sequence, colors):
    x = (x + 1) * 250
    y = (y + 1) * 250
    canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='red' if color else 'blue')
    
# отрисовка окружности
canvas.create_oval(0, 0, 500, 500, outline='black')

# запуск окна
root.mainloop()
