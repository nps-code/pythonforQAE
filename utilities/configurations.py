import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read(r'D:\1. Naresh\1. My Learning\0. Code_Repositories\learn_python\utilities\properties.ini')
    return config


db_credentials = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
}


def get_connection():
    try:
        database_connection = mysql.connector.connect(** db_credentials)
        if database_connection.is_connected():
            print("Database connection is successful.")
        return database_connection
    except Error as Ex:
        print(Ex)



