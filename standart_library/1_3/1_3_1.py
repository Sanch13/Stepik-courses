"""
Подвиг 4. С помощью класса Enum создайте перечисление TypeDigit с набором следующих констант:
INT = 1
REAL = 2
COMPLEX = 3

Объявите функцию с сигнатурой:
def factory_digit(*args, t:TypeDigit=TypeDigit.REAL)
которая формирует и возвращает число переданного в параметр t типа:

для типа TypeDigit.INT первое значение из args функции factory_digit приводится к типу int;
для типа TypeDigit.REAL первое значение из args функции factory_digit приводится к типу float;
для типа TypeDigit.COMPLEX первые два значения в args функции factory_digit образуют
действительную и мнимую часть комплексного числа.

Вызовите функцию factory_digit с позиционными аргументами 4.3, 2.1 и типом
TypeDigit.COMPLEX для параметра t. Результат вызова функции сохраните в переменной cmp.

P.S. На экран ничего выводить не нужно.
"""

from enum import Enum


class TypeDigit(Enum):
	INT = 1
	REAL = 2
	COMPLEX = 3


def factory_digit(*args, t: TypeDigit = TypeDigit.REAL):
	if t == TypeDigit.INT:
		return int(args[0])

	elif t == TypeDigit.REAL:
		return float(args[0])

	elif t == TypeDigit.COMPLEX:
		return complex(float(args[0]), float(args[1]))


if __name__ == '__main__':
	cmp = factory_digit(4.3, 2.1, t=TypeDigit.COMPLEX)
	print(cmp)
