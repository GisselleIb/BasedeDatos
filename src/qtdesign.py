# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    """Clase que construye la ventana principal de la interfaz gráfica.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupPersB = QtWidgets.QPushButton(self.centralwidget)
        self.groupPersB.setObjectName("groupPersB")
        self.gridLayout_3.addWidget(self.groupPersB, 0, 0, 1, 1)
        self.songsB = QtWidgets.QPushButton(self.centralwidget)
        self.songsB.setObjectName("songsB")
        self.gridLayout_3.addWidget(self.songsB, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 1)
        self.searchB = QtWidgets.QPushButton(self.centralwidget)
        self.searchB.setObjectName("searchB")
        self.gridLayout_2.addWidget(self.searchB, 2, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddPersontoGroup = QtWidgets.QAction(MainWindow)
        self.actionAddPersontoGroup.setObjectName("actionAdd_Person_to_Group")
        self.menuSettings.addAction(self.actionAddPersontoGroup)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player"))
        self.groupPersB.setText(_translate("MainWindow", "Add Group/Person"))
        self.songsB.setText(_translate("MainWindow", "Add Songs"))
        self.searchB.setText(_translate("MainWindow", "Search"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionAddPersontoGroup.setText(_translate("MainWindow", "Add Person to Group"))
