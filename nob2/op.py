# crud, create, read, update, delete
import sqlite3

class Pessoa:
    def __init__(self, db_string):
        self.db_string = db_string # caminho do banco de dados
        self.con = sqlite3.connect(db_string) # conectando ao banco
        self.cursor = self.con.cursor()

    def create(self, nome, idade):
        query = self.cursor.execute(f"""
        INSERT INTO Pessoas (nome, idade)
        VALUES ('{nome}',{idade});
        """)
        self.con.commit()
    def read(self, idusuario):
        self.idusuario = idusuario
        query = self.cursor.execute(f'''SELECT * FROM Pessoas
                            WHERE id = {idusuario}''')
        return query.fetchall()
    def read_all(self):
        query = self.cursor.execute('SELECT * FROM Pessoas;')
        return query.fetchall()

    def update(self, nome, idade, idusuario):
        query = self.cursor.execute((f'''UPDATE Pessoas
                                        SET nome="{nome}", idade={idade}
                                        WHERE id = {idusuario};'''))
        self.con.commit()
    def delete(self, idusuario):
        self.idusuario = idusuario
        query = self.cursor.execute((f'''DELETE FROM Pessoas
                                        WHERE id = {idusuario}'''))
        self.con.commit()

