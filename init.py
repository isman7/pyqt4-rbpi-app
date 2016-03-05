# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(250, 250, 500, 300)
        self.setWindowTitle('Tutorial PyQt4')
        self.home()
    
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_app)
        self.showFullScreen()
        
    def close_app(self):
        print("Adeu")
        sys.exit()



def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit()

run()