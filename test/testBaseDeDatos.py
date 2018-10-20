import unittest
import sys
sys.path.append('../..')
import sqlite3
from basededatos import BaseDeDatos

class TestBaseDeDatos(unittest.TestCase):
    bd=None
    def setUp(self):
        self.bd=BaseDeDatos()

    def tearDown(self):
        self.bd.cerrar()

    def test_creaBD(self):
        self.assertTrue(self.bd.creaBD())

    def test_creaTablas(self):
        self.bd.creaTablas()

    def test_llenaTablas(self):
        pass

    def test_comandos(self):
        pass

    def test_cerrar(self):
        pass
