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
        btn.move(300, 300)
        
        color = QtGui.QColor(0,0,0)
        font_color = QtGui.QAction('Font bg color', self)
        font_color.triggered.connect(self.color_picker)
        self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(font_color)

        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        
        
        self.showFullScreen()
        
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        
    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
        
    def close_app(self):
        print("Adeu")
        sys.exit()



def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit()

run()