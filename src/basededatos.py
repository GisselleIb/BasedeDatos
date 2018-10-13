import sqlite3
import os.path
from cancion import Cancion

class BaseDeDatos():

    def __init__(self):
        self.exist=False
        self.con=None
        self.creaBD()
    def creaBD(self):
        if os.path.isfile("bdmusical.bd"):
            self.con=sqlite3.connect("bdmusical.bd")
            self.cursor=self.con.cursor()
            self.exist=True
            print("here")
        else:
            self.con=sqlite3.connect("bdmusical.bd")
            self.cursor=self.con.cursor()
            self.creaTablas()
            print("Base de datos creada")

    def creaTablas(self):
        print("creando")
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
                self.con.execute('''INSERT INTO performers(id_type,name) \
                                    VALUES(?,?)''',(lista[0],lista[1]))
                self.con.commit()
            else:
                return

    def consulta(self,consulta,tipo):
        if tipo == "todo":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name
            FROM performers
            INNER JOIN songs ON performers.id_performer=songs.id_performer
            INNER JOIN albums ON albums.id_album=songs.id_album \
            ''')
            for row in self.cursor:
                print(row[0],row[1],row[2],row[3])
                return self.cursor
        if tipo == "artista":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name \
            FROM performers \
            INNER JOIN songs ON performers.id_performer=songs.id_performer \
            INNER JOIN albums ON albums.id_album=songs.id_album \
            WHERE performers.name= ? ''', (consulta,))
            for row in self.cursor:
                print(row[0],row[1],row[2],row[3])
            return self.cursor
        if tipo == "cancion":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name \
            FROM performers \
            INNER JOIN songs ON performers.id_performer=songs.id_performer \
            INNER JOIN albums ON albums.id_album=songs.id_album \
            WHERE songs.title= ? ''', (consulta,))
            for row in self.cursor:
                print(row[0],row[1],row[2],row[3])
            return self.cursor
        if tipo== "album":
            self.cursor.execute('''SELECT performers.name,songs.title,songs.genre,albums.name \
            FROM performers \
            INNER JOIN songs ON performers.id_performer=songs.id_performer \
            INNER JOIN albums ON albums.id_album=songs.id_album \
            WHERE albums.name= ? ''', (consulta,))
            for row in self.cursor:
                print(row[0],row[1],row[2],row[3])
            return self.cursor

    def comandos(self,comando):
        if "A:" in comando:
            comando.replace("A:","")
            self.consulta(comando)
        if "AM:" in comando:
            comando.replace("AM:","")
            self.consulta(comando)
        if "S:" in comando:
            comando.replace("S:","")
            self.consulta(comando)

    def cerrar():
        self.con.close(self)
