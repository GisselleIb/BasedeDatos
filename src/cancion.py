class Cancion:

    def __init__(self):
        self.artista=""
        self.titulo=""
        self.fecha=""
        self.genero=""
        self.numTrack=""
        self.album=""
        self.path=""
        self.id_album=0

    def setArtista(self,artista):
        if artista is None:
            self.artista="Unknown"
        else:
            self.artista=artista

    def setTitulo(self,titulo):
        if titulo is None:
            self.titulo="Unknown"
        else:
            self.titulo=titulo

    def setFecha(self,fecha):
        if fecha is None:
            self.fecha="2018"
        else:
            self.fecha=fecha

    def setGenero(self,genero):
        if genero is None:
            self.genero="Unknown"
        else:
            self.genero=genero

    def setTrack(self,track):
        if track is None:
            self.numTrack=0
        else:
            self.numTrack=track

    def setAlbum(self,album):
        if album is None:
            self.album="Unknown"
        else:
            self.album=album

    def setPath(self,path):
        self.path=path

    def setIdAlbum(self,id_album):
        self.id_album=id_album
