import unittest
from src.cancion import Cancion

class TestCancion(unittest.TestCase):
    cancion=""
        def setUp():
            artista=Artista()

        def test_setArtista():
            self.assertEqual(self.cancion.artista,"")
            self.cancion.setArtista("artist")
            self.assertEqual(self.artista,"artist")

        def test_setTitulo():
            self.assertEqual(self.cancion.titulo,"")
            self.cancion.setTitulo("title")
            self.assertEqual(self.cancion.titulo,"title")

        def test_setFecha():
            self.assertEqual(self.cancion.fecha,"")
            self.cancion.setFecha("11/11/11")
            self.assertEqual(self.cancion.titulo,"11/11/11")

        def test_setGenero():
            self.assertEqual(self.cancion.genero,"")
            self.cancion.setGenero("genre")
            self.assertEqual(self.cancion.genero,"genre")

        def test_setTrack():
            self.assertEqual(self.cancion.numTrack,"")
            self.cancion.setTrack("1")
            self.assertEqual(self.cancion.numTrack,"1")
