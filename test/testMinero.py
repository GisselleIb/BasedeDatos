import unittest
import sys
sys.path.append('../..')
from src.minero import Minero
from src.cancion import Cancion
from pathlib import Path
import eyed3
class TestMinero(unittest.TestCase):
    def setUp(self):
        self.minero=Minero()

    def test_minar(self):
        with self.assertRaises(OSError):
            self.minero.minar("~/Music")
        self.minero.minar(self.minero.path)
        self.assertTrue(len(self.minero.listCancion) >0)


    def test_creaCancion(self):
        audiotest=''
        c=None
        path=str(self.minero.path)
        p=Path(path)
        for mp3 in p.iterdir():
            audiotest=eyed3.load(mp3)
            self.assertTrue(type(self.minero.creaCancion(audiotest)) is type(Cancion))

    def test_llenaBase(self):
        pass
