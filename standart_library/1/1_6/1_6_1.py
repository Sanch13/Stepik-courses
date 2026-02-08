"""
Подвиг 4. Необходимо список прочитанных целых чисел:

digits = list(map(int, input().split()))

разделить на четные и нечетные. Для этого с помощью словаря defaultdict по ключу "even"
сформировать список из четных чисел digits, а по ключу "odd" - список из нечетных чисел digits.
На результирующий словарь defaultdict должна ссылаться переменная digit_groups.

Выведите по порядку на экран в одну строчку через пробел все выделенные нечетные числа по ключу "odd".
"""
from collections import defaultdict

digits = list(map(int, input().split()))

# здесь продолжайте программу
digit_groups = defaultdict(list)

[digit_groups[('even', 'odd')[i % 2]].append(i) for i in digits]

print(*digit_groups["odd"])
