# Ход конём
# Интеллектуалы племени «Тумба-Юмба» после охоты учатся играть в шахматы. На этой неделе они
# осваивают ход Конём.
# Напишите программу, которая будет проверять правильность хода Конём.
# На вход подаётся строка – это шахматная запись одного хода - начальной позиции фигуры и конечной
# позиции, например, так: D5-C7.
# На выход нужно вывести результат анализа записи хода: YES - если указанный ход верный,
# NO - если такой ход не по правилам, указанным для Коня.
# Гарантируется, что запись хода будет состоять из 5-ти символов, в середине будет «дефис»,
# буквы и цифры будут расположены на правильных местах и в разрешённом диапазоне для шахматной доски.
# Sample Input 1:
# D5-C7
# Sample Output 1:
# YES
# Sample Input 2:
# A1-C2
# Sample Output 2:
# YES
# Sample Input 3:
# A1-B2
# Sample Output 3:
# NO

step = input()

if (abs(ord(step[0]) - ord(step[3])) == 2 and abs(int(step[1]) - int(step[4])) == 1) or \
        (abs(ord(step[0]) - ord(step[3])) == 1 and abs(int(step[1]) - int(step[4])) == 2):
    print("YES")
else:
    print("NO")
