# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(849, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/xerolinux-logo128x128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 0, 96, 96))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("images/xerolinux-logo96x96.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(110, 30, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.mainLabel.setFont(font)
        self.mainLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.mainLabel.setWordWrap(True)
        self.mainLabel.setObjectName("mainLabel")
        self.exitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitPushButton.setGeometry(QtCore.QRect(703, 510, 141, 38))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(12)
        self.exitPushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitPushButton.setIcon(icon1)
        self.exitPushButton.setIconSize(QtCore.QSize(32, 32))
        self.exitPushButton.setObjectName("exitPushButton")
        self.okPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okPushButton.setGeometry(QtCore.QRect(540, 510, 151, 38))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(12)
        self.okPushButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/back-in-time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okPushButton.setIcon(icon2)
        self.okPushButton.setIconSize(QtCore.QSize(32, 32))
        self.okPushButton.setObjectName("okPushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 831, 391))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Xerolinux Rollback Utility"))
        self.mainLabel.setText(_translate("MainWindow", "Please select the snapshot from the list below and click the rollback button."))
        self.exitPushButton.setText(_translate("MainWindow", "&Exit"))
        self.okPushButton.setText(_translate("MainWindow", "&Rollback"))
