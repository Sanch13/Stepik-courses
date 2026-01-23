"""
Подвиг 4. В программе ниже формируется словарь со случайными ключами и значениями:

from collections import OrderedDict
import random

random.seed(1)

def gen_key_value(size=5):
    key = list("absdefghijkopqrstuvwzx0123456789")
    random.shuffle(key)
    return ("".join(key[:size]), random.randint(1, 1000))

data = OrderedDict(gen_key_value() for _ in range(7))
Необходимо удалить из словаря data первый элемент, а последний элемент переместить на первую позицию.
P.S. На экран ничего выводить не нужно.
"""

from collections import OrderedDict
import random

random.seed(1)

def gen_key_value(size=5):
    key = list("absdefghijkopqrstuvwzx0123456789")
    random.shuffle(key)
    return ("".join(key[:size]), random.randint(1, 1000))


data = OrderedDict(gen_key_value() for _ in range(7))
# здесь продолжайте программу
data.popitem(last=False)
data.move_to_end(key=list(data.keys())[-1], last=False)


