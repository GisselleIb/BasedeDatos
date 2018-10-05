from basededatos import BaseDeDatos
from cancion import Cancion
from pathlib import Path
import eyed3
class Minero:

    def __init__(self,bd):
        self.path=str(Path.home())+'/Music'
        self.listCancion=[]
        self.bd=bd

    def minar(self,dir):
        i=0
        audiofile=""
        path=Path(dir)
        for mp3 in path.iterdir():
            if(mp3.is_dir()):
                self.minar(str(mp3))
            try:
                audiofile=eyed3.load(mp3)
                self.listCancion.append(self.creaCancion(audiofile,path,i))
            except IOError:
                continue
            i+=1
        self.creaRegistros()

    def creaCancion(self,audiofile,path,i):
        cancion=Cancion()
        cancion.setArtista(audiofile.tag.artist)
        cancion.setTitulo(audiofile.tag.title)
        cancion.setGenero(str(audiofile.tag.genre))
        cancion.setTrack(audiofile.tag.track_num)
        cancion.setFecha(audiofile.tag.getBestDate())
        cancion.setAlbum(audiofile.tag.album)
        cancion.setIdAlbum(i)
        cancion.setPath(path)
        return cancion

    def creaRegistros(self):
        ids=0
        idp=0
        list=[]
        for cancion in self.listCancion:
            self.bd.llenaTablas("songs",[ids,idp,cancion.id_album,cancion.path,cancion.titulo,cancion.track,cancion.fecha,cancion.genero])
            self.bd.llenaTablas("albums",[cancion.id_album,cancion.path,cancion.album,cancion.fecha])
            self.bd.llenaTablas("performers",[cancion.idp,2,cancion.artista])
