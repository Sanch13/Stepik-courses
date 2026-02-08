""""""
"""
Подвиг 3. С помощью функции pprint() выведите на экран следующий список:

lst = [(10, 20), {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]
                  
с указанием следующих параметров:

максимальная ширина вывода 40;
максимальная глубина рекурсии 3.
"""

from pprint import pprint

lst = [(10, 20),
       {'Vertex': 1, 'links': [{'Vertex': 2, 'links': None}, {'Vertex': 3, 'links': None}]},
       {'Vertex': 10, 'links': [{'Vertex': 3, 'links': None}, {'Vertex': 4, 'links': None}]}]

# здесь продолжайте программу

pprint(lst, depth=3, width=40)