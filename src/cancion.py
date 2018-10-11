class Cancion:

    def __init__(self):
        self.artista=""
        self.titulo=""
        self.fecha=""
        self.genero=""
        self.track=""
        self.album=""
        self.path=""

    def setArtista(self,artista):
        if artista is None:
            self.artista="Unknown"
        else:
            self.artista=str(artista)

    def setTitulo(self,titulo):
        if titulo is None:
            self.titulo="Unknown"
        else:
            self.titulo=str(titulo)

    def setFecha(self,fecha):
        if fecha is None:
            self.fecha="2018"
        else:
            self.fecha=str(fecha)

    def setGenero(self,genero):
        if genero is None:
            self.genero="Unknown"
        else:
            self.genero=genero

    def setTrack(self,track):
        if track[0] is None:
            self.track=0
        else:
            self.track=int(track[0])

    def setAlbum(self,album):
        if album is None:
            self.album="Unknown"
        else:
            self.album=str(album)

    def setPath(self,path):
        self.path=str(path)
