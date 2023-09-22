# Проверка кода
# На вход подаётся одна строка с кодом программы, нужно проверить правильность расстановки парных скобок.
# Возможные пары скобок: [], {}, ().
# Кроме скобок в строке могут содержаться цифры, символы английского алфавита, знаки препинания.
# Например, строка 'def set(n):' должна признаваться корректной, а строка 'x = (f]' - некорректной.
# Если парные скобки расставлены в коде корректно, то на выход подайте одну строку Success, иначе Not Success.
# Эту задачу следует решить с использованием структуры данных stack.
# Если на Python, то с использованием методов списка append и pop.
# Sample Input 1:
# ()
# Sample Output 1:
# Success
# Sample Input 2:
# (){}[]
# Sample Output 2:
# Success
# Sample Input 3:
# ({[]})
# Sample Output 3:
# Success
# Sample Input 4:
# e = [i for i in range(5])
# Sample Output 4:
# Not Success

string = input()


def check_brackets(data: str) -> str:
    """Проверка корректно ли расставлены скобки в коде"""
    stack = []

    for char in data:  # проход по всем данным
        if char in "([{":  # если скобка открывающая добавляем в стек
            stack.append(char)  # добавляем в стек скобку
        elif char in "}])":  # если скобка закрывающая
            if not stack or is_matching_brackets(stack.pop(), char):
                # если стек пуст, а у нас еще есть закрывающая скобка или
                # открывающаяся скобка != закрывающая скобка то возвращаем "Not Success"
                return "Not Success"
    return "Not Success" if stack else "Success"


def is_matching_brackets(open_bracket: str, close_bracket: str) -> bool:
    """Если скобки равны вернем False иначе True"""
    brackets = {'(': ')', '[': ']', '{': '}'}
    return brackets.get(open_bracket) != close_bracket


print(check_brackets(string))
