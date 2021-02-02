"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
from timeit import timeit
from cProfile import run

# Первый — с помощью алгоритма «Решето Эратосфена»


def sieve_(n):
    num = n * 20  # не дошло, как сделать зависимость начального списка, чтобы в него входило n простых чисел ((
    sieve = [i for i in range(num)]
    sieve[1] = 0
    sieve_no_zero = []
    for i in range(2, num):
        if sieve[i] != 0:
            sieve_no_zero.append(sieve[i])
            j = i + i
            while j < num:
                sieve[j] = 0
                j += i
    return sieve_no_zero[n-1]


print(timeit('sieve_(1)', number=100, globals=globals()))      # 0.00047789999999999985
print(timeit('sieve_(10)', number=100, globals=globals()))      # 0.004707300000000001
print(timeit('sieve_(100)', number=100, globals=globals()))      # 0.0635475
print(timeit('sieve_(1_000)', number=100, globals=globals()))      # 0.6760917000000001
print(timeit('sieve_(10_000)', number=100, globals=globals()))      # 7.6224928
print(timeit('sieve_(100_000)', number=100, globals=globals()))      # 90.6689976
print(timeit('sieve_(1_000_000)', number=100, globals=globals()))      # 1021.3950092000001

run('sieve_(10_000)')
run('sieve_(100_000)')
run('sieve_(1_000_000)')

# 17989 function calls in 0.080 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.080    0.080 <string>:1(<module>)
#      1    0.071    0.071    0.079    0.079 HW_4_task_2.py:18(sieve_)
#      1    0.006    0.006    0.006    0.006 HW_4_task_2.py:20(<listcomp>)
#      1    0.000    0.000    0.080    0.080 {built-in method builtins.exec}
#  17984    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       148938 function calls in 0.913 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.014    0.014    0.913    0.913 <string>:1(<module>)
#      1    0.809    0.809    0.899    0.899 HW_4_task_2.py:18(sieve_)
#      1    0.079    0.079    0.079    0.079 HW_4_task_2.py:20(<listcomp>)
#      1    0.000    0.000    0.913    0.913 {built-in method builtins.exec}
# 148933    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       1270612 function calls in 10.381 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.134    0.134   10.381   10.381 <string>:1(<module>)
#      1    9.348    9.348   10.247   10.247 HW_4_task_2.py:18(sieve_)
#      1    0.786    0.786    0.786    0.786 HW_4_task_2.py:20(<listcomp>)
#      1    0.000    0.000   10.381   10.381 {built-in method builtins.exec}
# 1270607    0.114    0.000    0.114    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Второй — без использования «Решета Эратосфена»
# попробовала реализовать перебор делителей


def simple_num(n):
    count_simple_num = 0
    next_num = 2
    while count_simple_num < n:
        spam = 0
        for i in range(2, int(next_num ** 0.5) + 1):
            if next_num % i == 0:
                spam += 1
        if spam == 0:
            count_simple_num += 1
        if count_simple_num < n:
            next_num += 1

    return next_num


print(timeit('simple_num(1)', number=100, globals=globals()))      # 0.0000814000000000023
print(timeit('simple_num(10)', number=100, globals=globals()))      # 0.0022987000000000007
print(timeit('simple_num(100)', number=100, globals=globals()))      # 0.0751327
print(timeit('simple_num(1_000)', number=100, globals=globals()))      # 2.6801003999999997
print(timeit('simple_num(10_000)', number=100, globals=globals()))      # 175.7741049

run('simple_num(100)')
run('simple_num(1_000)')
run('simple_num(10_000)')

# 4 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 HW_4_task_2.py:87(simple_num)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       4 function calls in 0.027 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.027    0.027 <string>:1(<module>)
#      1    0.027    0.027    0.027    0.027 HW_4_task_2.py:87(simple_num)
#      1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       4 function calls in 1.757 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.757    1.757 <string>:1(<module>)
#      1    1.757    1.757    1.757    1.757 HW_4_task_2.py:87(simple_num)
#      1    0.000    0.000    1.757    1.757 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Первый вариант решения (с помощью алгоритма «Решето Эратосфена») имеет на мой взглят линейную сложность, 
т.е. O(n), т.к. при увеличении входящих данных n в 10 раз, время выполнения увеличивается примерно в 12 раз. 
Самое болбшое время в алгоритме занимает выполнение цикла. 
 
Второй вариант решения (без использования «Решета Эратосфена») имеет на мой взглят квадратичную сложность, 
т.е. O(n**2). Самое болбшое время в алгоритме занимает выполнение двух циклов.

Вывод: у «Эратосфена» получилось лучше) Первый вариант оптимальнее. 
"""
