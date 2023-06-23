# Напечатай цифру
# На вход подаётся цифра dig в диапазоне [0; 9].
# На выход нужно подать несколько строк - графический образ этой цифры из символов:
# Примеры вывода смотрите ниже...
# Пробелы за пределами напечатанного образа недопустимы...
# Sample Input 1:
# 0
# Sample Output 1:
# ##
# ##
# ##
# ##
# Sample Input 2:
# 1
# Sample Output 2:
# .#
# ##
# .#
# .#
# Sample Input 3:
# 2
# Sample Output 3:
# ##
# .#
# #.
# ##

d = {
    0: ['##', '##', '##', '##'],
    1: ['.#', '##', '.#', '.#'],
    2: ['##', '.#', '#.', '##'],
    3: ['##', '.#', '.#', '##'],
    4: ['##', '##', '.#', '.#'],
    5: ['##', '#.', '.#', '##'],
    6: ['.#', '#.', '##', '##'],
    7: ['##', '.#', '#.', '#.'],
    8: ['##', '..', '##', '##'],
    9: ['##', '##', '.#', '#.'],
}


num = int(input())
for v in d.get(num):
    print(v)


