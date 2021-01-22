"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print('Введите три разных числа ')
a = int(input('Ведите a '))
b = int(input('Ведите b '))
c = int(input('Ведите c '))
if a < b < c or a > b > c:
    avg_number = b
elif a < c < b or a > c > b:
    avg_number = c
else:
    avg_number = a
print(f'Средним является число {avg_number}')
