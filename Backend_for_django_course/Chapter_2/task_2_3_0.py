# Напишите функцию, в аргументы которой приходят два целых числа.
# Функция должна вернуть сумму этих чисел.
# # Также, напишите функцию декоратор, которая перед выполнением первой функции проверят
# есть ли среди этих чисел отрицательное число и выводит "YES", если такое число есть.
# Sample Input:
# 8 11
# Sample Output:
# 19

def decorator(func):
    def wrapper(a, b):
        if any(el < 0 for el in (a, b)):
            print("YES")
        return func(a, b)

    return wrapper


@decorator
def main(a, b):
    return a + b


x, y = [int(x) for x in input().split()]
print(main(x, y))
