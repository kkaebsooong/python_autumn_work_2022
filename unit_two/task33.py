# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

index = int(input('Введите число от 0 до 17:  '))

def exception_():
    text = 'Вы побелили в игре'
    try:
        print(text[index])
    except Exception:
        print('Введенный число находится вне заданного диапазона')

exception_()


massive = ['An', 'Peter', 'Simon', 'Gleb', 'Kai']
guest = input('Введите имя гостя: ')

def find_name():
    if guest in massive:
        print(guest)
    else:
        raise BaseException('Нет соответствий')

find_name()



import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="a197328456",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = 'create database postgres_db_test1'
    cursor.execute(sql_create_database)
except ConnectionResetError as error:
    print("Произошел разрыв соединения с сервером", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")