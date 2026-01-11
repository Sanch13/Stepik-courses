"""
Подвиг 7. С помощью функции namedtuple сформируйте именованный кортеж Path со следующим набором
 полей (порядок важен):

frm - город отправления (строка);
to - город назначения (строка);
dist - длина пути (целое число).
На основе входных данных:

row_data = [f(x) for f, x in zip((str, str, int), input().split())]


сформируйте запись path, как объект класса Path. Выполните с кортежем path следующие действия:

сохраните в переменной city_to значение поля to именованного кортежа path;
сформируйте новый кортеж path_2, изменив в исходном кортеже path значение поля dist на 0.
P.S. На экран ничего выводить не нужно."""

from collections import namedtuple

row_data = [f(x) for f, x in zip((str, str, int), input().split())]

# здесь продолжайте программу

Path = namedtuple("Path", "frm to dist")
path = Path(*row_data)
city_to = path.to
path_2 = path._replace(dist=0)
