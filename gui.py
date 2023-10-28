from PyQt6 import QtWidgets
import PyQt6
#from PyQt6.QWidgets import QWidget
from PyQt6.uic import loadUi
import sys

class Calendar(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calendar, self).__init__()
        loadUi("Calendar.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
    
    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected: ", dateSelected)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = Calendar()
    calendar.show()
    sys.exit(app.exec())