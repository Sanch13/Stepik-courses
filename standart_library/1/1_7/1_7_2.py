"""
Подвиг 5. Объявите в программе словарь st_marks типа OrderedDict и занесите в него следующие данные:
row_data = [(_row.split('=')[0], tuple(map(int, _row.split('=')[1].split('-')))) for _row in input().split()]

которые представлены в виде вложенных кортежей формата ключ-значение (пример):

[('Sergey', (2, 3, 4, 2, 5, 3)), ('Masha', (5, 4, 5, 2, 3, 2)), ...]
Необходимо каждое значение словаря st_marks заменить словарем defaultdict, в котором ключи -
это уникальные оценки студента, а значение - количество их повторений. Например, кортеж (2, 3, 4, 2, 5, 3) должен заменяться словарем:
defaultdict(<func>, {2: 2, 3: 2, 4: 1, 5: 1})

P.S. На экран ничего выводить не нужно.
"""

from collections import OrderedDict, defaultdict

row_data = [(_row.split('=')[0], tuple(map(int, _row.split('=')[1].split('-')))) for _row in input().split()]

# здесь продолжайте программу
st_marks = OrderedDict()

def get_values(v):
	values = defaultdict(int)
	for i in v:
		values[i] += 1

	return values


for k, v in row_data:
	st_marks[k] = get_values(v)

print(st_marks)
