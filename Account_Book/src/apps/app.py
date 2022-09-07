import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from src.UI.mainUI import Ui_MainWindow



class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
