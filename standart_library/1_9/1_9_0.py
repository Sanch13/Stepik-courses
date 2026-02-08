""""""
"""
Подвиг 4. В программе определены два следующих словаря с настройками приложения и пользователя:

app_settings = {'name': 'myapp', 'permissions': ['update', 'get', 'view'], 'update': False}
user_settings = {'uid': 43649045456, 'notify': ['email', 'phone'], 'premium': True}

                  
Необходимо с помощью класса ChainMap создать их объединенное представление all_settings в порядке 
user_settings, app_settings. И выполнить с объектом all_settings следующие действия:

по ключу 'update' получить значение и сохранить его в переменной st_update;
проверить наличие ключа 'permissions' и полученное булево значение сохранить в переменной 
st_perm_exists (True - ключ присутствует; False - отсутствует);
в словаре user_settings по ключу 'notify' удалите элемент 'phone'; затем, прочитайте с помощью 
объекта all_settings по этому ключу 'notify' значение и результат сохраните в переменной st_notify.
P.S. На экран ничего выводить не нужно.
"""


from collections import ChainMap

app_settings = {'name': 'myapp', 'permissions': ['update', 'get', 'view'], 'update': False}
user_settings = {'uid': 43649045456, 'notify': ['email', 'phone'], 'premium': True}

# здесь продолжайте программу

all_settings = ChainMap(user_settings, app_settings)
st_update = all_settings["update"]
st_perm_exists = 'permissions' in all_settings
user_settings.get("notify").remove('phone')
st_notify = all_settings.get("notify")

print(all_settings)


