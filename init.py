# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(250, 250, 500, 300)
window.setWindowTitle('Tutorial PyQt4')


window.show()