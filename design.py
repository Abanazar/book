from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 890)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:  #202225;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(558, 25, 521, 31))
        self.listWidget_2.setStyleSheet("border: 3px outset #ffffff;"
"color: #ffffff;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 70, 821, 771))
        self.textEdit.setStyleSheet("border: 3px groove #ffffff;\n"
"font-size: 20px;\n"
"color: #ffffff;\n")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 221, 771))
        self.listWidget.setStyleSheet("QListWidget{\n"
"border: 3px groove #ffffff;\n"
"color: #ffffff;\n"
"font-size: 16px;\n"
"}\n"
"QScrollBar:vertical {              \n"
"    border: none;\n"
"    background: white;\n"
"    width: 5px;               \n"
"    margin: 0px 0px 0px 0px;\n"
"    left: 15px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #ffffff;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: #ffffff;\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #ffffff;\n"
"    height: 0 px;;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 10, 221, 51))
        self.widget_3.setStyleSheet("border: 3px  groove rgb(210, 210, 210);")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(50, 10, 111, 31))
        self.label.setStyleSheet("font: 20px;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 30, 511, 21))
        self.pushButton_2.setStyleSheet("font-size: 16px;"
                                        "border: 0px groove #00000000;"
                                        "background-color: #00000000;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ARBook"))
        self.label.setText(_translate("MainWindow", "You Book"))
