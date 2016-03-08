# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from qt_design_test import Ui_MainWindow
import qtawesome as qta
import qrcode
from PIL import Image
from PIL import ImageQt

class main_window(QtGui.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Creating some variables for dinamic QR:
        self.qr_version = 7
        self.ui.versionLcd.display(self.qr_version)
        
        #Connecting the buttons:
        self.ui.quitButton.clicked.connect(self.close_app)
        self.ui.runButton.clicked.connect(self.create_qrcode)
        self.ui.loadButton.clicked.connect(self.open_file)
        self.ui.saveButton.clicked.connect(self.save_file)
        self.ui.saveButton.setDisabled(True)
        self.ui.downButton.clicked.connect(self.down_version)
        self.ui.upButton.clicked.connect(self.up_version)
                
        
        # Get icons by name.
        fa_exit = qta.icon('fa.times', options=[{'scale_factor': 0.8,
                                                 'color': 'white'}])
        fa_cogs = qta.icon('fa.cogs', options=[{'scale_factor': 0.8,
                                                 'color': 'white'}])
        fa_folder = qta.icon('fa.folder-open-o', options=[{'scale_factor': 0.8,
                                                 'color': 'black'}])
        fa_floppy = qta.icon('fa.floppy-o', options=[{'scale_factor': 0.8,
                                                 'color': 'black'}])                                         
        self.ui.quitButton.setIcon(fa_exit)
        self.ui.saveButton.setIcon(fa_floppy)
        self.ui.runButton.setIcon(fa_cogs)
        self.ui.loadButton.setIcon(fa_folder)

    def up_version(self):
        self.qr_version += 1
        if self.qr_version == 40: 
            self.ui.upButton.setDisabled(True)
        elif self.qr_version == 2:
            self.ui.downButton.setDisabled(False)
        self.ui.versionLcd.display(self.qr_version)
            
    def down_version(self):
        self.qr_version -= 1
        if self.qr_version == 1: 
            self.ui.downButton.setDisabled(True)
        elif self.qr_version == 39:
            self.ui.upButton.setDisabled(False)
        self.ui.versionLcd.display(self.qr_version)

    def create_qrcode(self):
        total_box = (self.qr_version - 1)*4 + 21
        box_size_stimate = 260 // total_box
        border_size = (260 - (box_size_stimate * total_box))//box_size_stimate//2
        print(self.qr_version, total_box, box_size_stimate, border_size, box_size_stimate * total_box)
        qr = qrcode.QRCode(
            version=self.qr_version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size_stimate,
            border= border_size,
        )
        qr.add_data('https://github.com/isman7')
        qr.make(fit=True)
        img = qr.make_image()
        self.pix = QtGui.QPixmap.fromImage(ImageQt.ImageQt(img))
        self.ui.label.setPixmap(self.pix)
        self.ui.saveButton.setDisabled(False)
    
    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Load File')
        if name:
            img_loaded = Image.open(name)
            self.pix = QtGui.QPixmap.fromImage(ImageQt.ImageQt(img_loaded))
            self.ui.label.setPixmap(self.pix)
            self.ui.saveButton.setDisabled(False)
    
    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File', "qrcode.png")
        self.pix.save(name)
        
        
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