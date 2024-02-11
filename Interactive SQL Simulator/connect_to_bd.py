import mysql.connector
from mysql.connector import Error

# host=os.getenv("HOST"),
# database=os.getenv("DATABASE"),
# user=os.getenv("USERNAME"),
# password=os.getenv("PASSWORD"),
config = {
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'mysql',
}

connection = mysql.connector.connect(**config)
# table_movie = """
# CREATE TABLE IF NOT EXISTS movies(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(100),
#     release_year YEAR(4),
#     genre VARCHAR(100)
# );
# """

add_book = (
    """INSERT INTO book
    (title, author, price, amount)
    VALUES (%s, %s, %s, %s)"""
)
# add_data = ("Мастер и Маргарита", "Булгаков М.А.", 670.99, 3)
# add_data = ("Белая гвардия", "Булгаков М.А.", 540.50, 5)
# add_data = ("Идиот", "Достоевский Ф.М.", 460.00, 10)
# add_data = ("Братья Карамазовы", "Достоевский Ф.М.", 799.01, 2)
# add_data = ("Стихотворения и поэмы", "Есенин С.А.", 650.00, 15)
# try:
#     if connection.is_connected():
#         cursor = connection.cursor()
#         cursor.execute(add_book, add_data)
#         connection.commit()

        # cursor.execute(table_movie)
    # cursor.execute("select @@version ")
    # version = cursor.fetchone()
    # if version:
    #     print('Running version: ', version)
    # else:
    #     print('Not connected.')
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     connection.close()

# fetchall() – возвращает число записей в виде упорядоченного списка;
# fetchmany(size) – возвращает число записей не более size;
# fetchone() – возвращает первую запись.

# query = """SELECT * FROM book"""
cursor = connection.cursor()
# cursor.execute(add_book, add_data)
# connection.commit()
results = cursor.fetchall()
# results = cursor.fetchone()
# print(type(results), results)
for row in results:
    print(row)
cursor.close()
connection.close()
