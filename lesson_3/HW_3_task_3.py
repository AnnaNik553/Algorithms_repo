"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el_inx = 0
max_el = array[0]
min_el_inx = 0
min_el = array[0]
for i, item in enumerate(array):
    if item > max_el:
        max_el_inx = i
        max_el = item
    elif item < min_el:
        min_el_inx = i
        min_el = item
array[min_el_inx], array[max_el_inx] = array[max_el_inx], array[min_el_inx]
print(array)
