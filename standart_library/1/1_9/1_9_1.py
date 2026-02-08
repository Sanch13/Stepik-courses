""""""
"""
Подвиг 6. В программе определены два следующих словаря с наборами цветов:

colors = {'black': 0, 'white': 255, 'gray': 127}
palitra = {'red': 45, 'yellow': 100, 'white': 255}
                  
Необходимо с помощью класса ChainMap создать их объединенное представление all_colors в порядке
 colors, palitra. И выполнить с объектом all_colors следующие действия:

поменять местами словари colors и palitra между собой;
добавить в начало объекта all_colors цвета (в виде отдельного, независимого словаря): 'blue'=74, 'pink'=10;
сформировать новый объект my_colors класса ChainMap путем отбора ключей 'white', 'red', 'yellow', 'pink' и их значений из объекта all_colors.
P.S. На экран ничего выводить не нужно.
"""
from collections import ChainMap

colors = {'black': 0, 'white': 255, 'gray': 127}
palitra = {'red': 45, 'yellow': 100, 'white': 255}

# здесь продолжайте программу

all_colors = ChainMap(colors, palitra)
all_colors.maps.reverse()
all_colors = all_colors.new_child({'blue': 74, 'pink': 10})
my_colors = ChainMap({k:v for k, v in all_colors.items() if k in ('white', 'red', 'yellow', 'pink')})

print(all_colors)
print(my_colors)


