import mysql.connector
from database.config import TYPE_BD,CONFIG

class DatabaseConnection:
    _instance = None
    def __new__(cls):           ##
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.cursor = None

        return cls._instance

    def connect(self):
        try:
            if TYPE_BD == "mysql":
                self.connection = mysql.connector.connect(**CONFIG)
            else:
                print("Type de base de donnees introuvable")
                return False
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Erreur de connexion a la base de donnees:{e}")
            return False

    def disconnect(self):
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
                print(f"Connection fermee")


    def commit(self):
        #valider les modifications
        if self.connection:
            self.connection.commit()

    def rollback(self):
        #annule les modifications
        if self.connection:
            self.connection.rollback()

    def execute(self, query, params=None):
        #Execute une requette sql
        try:
            self.cursor.execute(query, params or ())
            return True
        except Exception as e:
            print(f"Erreur de requette SQL :{e}")
            return False

    def fetchall(self):
        #Recuper tous les resultats
        self.connection.fetchall()

    def fetchone(self):
        #Recuper un seul resultat
        self.connection.fetchone()





