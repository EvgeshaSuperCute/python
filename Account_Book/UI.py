from PyQt5 import QtWidgets as qw
from PyQt5.QtWidgets import QApplication as qApp, QMainWindow as qmWin
import sys


def App():
    app = qApp(sys.argv)
    win = qmWin()

    win.setWindowTitle("Test")
    win.setGeometry(500, 300, 500, 500)

    win.show()

    sys.exit(app.exec_())