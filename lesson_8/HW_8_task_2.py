"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import collections

a = 'beep boop beer!'
my_coll = collections.Counter(a)
b = list(my_coll.most_common())
b.reverse()

while len(b) > 1:

    # беру 2 крайних элемента с самым малым весом

    left = b.pop(0)
    right = b.pop(0)
    weight = left[-1] + right[-1]

    # левая часть с 0

    if len(left) == 2:
        left_node = [[left[0], '0']]
    if len(left) > 2:
        left_node = []
        for i in range(len(left) - 1):
            spam = []
            spam.append(left[i][0])
            spam.append('0' + left[i][1])
            left_node.append(spam)

    # правая часть с 1

    if len(right) == 2:
        right_node = [[right[0], '1']]
    if len(right) > 2:
        right_node = []
        for i in range(len(right) - 1):
            spam = []
            spam.append(right[i][0])
            spam.append('1' + right[i][1])
            right_node.append(spam)

    # объединяю в новый узел

    node = []
    for i in left_node:
        node.append(i)
    for i in right_node:
        node.append(i)
    node.append(weight)

    # вставляю в лист

    if len(b) == 0:
        pos = 0
    for i in range(1, len(b) + 1):
        if b[i-1][-1] >= weight:
            pos = i
            break
        if b[i-1][-1] < weight and i == len(b):
            pos = len(b)
            break
    b.insert(pos, node)

my_dict = {}
for i in b:
    i.pop()
    for j in i:
        my_dict[j[0]] = j[1]

code_str = []
for i in a:
    code_str.append(my_dict[i])

print(f'словарь {my_dict}')
print(f"Строка {a} в закодированном виде: {''.join(code_str)}")

# вывод:
# словарь {'b': '00', 'e': '01', ' ': '100', 'p': '101', 'o': '110', '!': '1110', 'r': '1111'}
# Строка beep boop beer! в закодированном виде: 0001011011000011011010110000010111111110
