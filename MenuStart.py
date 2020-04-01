# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuStart.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(180, 200, 91, 41))
        self.button1.setObjectName("button1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(180, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.button1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button1_2.setGeometry(QtCore.QRect(300, 200, 91, 41))
        self.button1_2.setObjectName("button1_2")
        self.button1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button1_3.setGeometry(QtCore.QRect(430, 200, 91, 41))
        self.button1_3.setObjectName("button1_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 251, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../OneDrive/Documents/CIS 434/CIS_434/CSU_Logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Overview"))
        self.label1.setText(_translate("MainWindow", "Welcome to our restarurant!"))
        self.pushButton.setText(_translate("MainWindow", "Order"))
        self.button1_2.setText(_translate("MainWindow", "Inventory"))
        self.button1_3.setText(_translate("MainWindow", "Checkout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
