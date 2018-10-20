#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os.path
from cancion import Cancion

class BaseDeDatos():
    """Clase BaseDeDatos que crea una base de datos en la que
    guarda las canciones, los albumes y artistas
    """

    def __init__(self):
        """Constructor de la clase.
        Parámetros
        exist : bool
            Un booleano que dice si existe la base de datos o no.
        con : None
            Conexión con la base de datos,se inicia como None.
        """
        self.exist=False
        self.con=None
        self.creaBD()

    def creaBD(self):
        """Checa si ya existe la base de datos, si es así solo se
        conecta a ella y llama al metodo creaTablas, sino crea una nueva base.
        """
        if os.path.isfile("bdmusical.bd"):
            self.con=sqlite3.connect("bdmusical.bd")
            self.cursor=self.con.cursor()
            self.exist=True
        else:
            self.con=sqlite3.connect("bdmusical.bd")
            self.cursor=self.con.cursor()
            self.creaTablas()

    def creaTablas(self):
        """Crea las tablas necesarias para la base de datos.
        """
        self.con.execute('''CREATE TABLE types (
            id_type       INTEGER PRIMARY KEY,
            description   TEXT
        )''')
        self.con.execute('''INSERT INTO types VALUES(0,'Person')''')
        self.con.execute('''INSERT INTO types VALUES(1,'Group')''')
        self.con.execute('''INSERT INTO types VALUES(2,'Unknown')''')

        self.con.execute('''CREATE TABLE performers (
            id_performer  INTEGER PRIMARY KEY,
            id_type       INTEGER,
            name          TEXT,
            FOREIGN KEY   (id_type) REFERENCES types(id_type)
        )''')

        self.con.execute('''CREATE TABLE persons (
            id_person     INTEGER PRIMARY KEY,
            stage_name    TEXT,
            real_name     TEXT,
            birth_date    TEXT,
            death_date    TEXT
        )''')

        self.con.execute('''CREATE TABLE groups (
            id_group      INTEGER PRIMARY KEY,
            name          TEXT,
            start_date    TEXT,
            end_date      TEXT
        )''')

        self.con.execute('''CREATE TABLE albums (
            id_album      INTEGER PRIMARY KEY,
            path          TEXT,
            name          TEXT,
            year          INTEGER
        )''')

        self.con.execute('''CREATE TABLE songs (
            id_song      INTEGER PRIMARY KEY,
            id_performer  INTEGER,
            id_album      INTEGER,
            path          TEXT,
            title         TEXT,
            track         INTEGER,
            year          INTEGER,
            genre         TEXT,
            FOREIGN KEY   (id_performer) REFERENCES performers(id_performer),
            FOREIGN KEY   (id_album) REFERENCES albums(id_album)
        )''')

        self.con.execute('''CREATE TABLE in_group (
            id_person     INTEGER,
            id_group      INTEGER,
            PRIMARY KEY   (id_person, id_group),
            FOREIGN KEY   (id_person) REFERENCES persons(id_person),
            FOREIGN KEY   (id_group) REFERENCES  groups(id_group)
        )''')
        self.con.commit()

    def llenaTablas(self,tabla,lista):
        """Llena la tabla correspondiente con los datos de la lista.
        Parámetros
        tabla : str
            El nombre de la tabla a llenar.
        lista : [str]
            La lista con los datos a guardar.
        """
        p=""
        if tabla == "songs":
            self.cursor.execute('''SELECT id_performer
                                    FROM performers
                                    WHERE name= ? ''', (lista[5],))
            r=self.cursor.fetchone()
            p=r[0]
            self.cursor=self.con.execute('''SELECT id_album
                                            FROM albums
                                            WHERE name=?''',(lista[6],))
            r=self.cursor.fetchone()
            a=r[0]
            self.con.execute('''INSERT INTO songs (id_performer,id_album,path,title,track,year,genre)\
                                VALUES(?,?,?,?,?,?,?)''',\
            (p,a,lista[0],lista[1],lista[2],lista[3],lista[4]))
            self.con.commit()

        if tabla == "albums":
            self.cursor.execute('''SELECT id_album
                                    FROM albums
                                    WHERE name=?''',(lista[1],))
            if self.cursor.fetchone() == None:
                self.con.execute('''INSERT INTO albums (path,name,year)
                                    VALUES(?,?,?)''', \
             (lista[0],lista[1],lista[2]))
                self.con.commit()
            else:
                return

        if tabla == "performers":
            self.cursor.execute('''SELECT id_performer
                                    FROM performers
                                    WHERE name= ? ''', (lista[1],))
            if self.cursor.fetchone() == None:
                self.con.execute('''INSERT INTO performers(id_type,name)
                                    VALUES(?,?)''',(lista[0],lista[1]))
                self.con.commit()
            else:
                return
        if tabla == "groups":
            self.cursor.execute('''INSERT INTO groups (name,start_date, end_date)
                                   VALUES(?,?,?)''' , (lista[0],lista[1],lista[2]))
            self.con.commit()
        if tabla == "persons":
            self.cursor.execute('''INSERT INTO persons (stage_name,real_name,birth_date,death_date)
                                    VALUES(?,?,?,?)''', (lista[0],lista[1],lista[2],lista[3]))
            self.con.commit()
        if tabla == "in_group":
            self.cursor.execute('''SELECT id_person FROM persons
                                    WHERE stage_name=?''',(lista[0],))
            r=self.cursor.fetchone()
            p=r[0]
            self.cursor.execute('''SELECT id_group FROM groups
                                    WHERE name=?''',(lista[1],))
            r=self.cursor.fetchone()
            g=r[0]
            self.cursor.execute('''INSERT INTO in_group (id_person, id_group)
                                    VALUES(?,?)''', (p ,g))
            self.con.commit()

    def consulta(self,consulta,tipo):
        """Consulta la base de datos y regresa un cursor.
        Parámetros
        consulta : str
            Lo que se busca dentro de la base de datos.
        tipo : str
            El tipo de consulta.
        """
        if tipo == "todo":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name
            FROM performers
            INNER JOIN songs ON performers.id_performer=songs.id_performer
            INNER JOIN albums ON albums.id_album=songs.id_album
            ORDER BY performers.name''')
            return self.cursor
        if tipo == "artista":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name
            FROM performers
            INNER JOIN songs ON performers.id_performer=songs.id_performer
            INNER JOIN albums ON albums.id_album=songs.id_album
            WHERE performers.name LIKE ?
            ORDER BY performers.name ''', ('%'+consulta+'%',))
            return self.cursor
        if tipo == "cancion":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name
            FROM performers
            INNER JOIN songs ON performers.id_performer=songs.id_performer
            INNER JOIN albums ON albums.id_album=songs.id_album
            WHERE songs.title LIKE ?
            ORDER BY performers.name''', ('%'+consulta+'%',))
            return self.cursor
        if tipo== "album":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name
            FROM performers
            INNER JOIN songs ON performers.id_performer=songs.id_performer
            INNER JOIN albums ON albums.id_album=songs.id_album
            WHERE albums.name LIKE ?
            ORDER BY performers.name ''', ('%'+consulta+'%',))
            return self.cursor
        if tipo == "persons":
            self.cursor.execute('''SELECT persons.stage_name FROM persons
                                    ORDER BY persons.stage_name''')
            return self.cursor
        if tipo == "groups":
            self.cursor.execute('''SELECT groups.name FROM groups
                                    ORDER BY groups.name''')
            return self.cursor

    def comandos(self,comando):
        """Pequeño compilador que detecta el tipo de consulta que hace el usuario
        Parámetros
        comando : str
            La consulta del usuario con un determinado comando.
        """
        if comando is None:
            return self.consulta(comando, "todo")
        elif "A:" in comando:
            comando=comando.replace("A: ","")
            return self.consulta(comando,"artista")
        elif "AM:" in comando:
            comando=comando.replace("AM: ","")
            return self.consulta(comando,"album")
        elif "S:" in comando:
            comando=comando.replace("S: ","")
            return self.consulta(comando,"cancion")

    def cerrar():
        """Cierra la conexión con la base de datos
        """
        self.con.close(self)
