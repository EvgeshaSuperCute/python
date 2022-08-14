from PyQt5 import QtWidgets as qw
from PyQt5.QtWidgets import QApplication as qApp, QMainWindow as qmWin
import sys
import psycopg2
from psycopg2 import Error


def App():
    app = qApp(sys.argv)
    win = qmWin()

    win.setWindowTitle("Test")
    win.setGeometry(500, 300, 500, 500)

    win.show()

    sys.exit(app.exec_())


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

def get_data(con):
    cur = con.cursor()
    cur.execute('SELECT id, name, second_name, phone_number from "Person"')

    rows = cur.fetchall()
    for row in rows:
        print("id =", row[0])
        print("name =", row[1])
        print("second_name =", row[2])
        print("phone_namber =", row[3], "\n")

    cur.close()
    print("Operation done successfully")


def main():
    connect = db_connect()
    get_data(connect)

    close_connection(connect)

    # App()


#----------------------Main Part---------------------


if __name__ == "__main__":
    main()