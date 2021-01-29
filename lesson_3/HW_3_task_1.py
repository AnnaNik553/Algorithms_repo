"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

my_list = [i for i in range(2, 100)]
base_list = [i for i in range(2, 10)]
for i in base_list:
    count_mul = 0
    for j in my_list:
        if j % i == 0:
            count_mul += 1
    print(f'В диапазоне {count_mul} чисел(ла), кратных {i}')
