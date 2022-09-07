import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from apps.app import ExampleApp
from database.db_connect import db_connect, close_connection
import json


def get_data(con):
    cur = con.cursor()
    cur.execute('SELECT id, name, second_name, phone_number from "Person"')
    rows = cur.fetchall()

    request_result = {"RECORDS": []}

    for row in rows:
        request_result["RECORDS"].append({"id": row[0], "name": row[1], "second_name": row[2], "phone_number": row[3]})

    cur.close()
    print("Operation done successfully")
    return request_result


def set_data(con):
    cur = con.cursor()
    rows = []
    with open("../src/f_data/ExportJson.json", "r") as f:
        rows = json.load(f)
    print(json.dumps(rows, indent=2))

    i = 10
    for row in rows["RECORDS"]:
        print(row)
        i += 1
        request = """INSERT INTO "Person" VALUES(%s, %s, %s, %s)"""
        request_data = (row["id"]+str(i), row["name"], row["last_name"], row["phone_number"])
        cur.execute(request, request_data)

    con.commit()
    cur.close()
    print("Operation done successfully")
    return 0


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = ExampleApp()
    win.show()
    app.exec_()

    connect = db_connect()
    export = get_data(connect)
    # set_data(connect)

    with open("../src/f_data/request_result.json", "w") as f:
        json.dump(export, f, indent=2)
    print(json.dumps(export, indent=2))
    close_connection(connect)
    # App()


# ----------------------Main Part---------------------


if __name__ == "__main__":
    main()