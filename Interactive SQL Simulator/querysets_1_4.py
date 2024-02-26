# table book : [book_id, title, author, price, amount]

# 1.4.0 Вывести информацию (автора, название и цену) о  книгах, цены которых меньше или равны
# средней цене книг на складе. Информацию вывести в отсортированном по убыванию цены виде.
# Среднее вычислить как среднее по цене книги.
# query = """
# SELECT author, title, price
#   FROM book
#  WHERE price <= (SELECT AVG(price) FROM book)
#  ORDER BY price DESC;
# """

# 1.4.1 Вывести информацию (автора, название и цену) о тех книгах, цены которых превышают
# минимальную цену книги на складе не более чем на 150 рублей в отсортированном по возрастанию
# цены виде.
# query = """
# SELECT author, title, price
#   FROM book
#  WHERE price <= ((SELECT MIN(price) FROM book) + 150)
#  ORDER BY price ASC;
# """

# 1.4.2 Вывести информацию (автора, книгу и количество) о тех книгах, количество экземпляров
# которых в таблице book не дублируется.
# query = """
# SELECT author, title, amount
#   FROM book
#  WHERE amount IN (SELECT amount FROM book GROUP BY amount HAVING COUNT(amount) = 1);
# """

# 1.4.3 Вывести информацию о книгах(автор, название, цена), цена которых меньше самой большой из
# минимальных цен, вычисленных для каждого автора.
# query = """
# SELECT author, title, price
#   FROM book
#  WHERE price < ANY(SELECT MIN(price) FROM book GROUP BY author);
# """

# 1.4.4 Посчитать сколько и каких экземпляров книг нужно заказать поставщикам, чтобы на складе
# стало одинаковое количество экземпляров каждой книги, равное значению самого большего количества
# экземпляров одной книги на складе. Вывести название книги, ее автора, текущее количество
# экземпляров на складе и количество заказываемых экземпляров книг. Последнему столбцу присвоить
# имя Заказ. В результат не включать книги, которые заказывать не нужно.
# query = """
# SELECT title, author, amount, ((SELECT MAX(amount) FROM book) - amount) AS Заказ
#   FROM book
#  WHERE amount < ANY(SELECT MAX(amount) FROM book);
# """
# ROUND(SUM(price * amount), 2) SELECT title, author, price, amount,
#        (SELECT ROUND((SUM(price) / amount) * 100, 2) FROM book) AS income_percent
#   FROM book

# 1.4.5 при продаже всех книг, какая книга принесет больше всего выручки, в процентах.
# query = """
# SELECT author, title, price, amount,
#        (
#        ROUND(amount * price / (SELECT SUM(price * amount ) FROM book) * 100, 2)
#        ) AS income_percent
#  FROM book
# ORDER BY income_percent DESC;
# """
