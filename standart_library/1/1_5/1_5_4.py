"""
Подвиг 9. С помощью функции namedtuple сформируйте именованный кортеж StudentMarks со следующим
набором полей (порядок важен):

fio - ФИО студента (строка);
mark_python - оценка за Python;
mark_math - оценка по математике;
mark_phis - оценка по физике.
На основе входных данных:

row_data1 = [f(x) for f, x in zip((str, int, int, int), input().split())]
row_data2 = [f(x) for f, x in zip((str, int, int, int), input().split())]


сформируйте две записи st_mark1 и st_mark2, как объекты класса StudentMarks. Выполните с
полученными именованными кортежами следующие действия:

сформируйте обычный кортеж marks, состоящий только из оценок первого st_mark1 и второго st_mark2
студентов (порядок важен);
определите количество троек в кортеже st_mark1 и сохраните результат в переменной mark_three.
P.S. На экран ничего выводить не нужно."""

from collections import namedtuple

# значения списков row_data1 и row_data2 в программе не менять
row_data1 = [f(x) for f, x in zip((str, int, int, int), input().split())]
row_data2 = [f(x) for f, x in zip((str, int, int, int), input().split())]

# здесь продолжайте программу
StudentMarks = namedtuple("StudentMarks", "fio mark_python mark_math mark_phis")

st_mark1 = StudentMarks(*row_data1)
st_mark2 = StudentMarks(*row_data2)
mark1 = tuple(m for m in st_mark1 if isinstance(m, int))
mark2 = tuple(m for m in st_mark2 if isinstance(m, int))
marks = mark1 + mark2
mark_three = len([el for el in mark1 if el == 3])
mark_three1 = st_mark1.count(3)
