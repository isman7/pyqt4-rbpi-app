# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design_test.ui'
#
# Created: Mon Mar  7 19:19:16 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 290, 290))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(15, 15, 260, 260))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 371, 771, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loadButton = QtGui.QPushButton(self.layoutWidget)
        self.loadButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #333;\n"
"background-color: #fff;\n"
"border-color: #ccc;\n"
"}\n"
"\n"
"QPushButton:hover:pressed{\n"
"  color: #333;\n"
"  background-color: #e6e6e6;\n"
"  border-color: #adadad;\n"
"border: none;\n"
"}"))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.horizontalLayout.addWidget(self.loadButton)
        self.saveButton = QtGui.QPushButton(self.layoutWidget)
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #333;\n"
"background-color: #fff;\n"
"border-color: #ccc;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"  color: #333;\n"
"  background-color: #e6e6e6;\n"
"  border-color: #adadad;\n"
"}"))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.runButton = QtGui.QPushButton(self.layoutWidget)
        self.runButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #fff;\n"
"background-color: #5cb85c;\n"
"border-color: #4cae4c;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"  color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}\n"
""))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.quitButton = QtGui.QPushButton(self.layoutWidget)
        self.quitButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #fff;\n"
"background-color: #f0ad4e;\n"
"border-color: #eea236;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"  color: #fff;\n"
"  background-color: #ec971f;\n"
"  border-color: #d58512;\n"
"}"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(450, 30, 331, 61))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.upButton = QtGui.QPushButton(self.layoutWidget_3)
        self.upButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #333;\n"
"background-color: #fff;\n"
"border-color: #ccc;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"  color: #333;\n"
"  background-color: #e6e6e6;\n"
"  border-color: #adadad;\n"
"}"))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout_3.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(self.layoutWidget_3)
        self.downButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"display: inline-block;\n"
"padding: 6px 12px;\n"
"margin-bottom: 0;\n"
"font-size: 14px;\n"
"font-weight: normal;\n"
"line-height: 1.42857143;\n"
"text-align: center;\n"
"white-space: nowrap;\n"
"vertical-align: middle;\n"
"border: 1px solid transparent;\n"
"color: #333;\n"
"background-color: #fff;\n"
"border-color: #ccc;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"  color: #333;\n"
"  background-color: #e6e6e6;\n"
"  border-color: #adadad;\n"
"}"))
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.horizontalLayout_3.addWidget(self.downButton)
        self.versionLcd = QtGui.QLCDNumber(self.centralwidget)
        self.versionLcd.setGeometry(QtCore.QRect(330, 40, 111, 41))
        self.versionLcd.setObjectName(_fromUtf8("versionLcd"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Press \'Run\' to make a QR Code!", None))
        self.loadButton.setText(_translate("MainWindow", "Load", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.runButton.setText(_translate("MainWindow", "Run", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.upButton.setText(_translate("MainWindow", "UP", None))
        self.downButton.setText(_translate("MainWindow", "DOWN", None))

