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
import qrcode
from PIL import ImageQt

class main_window(QtGui.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.quitButton.clicked.connect(self.close_app)
        self.ui.runButton.clicked.connect(self.create_qrcode)
        
        # Get icons by name.
        fa_exit = qta.icon('fa.times', options=[{'scale_factor': 0.8,
                                                 'hover': 'fa.sign-out',
                                                 'active': 'fa.sign-out',
                                                 'color': 'white'}])
        fa_cog = qta.icon('fa.cog', options=[{'scale_factor': 0.8,
                                                 'hover': 'fa.cogs',
                                                 'active': 'fa.cogs',
                                                 'color': 'white'}])
        fa_folder = qta.icon('fa.folder-o', options=[{'scale_factor': 0.8,
                                                 'hover': 'fa.folder-open-o',
                                                 'active': 'fa.folder-open-o',
                                                 'color': 'black'}])
        fa_floppy = qta.icon('fa.floppy-o', options=[{'scale_factor': 0.8,
                                                 'color': 'black'}])                                         
        self.ui.quitButton.setIcon(fa_exit)
        self.ui.saveButton.setIcon(fa_floppy)
        self.ui.runButton.setIcon(fa_cog)
        self.ui.loadButton.setIcon(fa_folder)
        
#        asl_icon = qta.icon('ei.asl')
#        elusive_button = QtGui.QPushButton(asl_icon, 'Elusive Icons!')
    def create_qrcode(self):
        qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=4,
            border=4,
        )
        qr.add_data('https://github.com/isman7/pyqt4-rbpi-app/blob/1acd121f862fa837008fbb3674145cb1292b44d6/qt_design_test.py')
        qr.make(fit=True)
        qr.print_ascii()
        img = qr.make_image()
        self.pix = QtGui.QPixmap.fromImage(ImageQt.ImageQt(img))
        self.ui.label.setPixmap(self.pix)
        


    
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