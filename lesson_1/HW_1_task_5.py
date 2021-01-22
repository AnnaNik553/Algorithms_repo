"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('Введите две буквы алфавита от a до z')

a = input('Первая буква ').lower()
b = input('Вторая буква ').lower()
a_pos = alphabet.index(a)
b_pos = alphabet.index(b)
print(f'Буква "{a}" - {a_pos + 1} по счету в алфавите')
print(f'Буква "{b}" - {b_pos + 1} по счету в алфавите')

if a_pos > b_pos:
    bet_a_b = a_pos - b_pos - 1
    print(f'Между ними находится {bet_a_b} букв(ы)')
elif a_pos < b_pos:
    bet_a_b = b_pos - a_pos - 1
    print(f'Между ними находится {bet_a_b} букв(ы)')
else:
    print('Введена одна и та же буква')
