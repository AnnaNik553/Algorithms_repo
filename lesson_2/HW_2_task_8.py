"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def find_digit(number, digit, count=0):
    if number == 0:
        return count
    elif number % 10 == digit:
        return find_digit(number // 10, digit, count + 1)
    else:
        return find_digit(number // 10, digit, count)


srch_num = int(input('Введите искомую цифру (0-9): '))
lot_num = int(input('Сколько чисел будете вводить? '))
count_num = 0
for i in range(lot_num):
    num = int(input(f'Введите число {i + 1} '))
    count_num += find_digit(num, srch_num)
print(f'Цифра {srch_num} встречается в числах {count_num} раз(а)')
