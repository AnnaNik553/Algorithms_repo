"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import Counter

n = int(input('Введите количество компаний '))
counter = Counter()
sum_ = 0
for i in range(n):
    corp = input(f'Введите название {i + 1} компании ')
    profit = []
    for j in range(4):
        profit.append(int(input(f'Введите прибыль за {j + 1} квартал ')))
    counter[corp] = profit
    sum_ += sum(counter[corp])
avg_profit = sum_ / n
print(f'Средняя прибыль равна: {avg_profit} \nПрибыль выше среднего у компаний:')
for key in counter:
    if sum(counter[key]) > avg_profit:
        print(key)
print(f'Прибыль ниже среднего у компаний:')
for key in counter:
    if sum(counter[key]) < avg_profit:
        print(key)
