#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from basededatos import BaseDeDatos
from cancion import Cancion
from pathlib import Path
import eyed3
class Minero:
    """Clase Minero, busca en el directorio ~/Music los archivos mp3
    y los guarda en la base de datos.
    """

    def __init__(self):
        """Constructor de la clase.
        Atributos
        path : str
            El path del usuario a la carpeta Music
        listCancion : []
            La lista en la que se guardaran las canciones minadas.
        bd : BaseDeDatos
            Un objeto base de datos que se utilizara para guardar las
            canciones minadas.
        """
        self.path=str(Path.home())+'/Music'
        self.listCancion=[]
        self.bd=BaseDeDatos()

    def minar(self,dir):
        """Mina de forma recursiva las canciones, carpeta por carpeta.
        Parámetros
        dir : str
            Directorio actual.
        """
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
        """Crea objetos cancion en el que guarda los datos que saca
        de las etiquetas
        Parámetros
        audiofile : eyed3 object
            El objeto eyed3 del que leeremos las etiquetas necesarias.
        path : str
            El path en el que se encontró la canción.
        """
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
        """Por cada objeto Cancion guardado en listCancion, se guardan
        los datos en la tabla correspondiente de la base de datos.
        """
        for cancion in self.listCancion:
            self.bd.llenaTablas("albums",[cancion.path,cancion.album,cancion.fecha])
            self.bd.llenaTablas("performers",[2,cancion.artista])
            self.bd.llenaTablas("songs",[cancion.path,cancion.titulo,cancion.track,cancion.fecha,cancion.genero,cancion.artista,cancion.album])
