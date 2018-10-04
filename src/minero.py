from basededatos import BaseDeDatos
from pathlib import Path
import eyed3
class Minero:

    def __init__():
        self.path=str(Path.home())+'/Music'
        self.listCancion=[]

    def minar(dir):
        audiofile=""
        path=Path(dir)
        for mp3 in path.iterdir():
            if(mp3.is_dir()):
                self.minar(str(mp3))
            audiofile=eyed3.load(mp3)
            self.listCancion.append(self.creaCancion(audiofile,path))
        self.creaRegistros()

    def creaCancion(audiofile,path):
        cancion=Cancion()
        cancion.setArtista(audiofile.tag.artist)
        cancion.setTitulo(audiofile.tag.title)
        cancion.setGenero(str(audiofile.tag.genre))
        cancion.setTrack(audiofile.tag.track_num)
        cancion.setAlbum(audiofile.tag.album)
        cancion.setPath(path)
        return cancion

    def creaRegistros():
        pass
