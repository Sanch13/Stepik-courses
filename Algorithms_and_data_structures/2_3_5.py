# Код пифии
# Хакер Нео, не понимая своей миссии в Матрице, ищет встречи с Пифией.
# Личная встреча опасна, как и любое электронное сообщение, так как Нео уже давно попал под
# наблюдение Матрицы, и за ним охотится Агент Смит. Чтобы передавать сообщения, Пифия размещает
# их в сети, но адреса документов шифрует.
# Описание кода Пифии.
# Вы знаете, что каждый символ имеет свой порядковый номер в таблице символов, таким образом
# буквы можно заменить на их номера, а слова на последовательности целых чисел. Например,
# рассмотрим кодировку для имени Neo. Первая буква - N в таблице символов стоит на 78-ой позиции
# – это и есть её номер. Но Пифия пошла дальше и стала кодировать эти номера в шестнадцатеричной
# системе счисления, то есть нужно заменить
# 7810 на 4E16, так как 4E16 => 4*161 + 14*160 = 64 + 14 = 7810 Итак, если зашифровать имя
# Neo кодом Пифии, то получится такая последовательность: 4E656F, где каждые два последовательно
# записанных символа кодируют одну букву. Нео проводит дни в ожидании послания от Пифии –
# это будет адрес некоторого файла или сайта в сети. Однажды сообщение придёт и нужно будет
# оперативно его декодировать.
# Помогите Избранному - напишите программу для декодирования послания от Пифии.
# На вход подаётся одна зашифрованная строка.
# На выход подаёте одну расшифрованную строку.
# Sample Input 1:
# 68747470733A2F2F7777772E707974686F6E2E6F72672F646F776E6C6F6164732F
# Sample Output 1:
# https://www.python.org/downloads/
# Sample Input 2:
# 68747470733A2F2F6769746875622E636F6D2F
# Sample Output 2:
# https://github.com/

s = input()
print(bytes.fromhex(s).decode())
