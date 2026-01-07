"""
Подвиг 6. В программе ниже объявлен класс перечисления FoldersTable с набором полей таблицы
и список из данных (записей таблицы) data:

from enum import Enum

class FoldersTable(Enum):
	ID = 0
	NAME = 1
	PRICE = 2
	WEIGHT = 3

data = [(1, 'Table', 1000, 1.5), (4, 'CPU', 34200, 0.1), (2, 'Camera', 23100, 0.5)]

Необходимо сформировать словарь d_data, в котором ключами будут являться названия полей
(констант) класса FoldersTable, а значениями списки с соответствующими им значениям. Например,
значением ключа ID должен быть список из идентификаторов [1, 4, 2] (первые элементы кортежей
из data). И так для всех четырех свойств.

P.S. На экран ничего выводить не нужно.
"""

from enum import Enum

class FoldersTable(Enum):
	ID = 0
	NAME = 1
	PRICE = 2
	WEIGHT = 3


data = [(1, 'Table', 1000, 1.5), (4, 'CPU', 34200, 0.1), (2, 'Camera', 23100, 0.5)]

# здесь продолжайте программу
d_data = {}
for item in FoldersTable:
	d_data.update({item.name: [el[item.value] for el in data]})
