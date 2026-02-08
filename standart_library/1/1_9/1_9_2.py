""""""
"""
Подвиг 7. На основе словаря:

app_settings = {'name': 'myapp', 'permissions': ['update', 'get', 'view'], 'update': False}
                  
создайте объект settings класса ChainMap. Затем, добавьте в объект settings обновление 
конфигурации, представленное следующим словарем:

update_app_settings = dict(x.split('=') for x in input().split())
                  
Конфигурацию settings следует обновить так, чтобы данные из словаря update_app_settings читались в первую очередь.
После этого выполните откат конфигурации до прежнего состояния и сформируйте ее в виде нового 
объекта prev_settings объекта ChainMap. При этом объект settings должен оставаться неизменным.
P.S. На экран ничего выводить не нужно.
"""
from collections import ChainMap

app_settings = {'name': 'myapp', 'permissions': ['update', 'get', 'view'], 'update': False}
update_app_settings = dict(x.split('=') for x in input().split())

# здесь продолжайте программу

settings = ChainMap(app_settings)
settings = settings.new_child(update_app_settings)
prev_settings = ChainMap(settings.maps[-1])

# Свойство parents возвращает новый ChainMap без первого (самого "верхнего") словаря
# Объект settings при этом остается неизменным
prev_settings = settings.parents
print(settings)
print(prev_settings)

