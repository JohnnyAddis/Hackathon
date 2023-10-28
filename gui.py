from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
import sys

class Calendar(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calendar, self).__init__()
        loadUi("Calendar.ui", self)

app = QtWidgets.QApplication(sys.argv)
calendar = Calendar()
calendar.show()
sys.exit(app.exec())