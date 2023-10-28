from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys
from mplwidget import MplWidget

class loadVISNDashboard(QtWidgets.QMainWindow):
    """Class that loads the Veeva Interactive Sales Navigator
    loads UI file: VISNDashboard.ui """

    def __init__(self):
        super(loadVISNDashboard,self).__init__()

        # loads the ui file
        uic.loadUi("VISNDashboard.ui", self)

        self.calendar = self.findChild(QtWidgets.QPushButton,"calendarButton")
        self.calendar.clicked.connect(self.displayCalendar)
        self.leads = self.findChild(QtWidgets.QPushButton, "leadsButton")
        self.leads.clicked.connect(self.displayLeads)
        


        

    def displayCalendar(self):
        """linked to calendar button, pulls up the interactive calendar feature """

    def displayLeads(self):
        """linked to leads button, pulls up the window containing a list of sales leads"""

app = QtWidgets.QApplication(sys.argv)

VISN = loadVISNDashboard()
VISN.show()
sys.exit(app.exec_())