import unittest
from src.minero import Minero
from src.cancion import Cancion
class TestMinero(unittest.TestCase):
    minero=Minero()

    def test_minar():
        pass

    def test_creaCancion():
        audiotest=''
        c=None
        path=str(self.minero.path)+'/Music'
        p=Path(dir)
        for mp3 in path.iterdir():
            audiotest=eyed3.load(mp3)
            self.assertTrue(type(self.minero.creaCancion(audiotest)) is type(Cancion))

    def test_llenaBase():
        pass
