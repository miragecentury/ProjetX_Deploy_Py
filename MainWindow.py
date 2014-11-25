__author__ = 'victorien.vanroye@gmail.com'

from PySide import QtGui
from PySide import QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
       #QWidget Configuration
        self.resize(800, 600)
        self.setWindowTitle("Serial Terminal")
        self.setWindowIcon(QtGui.QIcon("supertux.png"))

        #Center Window : Thanx StackOverflow
        self.move(QtGui.QApplication.desktop().screen().rect().center()-self.rect().center())

        #Change Background Color
        p = self.palette()
        p.setBrush(self.backgroundRole(), p.dark())
        myColor = QtGui.QColor()
        myColor.setRgb(50, 50, 50)
        p.setColor(self.backgroundRole(), myColor)
        self.setPalette(p)
        self.statusBar().showMessage("Ready")