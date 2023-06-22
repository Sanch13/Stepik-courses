# Равнобедренные треугольники
# Знайка иногда ведёт частные уроки по геометрии и ему нужно рисовать равнобедренные треугольники.
# Но это рутинная операция и Знайке совсем не хочется тратить на это своё время. Помогите ему и
# напишите соответствующую программу.
# На вход подаётся целое число N в диапазоне [1; 30].
# На выход по результатам работы программы на экран выводится равнобедренный треугольник
# по такому формату:
# N – это высота треугольника,
# основание треугольника параллельно вертикальной стороне экрана,
# остальные параметры смотрите по примерам:
# Sample Input 1:
# 1
# Sample Output 1:
# *
# Sample Input 2:
# 2
# Sample Output 2:
# *
# **
# *
# Sample Input 3:
# 3
# Sample Output 3:
# *
# **
# * *
# **
# *
# Sample Input 4:
# 4
# Sample Output 4:
# *
# **
# * *
# *  *
# * *
# **
# *

num = int(input())
base = num * 2 - 1

lst = [['*' if j == 0 else ' ' for j in range(num)] for i in range(base)]
count = 0
for i in range(len(lst)):
    if i <= num - 1:
        lst[i][count] = "*"
        count += 1
        if count == num:
            count -= 1
    else:
        count -= 1
        lst[i][count] = "*"

for i in range(base):
    for j in range(num):
        if lst[i][j] == ' ' and "*" not in lst[i][j:]:
            continue
        print(lst[i][j], end='')
    print()

