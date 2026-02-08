"""
Подвиг 8. С помощью функции namedtuple сформируйте именованный кортеж Dress со следующим
набором полей (порядок важен):

model - модель платья (строка);
color - цвет платья (строка);
size - размер платья (целое число).
В программе реализовано считывание данных и сохранение их в виде двумерного списка data_rows:

import sys

# считывание списка из входного потока
data_rows = [[f(x) for f, x in zip((str, str, int), row.split())]
             for row in map(str.strip, sys.stdin.readlines())]

Формат списка data_rows имеет следующий вид (пример):

[['летнее', 'red', 10], ['зимнее', 'gray', 8], ...]

На основе списка data_rows сформируйте одномерный список db_rows из именованных кортежей Dress
с соответствующими данными. Порядок данных в db_rows должен совпадать с порядком исходных данных
data_rows.

P.S. На экран ничего выводить не нужно.
"""

from collections import namedtuple
import sys

# считывание списка из входного потока
# список data_rows в программе не менять
data_rows = [[f(x) for f, x in zip((str, str, int), row.split())]
             for row in map(str.strip, sys.stdin.readlines())]

# здесь продолжайте программу
Dress = namedtuple("Dress", "model color size")
db_rows = [Dress(*d) for d in data_rows]
