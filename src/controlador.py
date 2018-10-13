from basededatos import BaseDeDatos
from minero import Minero
from PyQt5.QtWidgets import QApplication
import sys
from bdGUI import BdGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = BdGUI()
    sys.exit(app.exec_())
    bd.consulta("Glass Animals", "artista")
    bd.consulta("The Trip", "cancion")
    bd.consulta("Unknown", "album")
