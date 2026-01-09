"""
Подвиг 8. Объявите в программе перечисление FilterType типа StrEnum, содержащее следующие константы:

DRAFT = 'draft'
PUBLISHED = 'article published'
CLOSED = 'article closed'
ALL = 'all articles'

Объявите функцию с сигнатурой:

def get_articles(lst, flt:FilterType=FilterType.ALL)
которая из списка:

articles = [('Python', 'published'), ('Python ООП', 'published'), ('The Standard Library', 'draft'),
            ('C/C++', 'published'), ('Java', 'closed'), ('JavaScript', 'closed')]


будет выделять кортежи с соответствующим типом параметра flt. Например, следующий вызов функции:

res = get_articles(articles, FilterType.CLOSED)

должен вернуть список:

[('Java', 'closed'), ('JavaScript', 'closed')]

Если же указывается значение flt=FilterType.ALL, то возвращается весь переданный список.

Вызовите функцию get_articles для списка articles с параметром flt=FilterType.PUBLISHED. Результат сохраните в переменной art_res.

P.S. На экран ничего выводить не нужно.

"""

import enum


class FilterType(enum.StrEnum):
	DRAFT = 'draft'
	PUBLISHED = 'article published'
	CLOSED = 'article closed'
	ALL = 'all articles'


def get_articles(lst, flt: FilterType=FilterType.ALL) -> list:
	return lst if flt == FilterType.ALL else [el for el in lst if flt.split()[-1] in el[-1]]

if __name__ == '__main__':
	articles = [('Python', 'published'), ('Python ООП', 'published'),
	            ('The Standard Library', 'draft'), ('C/C++', 'published'), ('Java', 'closed'), ('JavaScript', 'closed')]

	res = get_articles(articles, FilterType.CLOSED)
	print(res)
	art_res = get_articles(articles, FilterType.PUBLISHED)
	print(art_res)
