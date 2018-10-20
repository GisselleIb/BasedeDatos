#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from basededatos import BaseDeDatos
from minero import Minero
from dialogPG import Ui_Performer
from dialPerToGroup import Ui_Dialog
import sys
from qtdesign import Ui_MainWindow
from PyQt5 import QtGui

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget, QMainWindow, QDialog)


class BdGUI(QMainWindow):
    """Clase de la ventana principal. Contiene todo el funcionamiento
    de la interfaz gráfica y aquí se conectan los dos tipos de diálogos
    """

    ARTIST, TITLE, GENRE, ALBUM = range(4)

    def __init__(self,control):
        """Constructor de la clase
        Parámetros
        control : Controlador
            Objeto controlador con el que la interfaz se comunicara
            con la base de datos
        Atributos
        minero : Minero
            Objeto minero que la interfaz podrá llamar
        dialog = QDialog
            Objeto del diálogo que crea el diálogo para agregar
            personas y grupos
        dialog2 = QDialog
            Objeto del diálogo que crea la ventana para agregar
            personas a un grupo
        """
        super(BdGUI,self).__init__()
        self.control=control
        self.minero=Minero()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = QDialog()
        self.dialog2 = QDialog()
        self.dialog.ui = Ui_Performer()
        self.dialog2.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog2.ui.setupUi(self.dialog2)
        self.initUI()

    def initUI(self):
        """Inicia los diferentes widgets y los conecta
        a sus funciones correspondientes
        """
        self.ui.treeView.setRootIsDecorated(True)
        self.ui.treeView.setAlternatingRowColors(True)
        self.model = self.createBDModel(self)
        self.ui.treeView.setModel(self.model)
        self.ui.actionAddPersontoGroup.triggered.connect(self.openDialog)
        self.ui.searchB.clicked.connect(self.searchButton)
        self.ui.songsB.clicked.connect(self.fillTree)
        self.ui.groupPersB.clicked.connect(self.dialog.exec_)
        self.dialog.ui.buttonBox.accepted.connect(self.setPerson)
        self.dialog.ui.buttonBox.accepted.connect(self.setGroup)
        self.dialog2.ui.buttonBox.accepted.connect(self.addPerToGroup)

    def fillTree(self, model):
        """Mina y llena el treeView con los datos
        """
        if self.minero.bd.exist == False:
            self.minero.minar(self.minero.path)
            self.minero.creaRegistros()
        consulta=self.control.searchBD(None)
        if consulta is not None:
            for row in consulta:
                self.addSongs(model,row[0],row[1], row[2],row[3])

    def createBDModel(self,parent):
        """Crea el modelo que usara el treeView para la base de datos
        """
        model = QStandardItemModel(0, 4, parent)
        model.setHeaderData(self.ARTIST, Qt.Horizontal, "Artist")
        model.setHeaderData(self.TITLE, Qt.Horizontal, "Title")
        model.setHeaderData(self.GENRE, Qt.Horizontal, "Genre")
        model.setHeaderData(self.ALBUM, Qt.Horizontal, "Album")
        return model

    def searchButton(self):
        """Función conectada al botón Search, hace una
        consulta a la base de datos con lo escribió el
        usuario en la línea de busqueda
        """
        s=self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        self.clearTree()
        self.control.searchBD(s)

    def openDialog(self):
        """Llena la lista que contiene el dialogo2 con todas las
        personas  y grupos existentes en la base de datos
        """
        self.dialog2.ui.model.removeRows(0, self.dialog2.ui.model.rowCount())
        self.dialog2.ui.model2.removeRows(0, self.dialog2.ui.model2.rowCount())
        consP=self.minero.bd.consulta("","persons")
        self.dialog2.ui.setPerAndGroup(consP,"persons")
        consG=self.minero.bd.consulta("","groups")
        self.dialog2.ui.setPerAndGroup(consG,"groups")
        self.dialog2.exec_()

    def addPerToGroup(self):
        """Llama al controlador y le pasa los datos de la persona
        y grupo para agregarlos a la tabla 'in_group' de la base
        de datos
        """
        index1=self.dialog2.ui.listView.selectedIndexes()
        index2=self.dialog2.ui.listView_2.selectedIndexes()
        if index1 != [] and index2 != []:
            self.control.actualizaBD("in_group",[str(index1[0].data()),str(index2[0].data())])

    def clearTree(self):
        """Limpia todos los datos del treeView
        """
        self.model.beginResetModel()
        self.model.removeRows(0,self.model.rowCount())
        self.model.endResetModel()

    def addSongs(self,model, artist, title, genre, album):
        """Agrega los datos de una canción al treeView
        """
        model.insertRow(0)
        model.setData(model.index(0, self.ARTIST), artist)
        model.setData(model.index(0, self.TITLE), title)
        model.setData(model.index(0, self.GENRE), genre)
        model.setData(model.index(0, self.ALBUM), album)

    def setPerson(self):
        """Toma los datos escritos por el usuario en la
        línea correspondiente y se los pasa al controlador
        para que los agregue a la nueva persona a la
        base de datos
        """
        list=[]
        list.append(self.dialog.ui.stage.text())
        list.append(self.dialog.ui.real.text())
        list.append(self.dialog.ui.birth.text())
        list.append(self.dialog.ui.death.text())
        self.dialog.ui.stage.clear()
        self.dialog.ui.real.clear()
        self.dialog.ui.birth.clear()
        self.dialog.ui.death.clear()
        self.control.actualizaBD("persons",list)

    def setGroup(self):
        """Toma los datos escritos por el usuario en la
        línea correspondiente y se los pasa al controlador
        para que agregue a un nuevo grupo a la base de datos
        """
        list=[]
        list.append(self.dialog.ui.group.text())
        list.append(self.dialog.ui.start.text())
        list.append(self.dialog.ui.end.text())
        self.dialog.ui.group.clear()
        self.dialog.ui.start.clear()
        self.dialog.ui.end.clear()
        self.control.actualizaBD("groups",list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BdGUI()
    sys.exit(app.exec_())
