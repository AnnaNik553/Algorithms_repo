"""
Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def res(a, even=0, uneven=0):
    if a == 0:
        return even, uneven
    elif a % 2 == 0:
        return res(a // 10, even + 1, uneven)
    else:
        return res(a // 10, even, uneven + 1)


user_num = int(input('Введите натуральное число: '))
b, c = res(user_num)
print(f'В числе {user_num} {b} четные(х) и {c} нечетные(х) цифр(ы)')
