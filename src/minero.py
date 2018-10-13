from basededatos import BaseDeDatos
from cancion import Cancion
from pathlib import Path
import eyed3
class Minero:

    def __init__(self):
        self.path=str(Path.home())+'/Music'
        self.listCancion=[]
        self.bd=BaseDeDatos()

    def minar(self,dir):
        audiofile=""
        path=Path(dir)
        for mp3 in path.iterdir():
            if(mp3.is_dir()):
                self.minar(str(mp3))
            else:
                try:
                    audiofile=eyed3.load(mp3)
                    self.listCancion.append(self.creaCancion(audiofile,path))
                except IOError:
                    continue

    def creaCancion(self,audiofile,path):
        cancion=Cancion()
        cancion.setArtista(audiofile.tag.artist)
        cancion.setTitulo(audiofile.tag.title)
        cancion.setGenero(str(audiofile.tag.genre))
        cancion.setTrack(audiofile.tag.track_num)
        cancion.setFecha(audiofile.tag.getBestDate())
        cancion.setAlbum(audiofile.tag.album)
        cancion.setPath(path)
        return cancion

    def creaRegistros(self):
        for cancion in self.listCancion:
            self.bd.llenaTablas("albums",[cancion.path,cancion.album,cancion.fecha])
            self.bd.llenaTablas("performers",[2,cancion.artista])
            self.bd.llenaTablas("songs",[cancion.path,cancion.titulo,cancion.track,cancion.fecha,cancion.genero,cancion.artista,cancion.album])
