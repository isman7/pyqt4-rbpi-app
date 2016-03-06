# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_design_test.ui'
#
# Created: Sun Mar  6 17:35:08 2016
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
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 70, 92, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 30, 92, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 110, 92, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 150, 92, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(680, 310, 92, 27))
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
"color: #fff;\n"
"background-color: #ec971f;\n"
"border-color: #d58512;\n"
"}"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 190, 92, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 230, 92, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(680, 270, 92, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 468, 311))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.graphicsView = QtGui.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 448, 290))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton", None))

