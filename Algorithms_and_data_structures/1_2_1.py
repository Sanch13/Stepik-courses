# Любое чётное
# На вход подаётся список из n [1, 1000] целых чисел из диапазона [0, 1000], записанных в одну строку через пробел.
# На выход ваша программа должна вернуть любое чётное число из этого списка.
# Гарантируется, что в списке будет не менее одного чётного числа.
# Данные следует считывать из стандартного входного потока, например для Питона так:
# # исходную строку разбиваем по пробелам на список подстрок
# line = input()
# list_substrings = line.split()
# Ответ следует выводить в стандартный поток вывода, например для Питона так:
# print(result)
#
# Sample Input 1:
#
# 0 3 7 2 9 8 8 2 0 0
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# 7 7 1 4 7 6 4 1 5 4
# Sample Output 2:
#
# 4

from typing import List

list_substrings = input().split()


def find_first_odd(list_substrings: List[str]) -> int:
	for num in list_substrings:
		if int(num) % 2 == 0:
			return num


print(find_first_odd(list_substrings=list_substrings))