"""
Подвиг 10. С помощью класса Counter выполните подсчет частоты встречаемости символов следующих двух строк:

psw1 = input() # строку psw1 в программе не менять
psw2 = input() # строку psw2 в программе не менять

Результаты сохраните в словарях psw1_cnt и psw2_cnt соответственно. Затем, в каждом словаре
psw1_cnt и psw2_cnt отбросьте по два наиболее частотных символа. После этого сформируйте третий
словарь psw_cnt, как результат объединения словарей psw1_cnt и psw2_cnt.

На основе словаря psw_cnt сгенерируйте пароль из уникальных символов (ключей), которые следует
записать в порядке возрастания их частоты встречаемости. Результат сохраните в переменной psw_mdf.

P.S. На экран ничего выводить не нужно.
"""
from collections import Counter

psw1 = input() # строку psw1 в программе не менять
psw2 = input() # строку psw2 в программе не менять

# здесь продолжайте программу
psw1_cnt = Counter(psw1)
psw2_cnt = Counter(psw2)
psw1_cnt = psw1_cnt - Counter(dict(psw1_cnt.most_common(2)))
psw2_cnt = psw2_cnt - Counter(dict(psw2_cnt.most_common(2)))
psw_cnt = psw1_cnt | psw2_cnt
psw_mdf = "".join(dict(psw_cnt).keys())[::-1]
print(psw_mdf)
