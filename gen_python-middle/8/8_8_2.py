"""
Вам доступна строка sentence. Используя генератор множеств, напишите программу, которая создает множество, содержащее
 уникальные слова (в нижнем регистре) строки sentence. Результат выведите на одной строке в алфавитном порядке,
 разделяя слова одним символом пробела.
Примечание 1. Считайте, что строка sentence уже объявлена в вашей программе, и вы имеете к ней доступ.
Примечание 2. Учтите, что знаки пунктуации :,.!?(); не относятся к словам.
"""

import string

sentence = 'Dying for the right cause is the most human thing we can do.'

unique_letters = {i.lower().strip(string.punctuation) for i in sentence.split()}
print(*sorted(unique_letters))


