"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(array)


def merge_sort(arr):
    if len(arr) > 1:
        arr_1 = merge_sort(arr[:len(arr) // 2])
        arr_2 = merge_sort(arr[len(arr) // 2:])
        arr = arr_1 + arr_2
        for i in range(len(arr) - 1):
            min_ = arr[i]
            min_idx = i
            for j in range(i + 1, len(arr)):
                if min_ > arr[j]:
                    min_ = arr[j]
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(merge_sort(array))
