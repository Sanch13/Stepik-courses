from tabulate import tabulate

from mysql.connector import Error

from conn_to_bd import connect_to_bd
from querysets_1_4 import query


def get_data_from_db(query):
    try:
        connection = connect_to_bd()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        headers = [column[0] for column in cursor.description] if data else []
        return headers, data
    except Error as e:
        print("Error while executing query:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    headers, result = get_data_from_db(query=query)
    table_data = [list(row) for row in result]
    if table_data:
        print(tabulate(tabular_data=table_data,
                       headers=headers,
                       tablefmt='fancy_outline'))
    else:
        print("No data")
