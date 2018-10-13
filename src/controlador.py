from basededatos import BaseDeDatos
from minero import Minero
from PyQt5.QtWidgets import QApplication
import sys
from bdGUI import BdGUI

class Controlador():

    def __init__(self):
        self.bd=BaseDeDatos()
        self.gui=BdGUI(self)
        self.gui.fillTree(self.gui.model)
        self.gui.show()

    def search(self,comando):
        return self.bd.comandos(comando)

    def actualizaBD(self,evento):
        pass
    def actualizaGUI(self,cursor):
        for song in cursor:
            self.gui.addSongs(self.gui.model,song[0],song[1],song[2],song[3])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c=Controlador()
    sys.exit(app.exec_())
