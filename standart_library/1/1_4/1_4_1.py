"""
Подвиг 5. Объявите в программе перечисление FoodType типа IntEnum со следующим набором констант:

SEAFOOD = 1
MEATFOOD = 2
VEGETARIANFOOD = 3
Затем, объявите функцию с сигнатурой:

def get_menu(total, ms, t:FoodType=FoodType.MEATFOOD)
которая для словаря:

menus = {'SEAFOOD': [('Осьминог в соусе', 1430), ('Рыба жареная', 500), ('Морской окунь с картофелем', 2100)],
         'MEATFOOD': [('Котлета по Киевски', 800), ('Пельмени', 500), ('Манты', 1000)],
         'VEGETARIANFOOD': [('салат "Редиска"', 1200), ('капуста квашеная', 800), ('шуба без сельди', 600)]}

должна возвращать максимальный список из блюд, суммарная стоимость которых не превышает значения total. Например, следующий вызов функции:

res = get_menu(2200, menus, FoodType.SEAFOOD)

должен возвращать список:
[('Рыба жареная', 500), ('Осьминог в соусе', 1430)]

То есть, максимальное количество блюд, стоимость которых не превышает 2200.
Вызовите функцию get_menu с параметрами total=2500, ms=menus, t=FoodType.VEGETARIANFOOD и результат сохраните в переменной menu_res.

P.S. На экран ничего выводить не нужно.
"""

import enum


class FoodType(enum.IntEnum):
	SEAFOOD = 1
	MEATFOOD = 2
	VEGETARIANFOOD = 3


def get_menu(total, ms, t: FoodType = FoodType.MEATFOOD):
	lst_menu = sorted(ms[t.name], key=lambda x: x[-1])

	idx = 0
	for i, item in enumerate(lst_menu):
		price = item[-1]
		if total >= price:
			total -= price
			idx = i
		else:
			break
	return lst_menu[:idx + 1]

if __name__ == '__main__':
	menus = {'SEAFOOD': [('Осьминог в соусе', 1430), ('Рыба жареная', 500),
	                     ('Морской окунь с картофелем', 2100)],
	         'MEATFOOD': [('Котлета по Киевски', 800), ('Пельмени', 500), ('Манты', 1000)],
	         'VEGETARIANFOOD': [('салат "Редиска"', 1200), ('капуста квашеная', 800),
	                            ('шуба без сельди', 600)]}
	res = get_menu(2200, menus, FoodType.SEAFOOD)
	print(res)

	menu_res = res = get_menu(2500, menus, FoodType.VEGETARIANFOOD)
	print(menu_res)