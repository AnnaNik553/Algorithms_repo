"""
Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""


def revers(num, n=0):
    if num == 0:
        return n
    else:
        return revers(num // 10, n * 10 + num % 10)


user_num = int(input('Введите натуральное число: '))
while user_num % 10 == 0:
    user_num = user_num // 10
print(f'Обратное число  {revers(user_num)}')
