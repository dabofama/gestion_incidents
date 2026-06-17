from dao.base_dao import BaseDAO
from models.utilisateur import Utilisateur
from database.connexion import DatabaseConnection

class UtilisateurDAO(BaseDAO):

    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()
        self.cursor = self.db.cursor

    def get_all(self):
        try:
            self.cursor.execute("SELECT * FROM utilisateur")
            return self.cursor.fetchall()
        except Exception as e:
            print(f" Erreur get_all : {e}")
            return []

    def get_by_id(self, id):
        try:
            self.cursor.execute("SELECT * FROM utilisateur WHERE id = %s", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f" Erreur get_by_id : {e}")
            return None

    def get_by_login(self, login):
        try:
            self.cursor.execute(
                "SELECT * FROM utilisateur WHERE login = %s", (login,)
            )
            return self.cursor.fetchone()
        except Exception as e:
            print(f" Erreur d affichage : {e}")
            return None


    def delete_by_id(self, id):
            try:
                self.cursor.execute(
                    "SELECT COUNT(*) as total FROM incident WHERE utilisateur_id = %s", (id,)
                )
                result_incidents = self.cursor.fetchone()

                if result_incidents["total"] > 0:
                    print(" Impossible de supprimer : cet utilisateur a des incidents !")
                    return False

                self.cursor.execute(
                    "SELECT COUNT(*) as total FROM intervention WHERE technicien_id = %s", (id,)
                )
                result_interventions = self.cursor.fetchone()

                if result_interventions["total"] > 0:
                    print("Impossible de supprimer : cet utilisateur a des interventions !")
                    return False

                self.cursor.execute("DELETE FROM utilisateur WHERE id = %s", (id,))
                self.db.commit()
                print("Utilisateur supprimé avec succès !")
                return True

            except Exception as e:
                self.db.rollback()
                print(f"Erreur delete_by_id : {e}")
                return False

    def create(self, utilisateur):
        try:
            self.cursor.execute(
                "INSERT INTO utilisateur (login, password, nom, prenom, email, role, service) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    utilisateur.login,
                    utilisateur.password,
                    utilisateur.nom,
                    utilisateur.prenom,
                    utilisateur.email,
                    utilisateur.role,
                    utilisateur.service
                )
            )
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f" Erreur de creation : {e}")

    def update(self, utilisateur):
        try:
            self.cursor.execute(
                "UPDATE utilisateur SET login=%s, nom=%s, prenom=%s, "
                "email=%s, role=%s, service=%s WHERE id=%s",
                (
                    utilisateur.login,
                    utilisateur.nom,
                    utilisateur.prenom,
                    utilisateur.email,
                    utilisateur.role,
                    utilisateur.service,
                    utilisateur.id
                )
            )
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f" Erreur update : {e}")

    def authenticate(self, login, password):
        try:
            self.cursor.execute(
                "SELECT * FROM utilisateur WHERE login=%s AND password=%s",
                (login, password)
            )
            data = self.cursor.fetchone()
            if data:

                return Utilisateur(
                    id=data["id"],
                    login=data["login"],
                    password=data["password"],
                    nom=data["nom"],
                    prenom=data["prenom"],
                    email=data["email"],
                    role=data["role"],
                    service=data["service"],
                    date_creation=data["date_creation"]
                )
            return None
        except Exception as e:
            print(f" Erreur authenticate : {e}")
            return None

    def rechercher(self, terme):
        try:
            self.cursor.execute(
                "SELECT * FROM utilisateur WHERE nom LIKE %s OR login LIKE %s OR service LIKE %s",
                (f"%{terme}%", f"%{terme}%", f"%{terme}%")
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f" Erreur rechercher : {e}")
            return []