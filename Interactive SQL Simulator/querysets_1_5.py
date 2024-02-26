# 1.5.0 Создать таблицу поставка (supply), которая имеет ту же структуру, что и таблиц book.
# Поле	Тип, описание
# supply_id	INT PRIMARY KEY AUTO_INCREMENT
# title	VARCHAR(50)
# author	VARCHAR(30)
# price	DECIMAL(8, 2)
# amount	INT
# query = """
# CREATE TABLE supply(
#     supply_id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(50),
#     author VARCHAR(30),
#     price DECIMAL(8, 2),
#     amount INT
# );
# """

# 1.5.1 Занесите в таблицу supply четыре записи, чтобы получилась следующая таблица:
# supply_id	title	author	price	amount
# 1	Лирика	Пастернак Б.Л.	518.99	2
# 2	Черный человек 	Есенин С.А.	570.20	6
# 3	Белая гвардия	Булгаков М.А.	540.50	7
# 4	Идиот	Достоевский Ф.М.	360.80	3
# query = """
# INSERT INTO supply(title, author, price, amount)
# VALUES ('Лирика', 'Пастернак Б.Л.', 518.99, 2),
#        ('Черный человек', 'Есенин С.А.', 570.20, 6),
#        ('Белая гвардия', 'Булгаков М.А.', 540.50, 7),
#        ('Идиот', 'Достоевский Ф.М.', 360.80, 3);
# """

# 1.5.2 Добавить из таблицы supply в таблицу book, все книги, кроме книг, написанных
# Булгаковым М.А. и Достоевским Ф.М.
# query = """
# INSERT INTO book(title, author, price, amount)
#      SELECT title, author, price, amount
#        FROM supply
#       WHERE author NOT IN ('Булгаков М.А.', 'Достоевский Ф.М.');
# """

# 1.5.3 Занести из таблицы supply в таблицу book только те книги, авторов которых нет в  book.
# query = """
# INSERT INTO book(title, author, price, amount)
#      SELECT title, author, price, amount
#        FROM supply
#       WHERE author NOT IN (SELECT DISTINCT author FROM book);
# """

# 1.5.4 Уменьшить на 10% цену тех книг в таблице book, количество которых принадлежит интервалу
# от 5 до 10, включая границы.
# query = """
# UPDATE book
#    SET price = 0.9 * price
#  WHERE amount BETWEEN 5 AND 10;
# """
