from pprint import pprint

from mysql.connector import Error

from conn_to_bd import connect_to_bd
from querysets import query


def get_data_from_db(query):
    try:
        connection = connect_to_bd()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Error as e:
        print("Error while executing query:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    result = get_data_from_db(query=query)
    pprint(result)
