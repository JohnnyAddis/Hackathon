from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

class loadVISNDashboard(QtWidgets.QMainWindow):
    """Class that loads the Veeva Interactive Sales Navigator
    loads UI file: VISNDashboard.ui """

    def __init__(self):
        super(loadVISNDashboard,self).__init__()

        # loads the ui file
        uic.loadUi("VISNDashboard.ui", self)

app = QtWidgets.QApplication(sys.argv)

VISN = loadVISNDashboard()
VISN.show()
sys.exit(app.exec_())