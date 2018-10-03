import unittest
import sqlite3
from basededatos import BaseDeDatos

class TestBaseDeDatos(unittest.TestCase):
    bd=None
    def setUp():
        bd=BaseDeDatos()

    def tearDown():
        bd.cerrar()

    def test_creaBD():
        self.assertEqual(self.bd,None)
        self.assertTrue(self.bd.creaBD())

    def test_creaTablas():
        self.db.creaTablas()

    def test_llenaTablas():
        pass

    def test_comandos():
        pass

    def test_cerrar():
        pass
