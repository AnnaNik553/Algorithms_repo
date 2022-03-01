"""
https://drive.google.com/file/d/1IiMHisBumcd_CPftGPH0ITI4OrSEZJKN/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

print('Введите трехзначное число')
user_number = int(input('Число:  '))
a = user_number // 100
b = user_number % 100 // 10
c = user_number % 10
sum_number = a + b + c
multi_number = a * b * c
print(f'сумма цифр числа равна {sum_number}, произведение цифр числа равно {multi_number}')
