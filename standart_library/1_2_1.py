"""
Подвиг 6. В программе определены два множества:

s = set(map(int, input().split()))
fs = frozenset(map(int, input().split()))

Выполните с ними следующие действия (результатом каждого действия должно быть множество типа frozenset):

определите элементы, которые входят в множество s, но не входят в fs; результат сохраните в переменной res_1;
объедините элементы множеств s и fs; результат сохраните в переменной res_2;
определите общие элементы множеств s и fs; результат сохраните в переменной res_3;
определите элементы, которые уникальны для множеств s и fs (объединить и исключить общие значения); результат сохраните в переменной res_4.
P.S. На экран ничего выводить не нужно.
"""

# множества s и fs в программе не менять
s = set(map(int, input().split()))
fs = frozenset(map(int, input().split()))

# здесь продолжайте программу
res_1 = frozenset(s - fs)						    # fs - s # аналог fs.difference(s)
res_2 = frozenset(s.union(fs))  					# fs | s # аналог fs.union(s)
res_3 = frozenset(s.intersection(fs))				# fs & s # аналог fs.intersection(s)
res_4 = frozenset(s.symmetric_difference(fs))		# fs ^ s # аналог fs.symmetric_difference(s)

if __name__ == "__main__":
	print(res_1)
	print(res_2)
	print(res_3)
	print(res_4)


