import pyodbc as db
import typer


class Database:

    def __init__(self, name):
        self.name = name
        self._sql = 'CREATE DATABASE ' + self.name + ' COLLATE Latin1_General_CS_AS'

    def create_database(self):
        try:
            connection_string = 'DSN=ETL;'
            conn = db.connect(connection_string)
            csr = conn.cursor()
            csr.execute(self._sql)
            conn.commit()
        except Exception as e:
            typer.echo(e)
        finally:
            csr.close()
            conn.close()
