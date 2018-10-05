import unittest
import sys
sys.path.insert(0,'/home/gisselleib/Documents/moquito/MyP/proyectos/BDM/src')
from src.minero import Minero
from src.cancion import Cancion
class TestMinero(unittest.TestCase):
    minero=Minero()

    def test_minar(self):
        with self.assertRaises(OSError):
            self.minero.minar("~/Music")
        self.minero.minar(minero.path)
        self.assertTrue(len(minero.listCancion) >0)


    def test_creaCancion(self):
        audiotest=''
        c=None
        path=str(self.minero.path)+'/Music'
        p=Path(dir)
        for mp3 in path.iterdir():
            audiotest=eyed3.load(mp3)
            self.assertTrue(type(self.minero.creaCancion(audiotest)) is type(Cancion))

    def test_llenaBase(self):
        pass
