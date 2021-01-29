"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

new_array = list(set(array))
print(new_array)

tmp_count_often = 0
digit = 0
count_often = 0
for j, el in enumerate(new_array):
    often_digit = new_array[j]
    for i, item in enumerate(array):
        if item == often_digit:
            tmp_count_often += 1
    if tmp_count_often > count_often:
        digit = el
        count_often = tmp_count_often
    tmp_count_often = 0
if count_often > 1:
    print(f'Чаще всего встречается число {digit} - {count_often} раз(а)')
else:
    print('Числа не повторяются')
