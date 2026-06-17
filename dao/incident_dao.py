from dao.base_dao import BaseDAO
from models.incident import Incident
from database.connexion import DatabaseConnection

class IncidentDAO(BaseDAO):

    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()
        self.cursor = self.db.cursor

    def get_all(self):
        try:
            self.cursor.execute("SELECT * FROM incident")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur get_all : {e}")
            return []

    def get_by_id(self, id):
        try:
            self.cursor.execute("SELECT * FROM incident WHERE id = %s", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erreur get_by_id : {e}")
            return None

    def delete_by_id(self, id):
        try:

            self.cursor.execute(
                "SELECT COUNT(*) as total FROM intervention WHERE incident_id = %s", (id,)
            )
            result = self.cursor.fetchone()

            if result["total"] > 0:
                print("Impossible de supprimer : cet incident a des interventions !")
                return False

            self.cursor.execute("DELETE FROM incident WHERE id = %s", (id,))
            self.db.commit()
            print("Incident supprimé avec succès !")
            return True

        except Exception as e:
            self.db.rollback()
            print(f"Erreur delete_by_id : {e}")
            return False

    def create(self, incident):
        try:
            self.cursor.execute(
                "INSERT INTO incident (titre, description, priorite, statut, utilisateur_id) "
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    incident.titre,
                    incident.description,
                    incident.priorite,
                    incident.statut,
                    incident.utilisateur_id
                )
            )
            self.db.commit()
            print("Incident créé avec succès !")
        except Exception as e:
            self.db.rollback()
            print(f"Erreur create : {e}")

    def update_statut(self, id, nouveau_statut):

        transitions = {
            "OUVERT": "EN_COURS",
            "EN_COURS": "RESOLU",
            "RESOLU": "FERME"
        }
        try:

            self.cursor.execute(
                "SELECT statut FROM incident WHERE id = %s", (id,)
            )
            result = self.cursor.fetchone()

            if not result:
                print("Incident introuvable !")
                return False

            statut_actuel = result["statut"]

            # 2. Vérifier si la transition est autorisée
            if transitions.get(statut_actuel) != nouveau_statut:
                print(f"Transition interdite : {statut_actuel} → {nouveau_statut}")
                return False

            self.cursor.execute(
                "UPDATE incident SET statut = %s WHERE id = %s",
                (nouveau_statut, id)
            )
            self.db.commit()
            print(f"Statut mis à jour : {statut_actuel} → {nouveau_statut}")
            return True

        except Exception as e:
            self.db.rollback()
            print(f"Erreur update_statut : {e}")
            return False

    def get_by_utilisateur(self, utilisateur_id):
        try:
            self.cursor.execute(
                "SELECT * FROM incident WHERE utilisateur_id = %s", (utilisateur_id,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur get_by_utilisateur : {e}")
            return []

    def get_by_statut(self, statut):
        try:
            self.cursor.execute(
                "SELECT * FROM incident WHERE statut = %s", (statut,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur get_by_statut : {e}")
            return []

    def get_by_priorite(self, priorite):
        try:
            self.cursor.execute(
                "SELECT * FROM incident WHERE priorite = %s", (priorite,)
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur get_by_priorite : {e}")
            return []

    def get_ouverts_et_en_cours(self):
        try:
            self.cursor.execute(
                "SELECT * FROM incident WHERE statut IN ('OUVERT', 'EN_COURS')"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur d affichage : {e}")
            return []