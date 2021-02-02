"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
 первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Задача 3 из урока 3
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from timeit import timeit
from cProfile import run

# 1 вариант


def version_1(n):
    array = [random.randint(0, 100) for _ in range(n)]
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
    return array


print(timeit('version_1(10)', number=1_000, globals=globals()))      #  0.0179845
print(timeit('version_1(100)', number=1_000, globals=globals()))      #  0.15690130000000002
print(timeit('version_1(1_000)', number=1_000, globals=globals()))      #  1.6504455
print(timeit('version_1(10_000)', number=1_000, globals=globals()))      #  12.758556500000001
print(timeit('version_1(100_000)', number=1_000, globals=globals()))      #  99.4673198
print(timeit('version_1(1_000_000)', number=1_000, globals=globals()))      #  1011.3319041000001

run('version_1(100_000)')
run('version_1(1_000_000)')

# 526801 function calls in 0.193 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.193    0.193 <string>:1(<module>)
#      1    0.007    0.007    0.193    0.193 HW_4_task_1.py:22(version_1)
#      1    0.032    0.032    0.186    0.186 HW_4_task_1.py:23(<listcomp>)
# 100000    0.057    0.000    0.123    0.000 random.py:200(randrange)
# 100000    0.032    0.000    0.154    0.000 random.py:244(randint)
# 100000    0.044    0.000    0.066    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.193    0.193 {built-in method builtins.exec}
# 100000    0.008    0.000    0.008    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126796    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       5266655 function calls in 1.967 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    1.967    1.967 <string>:1(<module>)
#      1    0.073    0.073    1.966    1.966 HW_4_task_1.py:22(version_1)
#      1    0.328    0.328    1.892    1.892 HW_4_task_1.py:23(<listcomp>)
# 1000000    0.579    0.000    1.244    0.000 random.py:200(randrange)
# 1000000    0.320    0.000    1.564    0.000 random.py:244(randint)
# 1000000    0.448    0.000    0.665    0.000 random.py:250(_randbelow_with_getrandbits)
#       1    0.000    0.000    1.967    1.967 {built-in method builtins.exec}
# 1000000    0.085    0.000    0.085    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1266650    0.132    0.000    0.132    0.000 {method 'getrandbits' of '_random.Random' objects}

# 2 вариант


def version_2(n):
    array = [random.randint(0, 100) for _ in range(n)]
    max_ = array.index(max(array))
    min_ = array.index(min(array))
    array[min_], array[max_] = array[max_], array[min_]
    return array


print(timeit('version_2(10)', number=1_000, globals=globals()))      # 0.010969199999999998
print(timeit('version_2(100)', number=1_000, globals=globals()))      # 0.0960535
print(timeit('version_2(1_000)', number=1_000, globals=globals()))      # 0.9436575
print(timeit('version_2(10_000)', number=1_000, globals=globals()))      # 9.568958199999999
print(timeit('version_2(100_000)', number=1_000, globals=globals()))      # 95.54415610000001
print(timeit('version_2(1_000_000)', number=1_000, globals=globals()))      # 973.449172

run('version_2(100_000)')
run('version_2(1_000_000)')

# 526867 function calls in 0.193 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.193    0.193 <string>:1(<module>)
#      1    0.000    0.000    0.193    0.193 HW_4_task_1.py:89(version_2)
#      1    0.031    0.031    0.189    0.189 HW_4_task_1.py:90(<listcomp>)
# 100000    0.058    0.000    0.126    0.000 random.py:200(randrange)
# 100000    0.032    0.000    0.158    0.000 random.py:244(randint)
# 100000    0.045    0.000    0.067    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.193    0.193 {built-in method builtins.exec}
#      1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
#      1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
# 100000    0.008    0.000    0.008    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126858    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
#       5267421 function calls in 1.928 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    1.928    1.928 <string>:1(<module>)
#      1    0.000    0.000    1.927    1.927 HW_4_task_1.py:89(version_2)
#      1    0.324    0.324    1.890    1.890 HW_4_task_1.py:90(<listcomp>)
# 1000000    0.580    0.000    1.245    0.000 random.py:200(randrange)
# 1000000    0.322    0.000    1.566    0.000 random.py:244(randint)
# 1000000    0.447    0.000    0.665    0.000 random.py:250(_randbelow_with_getrandbits)
#       1    0.000    0.000    1.928    1.928 {built-in method builtins.exec}
#       1    0.019    0.019    0.019    0.019 {built-in method builtins.max}
#       1    0.018    0.018    0.018    0.018 {built-in method builtins.min}
# 1000000    0.085    0.000    0.085    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1267412    0.132    0.000    0.132    0.000 {method 'getrandbits' of '_random.Random' objects}
#       2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# 3 вариант, через рекурсию


def version_3(n):
    array = [random.randint(0, 100) for _ in range(n)]

    def min_max(array, i=0, min_=0, max_=0):
        if i == len(array):
            return min_, max_
        elif array[i] < array[min_]:
            return min_max(array, i + 1, i, max_)
        elif array[i] > array[max_]:
            return min_max(array, i + 1, min_, i)
        else:
            return min_max(array, i + 1, min_, max_)

    min_, max_ = min_max(array)
    array[min_], array[max_] = array[max_], array[min_]
    return array


print(timeit('version_3(10)', number=1_000, globals=globals()))      # 0.013384299999999998
print(timeit('version_3(100)', number=1_000, globals=globals()))      # 0.1213649
print(timeit('version_3(900)', number=1_000, globals=globals()))      # 1.1632050999999999
# при n > - максимальная глубина рекурсии превышена при вызове объекта Python

run('version_3(10)')
run('version_3(100)')

# 79 function calls (69 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 HW_4_task_1.py:153(version_3)
#      1    0.000    0.000    0.000    0.000 HW_4_task_1.py:154(<listcomp>)
#   11/1    0.000    0.000    0.000    0.000 HW_4_task_1.py:156(min_max)
#     10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     10    0.000    0.000    0.000    0.000 random.py:244(randint)
#     10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       725 function calls (625 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 HW_4_task_1.py:153(version_3)
#      1    0.000    0.000    0.000    0.000 HW_4_task_1.py:154(<listcomp>)
#  101/1    0.000    0.000    0.000    0.000 HW_4_task_1.py:156(min_max)
#    100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#    100    0.000    0.000    0.000    0.000 random.py:244(randint)
#    100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    118    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""
Первый вариант решения имеет на мой взглят линейную сложность, 
т.е. O(n), т.к. при увеличении входящих данных n в 10 раз, время выполнения увеличивается примерно в 10 раз. 
Самое болбшое время расходуется на формирование списка и выполнение цикла.
 
Второй вариант решения также имеет на мой взглят линейную сложность, 
т.е. O(n). Однако, выполняется быстрее, чем первый, т.к. в алгоритме используются встроенные функции поиска
максимального и минимального элемента списка, а также поиска индекса элемента списка.
Самое болбшое время в алгоритме занимает формирование списка.

Третий рекурсивный вариант решения задачи для n < 1000  выполняется быстрее первого варианта, однако проверить n > 1000
нет возможности, т.к при n > 1000 - максимальная глубина рекурсии превышена при вызове объекта Python
По имеющимся измерениям можнос делать вывод, что алгоритм имеет линейную сложность.

Вывод: Оптимальным вариантом решения задачи является второй алгоритм, с использованием встроенных функций.  
"""

