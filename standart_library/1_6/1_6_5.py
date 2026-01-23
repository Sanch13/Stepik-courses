"""
Подвиг 8. Сформируйте в программе словарь ul_abc типа defaultdict, который каждый новый ключ
 инициализирует очередным значением из строки

"abcdef"

Например, для пустого словаря ul_abc, при обращении к несуществующим ключам, получались бы следующие значения:

ul_abc['key1'] # 'a'
ul_abc['key2'] # 'b'
...
ul_abc['key6'] # 'f'
ul_abc['key7'] # 'a'


Обратите внимание, что при выборе всех значений из строки "abcdef", осуществляется возврат к
 ее началу и процесс выбора символов повторяется.
Для реализации этой логики объявите пользовательскую инициализирующую функцию для словаря defaultdict.
P.S. На экран ничего выводить не нужно, только определить словарь ul_abc.
"""
from collections import defaultdict


def df_init(idx=-1):
	s = "abcdef"
	length = len(s)
	def counter():
		nonlocal idx
		idx += 1
		return s[idx % length]

	return counter

# здесь продолжайте программу
ul_abc = defaultdict(df_init())

for i in range(20):
	ul_abc[i]
# x = ul_abc['x']
# y = ul_abc['y']
print(ul_abc)
