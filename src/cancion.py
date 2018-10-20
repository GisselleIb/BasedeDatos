#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Cancion:
    """Clase Cancion, guarda los datos de cada canción
    """

    def __init__(self):
        """Constructor de la clase.
        Atributos
        artista : str
            El nombre del artista de la canción
        titulo : str
            El título de la canción
        fecha : str
            Fecha en que salió la canción
        genero : str
            El género de la canción
        track : str
            El número de track de la canción
        album : str
            El nombre del álbum
        path : str
            El path en el que se encuentra la canción
        """
        self.artista=""
        self.titulo=""
        self.fecha=""
        self.genero=""
        self.track=""
        self.album=""
        self.path=""

    def setArtista(self,artista):
        """Setter del artista
        Parámetros
        artista : str
            Nombre de la artista
        """
        if artista is None:
            self.artista="Unknown"
        else:
            self.artista=str(artista)

    def setTitulo(self,titulo):
        """Setter del título
        Parámetros
        titulo : str
            Título de la canción
        """
        if titulo is None:
            self.titulo="Unknown"
        else:
            self.titulo=str(titulo)

    def setFecha(self,fecha):
        """Setter de la fecha
        Parámetros
        fecha : str
            Fecha en que salió de la canción
        """
        if fecha is None:
            self.fecha="2018"
        else:
            self.fecha=str(fecha)

    def setGenero(self,genero):
        """Setter del género
        Parámetros
        genero : str
            Género de la canción
        """
        if genero is None:
            self.genero="Unknown"
        else:
            self.genero=genero

    def setTrack(self,track):
        """Setter del track
        Parámetros
        track : int
            El número de track de la canción
        """
        if track[0] is None:
            self.track=0
        else:
            self.track=int(track[0])

    def setAlbum(self,album):
        """Setter del álbum
        Parámetros
        album : str
            El nombre del álbum al que pertenece la canción
        """
        if album is None:
            self.album="Unknown"
        else:
            self.album=str(album)

    def setPath(self,path):
        """Setter del path de la canción
        Parámetros
        path : str
            El path de la canción
        """
        self.path=str(path)
