import sqlalchemy
from sqlalchemy.orm import sessionmaker

import sqlalchemy_tables


engine = sqlalchemy.create_engine("postgresql+psycopg2://sanch:vektor1302@localhost:5432/stepik")
"""
sqlalchemy.create_engine: Это функция из библиотеки SQLAlchemy, которая создаёт и возвращает
объект Engine. Engine - это интерфейс для взаимодействия с базой данных, предоставляющий
множество методов для выполнения SQL-запросов и управления соединениями с базой данных.
"""

tables.Base.metadata.create_all(engine)
"""
metadata - это объект, связанный с базовым классом, который содержит метаданные, такие как 
определения таблиц и другие параметры схемы. Метод create_all - это метод metadata объекта, 
который создает все таблицы, определенные в метаданных, в базе данных. Он принимает в качестве 
аргумента объект Engine (engine), с которым будет установлено соединение для выполнения 
SQL-запросов.
"""

Session = sessionmaker(bind=engine)
"""
Аргумент bind указывает, с каким движком (engine) базы данных будет связана сессия. engine в 
данном случае — это объект SQLAlchemy, представляющий подключение к базе данных. Сессия будет 
использовать этот движок для выполнения операций с базой данных. sessionmaker: Это фабричная 
функция, предоставляемая SQLAlchemy. Она создает новые экземпляры Session для работы с базой 
данныx.
"""

connection = Session()  #  создает новый объект сессии SQLAlchemy
"""
Session здесь представляет собой класс, созданный с использованием sessionmaker для работы с базой
данных. Когда мы вызываем Session(), мы создаем новый экземпляр сессии.
connection = ...: Эта строка создает переменную connection и присваивает ей новый экземпляр сессии. 
Обычно название connection может быть введено, чтобы дать понять, что это связано с подключением 
к базе данных. Однако, стоит отметить, что сессии SQLAlchemy не представляют прямого подключения к 
базе данных, они предоставляют интерфейс для управления транзакциями и выполнения запросов.
"""

# res = connection.execute(sqlalchemy.text("select * from Users"))
# print(res.fetchall())
# connection.close()


# new_good = tables.MyGoods("Apple", 1000, 10)  #  создается новый экземпляр объекта класса MyGoods
# connection.add(new_good)  #  метод add добавляет объект в текущую сессию SQLAlchemy.
# connection.commit()  # Фиксация изменений в базе данных
# connection.close()  # Закрыть соединение с базой данных


goods = connection.query(tables.MyGoods).all()
for i in goods:
    print(i)

