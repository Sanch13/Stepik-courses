""""""
"""
Подвиг 6. Создайте в программе объект pr класса PrettyPrinter со следующими параметрами:

максимальная ширина вывода 50;
количество символов отступа 3;
максимальная глубина рекурсии 4.
Используя объект pr, сформируйте строку data_str для следующих данных:

lst = [(10, 20), {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]
                  
Также, используя объект pr, выведите данные lst на экран.
"""
from pprint import pprint, pformat, PrettyPrinter

lst = [(10, 20), {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]

# здесь продолжайте программу

pr = PrettyPrinter(indent=3, depth=4, width=50)
data_str = pr.pformat(lst)
pr.pprint(lst)

