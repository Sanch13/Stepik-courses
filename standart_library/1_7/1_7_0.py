"""Подвиг 3. Объявите в программе словарь data типа OrderedDict и занесите в него следующие данные:

row_data = [_row.split('=') for _row in input().split()]

которые представлены в виде вложенных списков формата ключ-значение (пример):

[['idea', 'идея'], ['машина', 'car'], ['model', 'BMW'], ...]

Необходимо удалить первый ключ полученного словаря data и проверить, имеется ли в нем ключ "people".
Результирующее булево значение сохранить в переменной find_key (True - ключ найден,
False - ключ отсутствует).

Выведите на экран в одну строчку через пробел набор всех значений словаря data в порядке их следования.
"""

from collections import OrderedDict

row_data = [_row.split('=') for _row in input().split()]

# здесь продолжайте программу

data = OrderedDict(row_data)
data.popitem(last=False)
find_key = "people" in data
print(*data.values())
