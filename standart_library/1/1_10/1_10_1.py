""""""
"""
Подвиг 4. С помощью функции pprint() выведите на экран следующий список:

lst = [(10, 20), {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]

                  
с указанием следующих параметров:

максимальная ширина вывода 30;
количество символов отступа 5;
максимальная глубина рекурсии 2.
"""

from pprint import pprint

lst = [(10, 20),
       {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]

# здесь продолжайте программу

pprint(lst, indent=5, depth=2, width=30)