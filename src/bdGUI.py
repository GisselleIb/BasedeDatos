#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from basededatos import BaseDeDatos
from minero import Minero
import sys
from qtdesign import Ui_MainWindow
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget, QMainWindow)


class BdGUI(QMainWindow):

    ARTIST, TITLE, GENRE, ALBUM = range(4)

    def __init__(self):
        super(BdGUI,self).__init__()
        self.minero=Minero()
        self.bd=BaseDeDatos()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.treeView.setRootIsDecorated(True)
        self.ui.treeView.setAlternatingRowColors(True)

        model = self.createBDModel(self)
        self.ui.treeView.setModel(model)
        print(self.minero.bd.exist)
        if self.minero.bd.exist == False :
            self.minero.minar(self.minero.path)
            self.minero.creaRegistros()
        consulta=self.bd.consulta(None,"todo")
        if consulta is not None:
            print("not None")
            for row in consulta:
                self.addSongs(model,row[0],row[1], row[2],row[3])

        self.show()

    def createBDModel(self,parent):
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.ARTIST, Qt.Horizontal, "Artist")
        model.setHeaderData(self.TITLE, Qt.Horizontal, "Title")
        model.setHeaderData(self.GENRE, Qt.Horizontal, "Genre")
        model.setHeaderData(self.ALBUM, Qt.Horizontal, "Album")
        return model

    def addSongs(self,model, artist, title, genre, album):
        model.insertRow(0)
        model.setData(model.index(0, self.ARTIST), artist)
        model.setData(model.index(0, self.TITLE), title)
        model.setData(model.index(0, self.GENRE), genre)
        model.setData(model.index(0, self.ALBUM), album)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BdGUI()
    sys.exit(app.exec_())
