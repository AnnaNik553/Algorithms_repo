"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_neg = 0
pos_neg = 0
for i, item in enumerate(array):
    if item < 0 and max_neg == 0:
        max_neg = item
        pos_neg = i
        continue
    elif (item < 0) and (item > max_neg):
        max_neg = item
        pos_neg = i
if max_neg == 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимальное отрицательное число равно {max_neg}, его позиция в массиве {pos_neg}')
