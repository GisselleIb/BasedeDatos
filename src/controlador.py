#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from basededatos import BaseDeDatos
from minero import Minero
from PyQt5.QtWidgets import QApplication
import sys
from bdGUI import BdGUI

class Controlador():
    """Clase Controlador, se encarga de la comunicación entre
    la base de datos y la interfaz.
    """

    def __init__(self):
        """Constructor de la clase, crea una instancia de legal
        interfaz y una instancia de la base de datos.
        Atributos
        gui : BdGUI
            La interfaz grafica
        bd : BaseDeDatos
            Objeto base de datos que se utilizara para hacer las
            consultas y guardar nuevos datos.
        """
        self.gui=BdGUI(self)
        self.bd=BaseDeDatos()
        #self.gui.fillTree(self.gui.model)
        self.gui.show()

    def searchBD(self,comando):
        """Actualiza la interfaz con la consulta que regresa la
        base de datos.
        Parámetros
        comando : str
            Comando que se pasa a la base de datos para hacer
            una consulta.
        """
        self.actGUITree(self.bd.comandos(comando))

    def actualizaBD(self,tabla,args):
        """Recibe nuevos datos para llenar una tabla en específico
        de la base de datos.
        Parámetros
        tabla : str
            La tabla en la que se introduciran los datos nuevos.
        args : [str]
            Lista con los datos a guardar en la base de datos.
        """
        b=False
        for s in args:
            if s != "":
                b=True
        if b:
            self.bd.llenaTablas(tabla,args)
        else: return

    def actGUITree(self,cursor):
        """Actualiza el treeView de la interfaz con los datos que
        guarda la base de datos.
        cursor : cursor
            Iterable que contiene los datos de la consulta.
        """
        if cursor is not None:
            for song in cursor:
                self.gui.addSongs(self.gui.model,song[0],song[1],song[2],song[3])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c=Controlador()
    sys.exit(app.exec_())
