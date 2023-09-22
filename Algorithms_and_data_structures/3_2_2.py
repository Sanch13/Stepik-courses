# Проверка кода - 2
# На вход подаётся одна строка с кодом программы, нужно проверить правильность расстановки парных скобок.
# Возможные пары скобок: [], {}, ().
# Кроме скобок в строке могут содержаться цифры, символы английского алфавита, знаки препинания, пробелы.
# Например, строка 'def set(n):' должна признаваться корректной, а строка 'x = (f]' - некорректной.
# Если парные скобки расставлены в коде корректно, то на выход подайте одну строку Success, а
# иначе на выход подайте индекс первого неправильного символа (счёт символов в строке идёт с нуля).
# Например, для строки 'x = (f]' на выход подайте 6.
# Обратите внимание на эти примеры:
# input
# foo(bar);
# foo(bar[i);
# foo(bar[i];
# foo(bar(i;
# output
# Success
# 9
# 3
# 7
# и внимательно изучите открытые ниже тесты.
# Если скобка открыта, но закрыта неправильной скобкой, то следует вывести индекс этой
# неправильной скобки - foo(bar[i);.
# Если скобка открыта, но незакрыта, то нужно выводить индекс именно этой скобки - foo(bar[i];.
# Если незакрытыми оказались несколько скобок, то нужно вывести индекс последней незакрытой
# скобки - foo(bar(i;.
# Эту задачу следует решить с использованием структуры данных stack.
# Если на Python, то с использованием методов списка append и pop.
# Sample Input 1:
# ()[()]{}
# Sample Output 1:
# Success
# Sample Input 2:
# ){}[]
# Sample Output 2:
# 0
# Sample Input 3:
# x = [0}
# Sample Output 3:
# 6
# Sample Input 4:
# e = [i for i in range(5])
# Sample Output 4:
# 23
# Sample Input 5:
# {{[()]]
# Sample Output 5:
# 6

string = input()
lst = []
d = {'(': [], '[': [], '{': []}


def check_brackets(data: str) -> str:
    """Проверка корректно ли расставлены скобки в коде"""
    stack = []
    b = {')': '(', ']': '[', '}': '{'}
    for ind, char in enumerate(data):  # проход по всем данным
        if char in "([{":  # если скобка открывающая добавляем в стек
            stack.append([ind, char])  # добавляем в стек скобку
            # print(stack)  # [[3, '('], [7, '[']]
        elif char in "}])":  # если скобка закрывающая
            i, el = stack.pop()
            # print(i, el)
            if not stack or is_matching_brackets(el, char):
                # если стек пуст, а у нас еще есть закрывающая скобка или
                # открывающаяся скобка != закрывающая скобка то возвращаем "Not Success"
                return ind
            print(stack, "stack")
            # d.pop(d.get(
            # print(data.rfind(b.get(char)))
            # print(d[b.get(char)])
            # d[b.get(char)] = d[b.get(char)][:-1]
    return stack[0][0] if stack else "Success"


def is_matching_brackets(open_bracket: str, close_bracket: str) -> bool:
    """Если скобки равны вернем False иначе True"""
    brackets = {'(': ')', '[': ']', '{': '}'}
    return brackets.get(open_bracket) != close_bracket


print(check_brackets(string))
# print(lst)

