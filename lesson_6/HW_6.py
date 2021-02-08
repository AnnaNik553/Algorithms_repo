"""
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Microsoft Windows [Version 10.0.18363.1316] 64-разрядная

Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
from collections import Counter
import sys


def show_(obj):
    sum_ = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                sum_ += sys.getsizeof(key)
                sum_ += sys.getsizeof(value)
        elif not isinstance(obj, str):
            for item in obj:
                sum_ += sys.getsizeof(item)
    return sum_


# 1 вариант

def res(a, even=0, uneven=0):
    if a == 0:
        return even, uneven
    elif a % 2 == 0:
        return res(a // 10, even + 1, uneven)
    else:
        return res(a // 10, even, uneven + 1)


user_num = int(input('Введите натуральное число: '))
b, c = res(user_num)
print(f'В числе {b} четные(х) и {c} нечетные(х) цифр(ы)')
print(f'Использовано памяти {sys.getsizeof(user_num) + sys.getsizeof(b) + sys.getsizeof(c)} байт')


"""
Введите натуральное число: 123456
В числе 3 четные(х) и 3 нечетные(х) цифр(ы)
Использовано памяти 44 байт
"""


# 2 вариант

user_num = input('Введите натуральное число: ')
lst = list(map(int, user_num))
even = len([i for i in lst if i % 2 == 0])
uneven = len(lst) - even
print(f'В числе {even} четные(х) и {uneven} нечетные(х) цифр(ы)')
print(f'Использовано памяти {show_(user_num) + show_(lst) + show_(even) + show_(uneven)} байт')

"""
Введите натуральное число: 123456
В числе 3 четные(х) и 3 нечетные(х) цифр(ы)
Использовано памяти 219 байт
"""

# 3 вариант

num = Counter(input('Введите натуральное число: '))
even = num['0'] + num['2'] + num['4'] + num['6'] + num['8']
uneven = num['1'] + num['3'] + num['5'] + num['7'] + num['9']
print(f'В числе {even} четные(х) и {uneven} нечетные(х) цифр(ы)')
print(f'Использовано памяти {show_(num.keys()) + show_(num.values()) + show_(even) + show_(uneven)} байт')

"""
Введите натуральное число: 123456
В числе 3 четные(х) и 3 нечетные(х) цифр(ы)
Использовано памяти 308 байт
"""

# 4 вариант

num = input('Введите натуральное число: ')
even = 0
uneven = 0
for i in num:
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    if i in {'1', '3', '5', '7', '9'}:
        uneven += 1
    if i == num[-1]:
        size_i = sys.getsizeof(i)
print(f'В числе {even} четные(х) и {uneven} нечетные(х) цифр(ы)')
print(f'Использовано памяти {show_(num) + show_(even) + show_(uneven) + size_i} байт')

"""
Введите натуральное число: 123456
В числе 3 четные(х) и 3 нечетные(х) цифр(ы)
Использовано памяти 85 байт
"""

"""
1 вариант - 44 байт
2 вариант - 219 байт
3 вариант - 308 байт
4 вариант - 85 байт
Вывод:
Самым экономичным по памяти является вариант № 1 (с рекурсией).
Мне казалось, что рекурсия тратит много памяти.
Хотя я вероятно не все посчитала. 
Самым затратным оказался вариант № 3 (с Counter).
"""
