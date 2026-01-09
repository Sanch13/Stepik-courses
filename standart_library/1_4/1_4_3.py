"""
Подвиг 10. Перечисления типов IntEnum и StrEnum можно формировать динамически следующим образом:

import enum

Color = enum.IntEnum('Color', {'RED': 100, 'GREEN': 200, 'BLUE': 125})

Здесь создается класс с именем Color и атрибутами (константами): RED = 100, GREEN = 200, BLUE = 125. Эта команда полный аналог следующего класса:

class Color(enum.IntEnum):
    RED = 100
    GREEN = 200
    BLUE = 125

Используя динамический способ создания классов-перечислений, с помощью класса StrEnum создайте
перечисление DigitType, используя только уникальные имена полей следующего списка:

tp_lst = input().split()  # этот список в программе не менять

Имена констант формируйте заглавными буквами, а значения - строчными.
Порядок следования констант в классе DigitType может быть любым.

P.S. На экран ничего выводить не нужно.
"""

import enum

tp_lst = input().split()

d = {}
for el in tp_lst:
	d.setdefault(el.upper(), el.lower())

# {'RED': 100, 'GREEN': 200, 'BLUE': 125}
DigitType = enum.StrEnum('DigitType', d)

if __name__ == '__main__':
	for i in DigitType:
		print(f"{i.name} ==> {i.value}")
