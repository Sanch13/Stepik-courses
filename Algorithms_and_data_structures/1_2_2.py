# Минимальное число
# Напишите программу, которая в последовательности натуральных чисел определяет минимальное число, оканчивающееся на 3.
# На вход программа получает:
# - в первой строке одно целое число N - количество чисел в последовательности;
# - в последующих N строках сами числа последовательности.
# В последовательности всегда имеется хотя бы одно число, оканчивающееся на 3.
# Количество чисел не превышает 1000. Введённые числа не превышают 30 000.
# Программа должна вывести одно число – минимальное число, оканчивающееся на 3.
# Для получения данных сначала считайте первую строку и извлеките число N, затем запустите цикл с N повторами и считайте N строк с данными для программы.
#
# Sample Input 1:
# 4
# 63
# 10
# 531
# 11
# Sample Output 1:
# 63
# Sample Input 2:
# 7
# 1
# 11
# 10
# 31
# 33
# 103
# 993
# Sample Output 2:
# 33


num = int(input())
seq = [input()for i in range(num)]
print(min([int(i) for i in seq if i[-1] == '3']))