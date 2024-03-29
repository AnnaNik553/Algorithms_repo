"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
 Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        x = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                x = True
        n += 1
        if x is False:
            break

    return arr


print(bubble_sort(array))

# по улучшению фантазии не хватило) воспользовалась подсказкой из методички - выход из цикла, если не было перестановок
