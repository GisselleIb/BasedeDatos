from basededatos import BaseDeDatos
from minero import Minero


if __name__ == "__main__":
    bd=BaseDeDatos()
    min=Minero(bd)
    bd.creaBD()
    min.minar(min.path)
    min.creaRegistros()
    bd.consulta("Glass Animals", "artista")
    bd.consulta("The Trip", "cancion")
    bd.consulta("Unknown", "album")
