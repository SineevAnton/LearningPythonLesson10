# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(3, 0, 34);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.frame.setStyleSheet("background-color: rgb(0, 207, 173);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 480, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 7, 44);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(165, 75, 150, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("58902.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 280, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: rgb(0, 207, 173);\n"
"border: 2px solid;\n"
"border-radius: 30;\n"
"color: rgb(0, 7, 44);\n"
"border-color: rgb(0, 19, 130);")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 360, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: rgb(0, 207, 173);\n"
"border: 2px solid;\n"
"border-radius: 30;\n"
"color: rgb(0, 7, 44);\n"
"border-color: rgb(0, 19, 130);")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 440, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: rgb(0, 207, 173);\n"
"border: 2px solid;\n"
"border-radius: 30;\n"
"color: rgb(0, 7, 44);\n"
"border-color: rgb(0, 19, 130);")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 520, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: rgb(0, 207, 173);\n"
"border: 2px solid;\n"
"border-radius: 30;\n"
"color: rgb(0, 7, 44);\n"
"border-color: rgb(0, 19, 130);")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 600, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 207, 173);\n"
"    color: rgb(0, 7, 44);\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 170, 255);\n"
"    color: rgb(0, 7, 44);\n"
"    border-radius: 30;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CURRENCY CONVERTER"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРОВАТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
