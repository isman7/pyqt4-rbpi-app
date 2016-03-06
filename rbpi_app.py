# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design_test.ui'
#
# Created: Sun Mar  6 16:29:16 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtGui, QtCore
from qt_design_test import Ui_MainWindow
import qtawesome as qta

class main_window(QtGui.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.quitButton.clicked.connect(self.close_app)
        
        # Get icons by name.
        fa_icon = qta.icon('fa.times', options=[{'scale_factor': 0.8,
                                                 'hover': 'fa.sign-out',
                                                 'active': 'fa.sign-out',
                                                 'color': 'white'}])
        self.ui.quitButton.setIcon(fa_icon)
        
#        asl_icon = qta.icon('ei.asl')
#        elusive_button = QtGui.QPushButton(asl_icon, 'Elusive Icons!')
    
    def close_app(self):
        print("Adeu")
        sys.exit()


import sys
def run():
    
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    mainWindow = main_window()
    mainWindow.showFullScreen()
    sys.exit()

run()