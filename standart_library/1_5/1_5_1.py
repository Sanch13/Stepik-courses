"""
Подвиг 5. Для хранения записей таблицы БД следующей структуры:

объявите в программе именованный кортеж Users с полями (порядок полей важен):

uid - уникальный идентификатор записи;
gender - пол игрока (1 - мужской, 2 - женский);
name - имя игрока;
level - достигнутый уровень в игре;
score - количество набранных очков.
На основе входных данных:

row_data = [f(x) for f, x in zip((int, int, str, int, int), input().split())]


сформируйте запись row1, как объект класса Users. Выведите на экран значения его полей в
порядке их следования каждое с новой строки (в конце строк пробелов быть не должно).
"""

from collections import namedtuple

row_data = [f(x) for f, x in zip((int, int, str, int, int), input().split())]

# здесь продолжайте программу
Users = namedtuple("Users", "uid gender name level score")

row1 = Users(*row_data)
for r in row1:
	print(r)


