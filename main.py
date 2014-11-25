__author__ = 'Hades'

from MainWindow import MainWindow
from PySide import QtGui
from PySide import QtCore
import sys

app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
exit()
