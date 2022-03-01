"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
import statistics

M = 5
SIZE = M * 2 + 1
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = 0
b = 0
for i in range(len(array)):
    med = array[i]
    for j in range(len(array)):
        if array[j] <= med:
            a += 1
        if array[j] >= med:
            b += 1
    if a == len(array) // 2 + 1 or b == len(array) // 2 + 1 or a >= len(array) // 2 + 1 and b >= len(array) // 2 + 1:
        print(f'медианой массива является число {med}')
        break
    a = 0
    b = 0

# условий нагородила, но вроде работает. проверяла много)) раз

# для проверки

print(statistics.median(array))
