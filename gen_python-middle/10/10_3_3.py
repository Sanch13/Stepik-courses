"""
ам доступна строка text, содержащая слова в нижнем регистре, разделенные символом пробела. Напишите программу,
 которая выводит наиболее часто встречающееся слово строки text. Если таких слов несколько, должно быть выведено то,
 что меньше в лексикографическом порядке.

Примечание. Считайте, что строка text уже объявлена в вашей программе, и вы имеете к ней доступ.
"""

text = text = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# game

res = {}
max_count = 0
for word in text.split():
    res[word] = res.get(word, 0) + 1
    if res[word] > max_count:
        max_count = res[word]

print(min(word for word, count in res.items() if count == max_count))