import pymongo
"""pymongo - это библиотека для работы с MongoDB на языке Python"""

from bson.objectid import ObjectId
"""Если нам требуется обратиться к элементу по id, то ObjectId надо привести в правильный тип, 
используя класс ObjectId модуля bson"""

client = pymongo.MongoClient("mongodb://localhost:27017/")
"""
переменная client будет представлять собой объект клиента MongoDB. С его помощью вы можете
устанавливать соединение с базой данных, выполнять запросы, получать коллекции и многое другое
MongoClient - это класс, предоставляемый PyMongo для создания подключения к серверу 
MongoDB. Он принимает URI (Uniform Resource Identifier) в качестве аргумента, 
который указывает, где и как установлен MongoDB. 
mongodb://localhost:27017/" - это URI, который определяет местоположение MongoDB-сервера. 
В данном случае:
    mongodb:// - указывает, что используется протокол MongoDB.
    localhost - это хост (в данном случае, сервер MongoDB работает на том же компьютере, 
    где выполняется код).
    27017 - это порт, на котором слушает MongoDB. По умолчанию MongoDB использует порт 27017.
"""

db = client["new_base"]
collection = db["myCollection"]
query = {"name": "John"}
results = collection.find(query)

collection.insert_one({"name": "Alex", "age": 15})
for result in results:
    print(result)  # {'_id': ObjectId('65955f215eca5cc94db6cf97'), 'name': 'John', 'age': 30}

res = collection.find({"_id": ObjectId("65955f215eca5cc94db6cf97")})
print(list(res))  # [{'_id': ObjectId('65955f215eca5cc94db6cf97'), 'name': 'John', 'age': 30}]
