import unittest
import sys
sys.path.append('../..')
from src.cancion import Cancion

class TestCancion(unittest.TestCase):
    def setUp(self):
        self.cancion=Cancion()
    def test_setArtista(self):
        self.assertEqual(self.cancion.artista,"")
        self.cancion.setArtista("artist")
        self.assertEqual(self.cancion.artista,"artist")

    def test_setTitulo(self):
        self.assertEqual(self.cancion.titulo,"")
        self.cancion.setTitulo("title")
        self.assertEqual(self.cancion.titulo,"title")

    def test_setFecha(self):
        self.assertEqual(self.cancion.fecha,"")
        self.cancion.setFecha("11/11/11")
        self.assertEqual(self.cancion.fecha,"11/11/11")

    def test_setGenero(self):
        self.assertEqual(self.cancion.genero,"")
        self.cancion.setGenero("genre")
        self.assertEqual(self.cancion.genero,"genre")

    def test_setTrack(self):
        self.assertEqual(self.cancion.track,"")
        self.cancion.setTrack("1")
        self.assertEqual(self.cancion.track,1)
