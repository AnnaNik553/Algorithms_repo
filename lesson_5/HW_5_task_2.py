"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
from collections import deque

# работает только с положительными числами
# 1 вариант - перевод чисел из 16 в 10, сложение, умножение, веревод в 16

hex_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def hex_in_ten(num):
    b = defaultdict(str)
    for j, char in enumerate(num):
        b[j] = char
    n = 1
    for char in b.keys():
        b[char] = hex_[b[char]] * (16 ** (len(b) - n))
        n += 1
    num_ten = sum(b.values())
    return num_ten


def ten_in_hex(num):
    if num == 0:
        return '0'
    hex_new = deque()
    while num > 0:
        ost = str(num % 16)
        num = num // 16
        hex_new.appendleft(hex_[ost])
    return hex_new


num_1 = input('Введите 1 положительное шестнадцатеричное число: ').upper()
num_2 = input('Введите 2 положительное шестнадцатеричное число: ').upper()
num_1_ten = hex_in_ten(num_1)
num_2_ten = hex_in_ten(num_2)
sum_ = num_1_ten + num_2_ten
mult_ = num_1_ten * num_2_ten
sum_hex = ten_in_hex(sum_)
mult_hex = ten_in_hex(mult_)

print('Сумма равна: ', end='')
if sum_hex[0] != '0':
    for i in sum_hex:
        print(i, end='')
else:
    print(0)
print('\nПроизведение равно: ', end='')
if mult_hex[0] != '0':
    for i in mult_hex:
        print(i, end='')
else:
    print(0)
print('\n')

# 2 вариант - только сложение

hex_out = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_in = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
          10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def num_int(num):
    num_in_int = deque()
    for char in num:
        num_in_int.append(hex_out[char])
    return num_in_int


def sum_int(num_int_1, num_int_2):
    if len(num_int_1) > len(num_int_2):
        for i in range(len(num_int_1) - len(num_int_2)):
            num_int_2.appendleft(0)
    elif len(num_int_2) > len(num_int_1):
        for i in range(len(num_int_2) - len(num_int_1)):
            num_int_1.appendleft(0)
    spam_sum = deque()
    for i in range(len(num_int_1)):
        spam_sum.appendleft(num_int_1[i] + num_int_2[i])
    sum_numbers = deque()
    p = 0
    for i in range(len(spam_sum)):
        if spam_sum[i] + p > 15:
            sum_numbers.appendleft(spam_sum[i] + p - 16)
            p = 1
        else:
            sum_numbers.appendleft(spam_sum[i] + p)
            p = 0
    if p == 1:
        sum_numbers.appendleft(p)
    return sum_numbers


def num_hex(num):
    sum_hex = deque()
    for i in num:
        sum_hex.append(hex_in[i])
    return sum_hex


n_1 = input('Введите 1 положительное шестнадцатеричное число: ').upper()
n_2 = input('Введите 2 положительное шестнадцатеричное число: ').upper()
n_int_1 = num_int(n_1)
n_int_2 = num_int(n_2)
sum_ = sum_int(n_int_1, n_int_2)
sum_new = num_hex(sum_)
print('Сумма равна: ', end='')
for i in sum_new:
    print(i, end='')
