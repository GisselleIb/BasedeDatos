# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogPerform.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Performer(object):
    """Clase que crea el diálogo para agregar personas
    y grupos.
    """
    def setupUi(self, Performer):
        Performer.setObjectName("Performer")
        Performer.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Performer)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Performer)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.stage = QtWidgets.QLineEdit(self.tab_1)
        self.stage.setGeometry(QtCore.QRect(100, 10, 281, 31))
        self.stage.setObjectName("stage")
        self.real = QtWidgets.QLineEdit(self.tab_1)
        self.real.setGeometry(QtCore.QRect(100, 50, 281, 31))
        self.real.setObjectName("real")
        self.birth = QtWidgets.QLineEdit(self.tab_1)
        self.birth.setGeometry(QtCore.QRect(100, 90, 281, 31))
        self.birth.setObjectName("birth")
        self.death = QtWidgets.QLineEdit(self.tab_1)
        self.death.setGeometry(QtCore.QRect(100, 130, 281, 31))
        self.death.setObjectName("death")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(0, 20, 91, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(0, 90, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 101, 19))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.group = QtWidgets.QLineEdit(self.tab_2)
        self.group.setGeometry(QtCore.QRect(120, 20, 261, 31))
        self.group.setObjectName("group")
        self.start = QtWidgets.QLineEdit(self.tab_2)
        self.start.setGeometry(QtCore.QRect(120, 80, 261, 31))
        self.start.setObjectName("start")
        self.end = QtWidgets.QLineEdit(self.tab_2)
        self.end.setGeometry(QtCore.QRect(120, 140, 261, 31))
        self.end.setObjectName("end")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 101, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 91, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 81, 19))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Performer)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Performer.accept)
        self.buttonBox.rejected.connect(Performer.reject)
        QtCore.QMetaObject.connectSlotsByName(Performer)

    def retranslateUi(self, Performer):
        _translate = QtCore.QCoreApplication.translate
        Performer.setWindowTitle(_translate("Performer", "Dialog"))
        self.label.setText(_translate("Performer", "Stage name:"))
        self.label_2.setText(_translate("Performer", "Real name:"))
        self.label_3.setText(_translate("Performer", "Date of birth"))
        self.label_4.setText(_translate("Performer", "Date of death:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Performer", "Person"))
        self.label_5.setText(_translate("Performer", "Group name:"))
        self.label_6.setText(_translate("Performer", "Start date:"))
        self.label_7.setText(_translate("Performer", "End date:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Performer", "Group"))
