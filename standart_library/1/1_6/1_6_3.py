"""
Подвиг 6. В программе выполняется считывание данных по маркам машин и их ценам следующим образом:

data_cars = [(x.split('=')[0], float(x.split('=')[1])) for x in input().split()]

В результате формируется список вида (пример):

[('BMW', 1000.0), ('Lada', 500.0), ..., ('BMW', 1100.0), ...]

Используя словарь defaultdict, необходимо вычислить среднюю цену по каждой марке автомобиля и
результат представить в виде словаря car_price, ключами которого являются марки машин, а
значениями - соответствующие средние цены. Например:

{"BMW": 1050.0, "Lada": 474.3, ...}

P.S. На экран ничего выводить не нужно.
"""
from collections import defaultdict
from itertools import count

data_cars = [(x.split('=')[0], float(x.split('=')[1])) for x in input().split()]
# [('BMW', 1000.0), ('Lada', 500.0), ..., ('BMW', 1100.0), ...]
# здесь продолжайте программу
car_price, s, c = defaultdict(float), defaultdict(float), defaultdict(int)

for car, price in data_cars:
    s[car] += price
    c[car] += 1
    car_price[car] = s[car]/c[car]