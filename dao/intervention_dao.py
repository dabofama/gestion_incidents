from dao.base_dao import BaseDAO
from models.intervention import Intervention
from database.connexion import DatabaseConnection

class InterventionDAO(BaseDAO):

    def __init__(self):
        self.db = DatabaseConnection()
        if not self.db.connection or not self.db.connection.is_connected():
            self.db.connect()
        self.cursor = self.db.cursor

    def get_all(self):
        try:
            self.cursor.execute("SELECT * FROM intervention")
            return self.cursor.fetchall()
        except Exception as e:
            print(f" Erreur get_all : {e}")
            return []

    def get_by_id(self, id):
        try:
            self.cursor.execute("SELECT * FROM intervention WHERE id = %s", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f" Erreur get_by_id : {e}")
            return None

    def delete_by_id(self, id):
        try:
            self.cursor.execute("DELETE FROM intervention WHERE id = %s", (id,))
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f" Erreur delete_by_id : {e}")
            return False

    def create(self, intervention):
        try:
            self.cursor.execute(
                "SELECT statut FROM incident WHERE id = %s", (intervention.incident_id,)
            )
            result = self.cursor.fetchone()
            if not result:
                print(" Incident introuvable !")
                return False
            if result["statut"] not in ("OUVERT", "EN_COURS"):
                print(f" Impossible d'ajouter une intervention : statut = {result['statut']}")
                return False
            self.cursor.execute(
                "INSERT INTO intervention (commentaire, duree_minutes, incident_id, technicien_id) "
                "VALUES (%s, %s, %s, %s)",
                (intervention.commentaire, intervention.duree_minutes,
                 intervention.incident_id, intervention.technicien_id)
            )
            self.db.commit()
            print(" Intervention ajoutée avec succès !")
            return True
        except Exception as e:
            self.db.rollback()
            print(f" Erreur create : {e}")
            return False

    def get_by_incident(self, incident_id):
        try:
            self.cursor.execute(
                "SELECT * FROM intervention WHERE incident_id = %s", (incident_id,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f" Erreur get_by_incident : {e}")
            return []

    def get_by_technicien(self, technicien_id):
        try:
            self.cursor.execute(
                "SELECT * FROM intervention WHERE technicien_id = %s", (technicien_id,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f" Erreur get_by_technicien : {e}")
            return []