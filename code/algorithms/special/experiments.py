import numpy as np
import pandas as pd


zeros = np.zeros((10, 10))

print(zeros)

x, y = 5, 5
zeros[x, y] = 1

print(zeros)

empty = np.argwhere(zeros == 0)
empty = empty[np.all(np.abs(empty - [x, y]) <= 1, axis=1)]

print(empty)

for i in empty:
    zeros[i[0], i[1]] = 2
    
print(zeros)