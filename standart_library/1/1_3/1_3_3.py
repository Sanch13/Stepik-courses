"""
Подвиг 9. Перечисления можно формировать динамически с помощью мета-класса Enum следующим образом:

from enum import Enum

Version = Enum('Version', {'V1': 1, 'V2': 2})

Здесь создается класс с именем Version и атрибутами (константами): V1 = 1, V2 = 2.
Эта команда полный аналог следующего класса:

class Version(Enum):
    V1 = 1
    V2 = 2

Используя динамический способ создания классов-перечислений, создайте перечисление Goods с
набором уникальных полей (констант) следующего списка:

goods = ['Table', 'Monitor', 'Mouse', 'Keyboard', 'Table', 'CPU', 'GPU', 'Monitor']

Значениями констант должны быть их порядковые номера, начинает с 1, то есть, Table=1, Monitor=2 и
так далее. Обратите внимание, что из списка goods нужно выбрать только первые уникальные строки,
остальные не использовать.

P.S. На экран ничего выводить не нужно.
"""

from enum import Enum

goods = ['Table', 'Monitor', 'Mouse', 'Keyboard', 'Table', 'CPU', 'GPU', 'Monitor']

# здесь продолжайте программу
d = {}
count = 1
for item in goods:
	if item not in d:
		d[item] = count
		count += 1

Goods = Enum('Goods', d)

# Goods = {d.setdefault(item.upper(), i) for i, item in enumerate(goods, 1)}
# print(Goods)