"""
Подвиг 3. С помощью класса Enum создайте перечисление TypeBook со следующими элементами:

- константами:
DRAMA = 3
THRILLER = "thriller"
LOVESTORY = (0, 1, 2)

- методами:
get_default(cls) - метод класса (classmethod), возвращающий свойство LOVESTORY

Создайте переменную p_th, которая ссылается на свойство THRILLER класса TypeBook.
Выведите на экран в одну строчку через пробел имя свойства p_th и его значение.
"""

from enum import Enum


class TypeBook(Enum):
	DRAMA = 3
	THRILLER = "thriller"
	LOVESTORY = (0, 1, 2)

	@classmethod
	def get_default(cls):
		return cls.LOVESTORY


p_th = TypeBook.THRILLER
print(f"{p_th.name} {p_th.value}")

