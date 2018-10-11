#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from qtdesign import Ui_MainWindow
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget)


class App(QWidget):

    ARTIST, TITLE, GENRE, ALBUM = range(4)

    def __init__(self,bd):
        super().__init__()
        self.bd=bd
        self.ui=Ui_MainWindow()
        self.setupUi(QtWidgets.QMainWindow())

    def initUI(self):
        self.dataGroupBox = QGroupBox("Songs")
        self.ui.treeView.setRootIsDecorated(True)
        self.ui.treeView.setAlternatingRowColors(True)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.ui.treeView)
        self.dataGroupBox.setLayout(dataLayout)

        model = self.createBDModel(self)
        self.ui.treeView.setModel(model)
        self.addSongs(model)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)

        self.show()

    def addSongs(self,model):
        pass

    def createBDModel(self,parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.ARTIST, Qt.Horizontal, "Artist")
        model.setHeaderData(self.TITLE, Qt.Horizontal, "Title")
        model.setHeaderData(self.GENRE, Qt.Horizontal, "Genre")
        model.setHeaderData(self.ALBUM, Qt.Horizontal, "Album")
        return model

    def addMail(self,model, artist, title, genre, album):
        model.insertRow(0)
        model.setData(model.index(0, self.ARTIST), artist)
        model.setData(model.index(0, self.TITLE), title)
        model.setData(model.index(0, self.GENRE), genre)
        model.setData(model.index(0, self.ALBUM), album)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
