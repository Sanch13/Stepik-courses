# Шамбала
# Шаман племени «Тумба-Юмба» обладает особым даром – он умеет отгонять беду от посевов племени.
# Но для успешного камлания он должен в день начала посевов правильно сложить особенную фигуру,
# называемую Шамбалой, чтобы боги погоды были благосклонны к жителям племени. Как строится Шамбала
# посмотрите в прилагаемых к задаче примерах.
# В данной задаче нужно вывести на экран в символическом виде концентрические круги символами ‘X’
# и пробелами, количество которых зависят от номера N текущего дня.
# На вход подаётся одна строка с числом N [1, 30].
# На выход нужно подать несколько строк с изображением шамбалы.
# Sample Input 1:
# 1
# Sample Output 1:
# X
# Sample Input 2:
# 2
# Sample Output 2:
# XXX
# X X
# XXX
# Sample Input 3:
# 3
# Sample Output 3:
# XXXXX
# X   X
# X X X
# X   X
# XXXXX
# Sample Input 4:
# 4
# Sample Output 4:
# XXXXXXX
# X     X
# X XXX X
# X X X X
# X XXX X
# X     X
# XXXXXXX

num = int(input())

r = 2 * num - 1
s = 0
arr = [[' ' for _ in range(r)] for _ in range(r)]

while s < r:
    for col in range(s, r):
        for row in range(s, r):
            if col == s or row == s or col == r - 1 or row == r - 1:
                arr[col][row] = 'X'
    s += 2
    r -= 2

for i in range(2 * num - 1):
    for j in range(2 * num - 1):
        print(arr[i][j], end='')
    print()


