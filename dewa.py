# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'de.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 890)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:2, y1:3, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 221, 771))
        self.listWidget.setStyleSheet("border: 3px groove rgb(71, 71, 71);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 16px;")
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 70, 821, 771))
        self.textEdit.setStyleSheet("border: 3px groove rgb(71, 71, 71);\n"
"font-size: 20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:2, y1:3, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.textEdit.setObjectName("textEdit")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(558, 25, 521, 31))
        self.listWidget_2.setStyleSheet("border: 3px outset rgb(71, 71, 71);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 30, 511, 21))
        self.pushButton_2.setStyleSheet("font-size: 16px;"
                                        "border: 0px groove #00000000;"
                                        "background-color: #00000000;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 10, 221, 51))
        self.widget_3.setStyleSheet("border: 3px  groove rgb(71, 71, 71);")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 31))
        self.label.setStyleSheet("font: 20px;\n"
"color: rgb(0, 0, 0)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARBook"))
        self.label.setText(_translate("MainWindow", "  You Book"))
