"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

import hashlib


def count_str(a):
    my_hash = set()
    n = 1
    for i in range(len(a) - 1):
        for j in range(len(a)):
            my_hash.add(hashlib.sha1((a[j:j + n]).encode('utf-8')).hexdigest())
        n += 1
    return len(my_hash)


print(f'Количество подстрок равно {count_str(input(f"Введите строку: "))}')
