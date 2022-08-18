import psycopg2
from psycopg2 import Error


def db_connect():
    try:
        # Подключение к существующей базе данных
        con = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="2825",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="AccountBook")

        # Курсор для выполнения операций с базой данных
        cursor = con.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(con.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        return con

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if cursor:
            cursor.close()


def close_connection(con):
    if con:
        con.close()
        print("Соединение с PostgreSQL закрыто")