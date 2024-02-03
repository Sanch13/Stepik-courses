import mysql.connector

from secrets import secret

config = {
    "user": secret.USER,
    "password": secret.PASSWORD,
    "host": secret.HOST,
    "database": secret.DATABASE
}


def connect_to_bd(config=config):
    connection = mysql.connector.connect(**config)
    return connection
