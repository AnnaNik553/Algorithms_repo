"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def sum_serial(n, el=1.0, sum_el=1.0):
    if n == 1:
        return sum_el
    else:
        el /= -2
        return sum_serial(n - 1, el, sum_el + el)


div_count = int(input('Введите количество элементов ряда: '))
print(f'Сумма элементов ряда равна {sum_serial(div_count)}')
