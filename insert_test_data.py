from dao.utilisateur_dao import UtilisateurDAO
from models.utilisateur import Utilisateur

def inserer_donnees_test():
    dao = UtilisateurDAO()

    admin = Utilisateur(
        login="admin",
        password="admin123",
        nom="Diallo",
        prenom="Mamadou",
        email="admin@entreprise.sn",
        role="ADMIN",
        service="Informatique"
    )

    technicien = Utilisateur(
        login="tech1",
        password="tech123",
        nom="Fall",
        prenom="Moussa",
        email="tech1@entreprise.sn",
        role="TECHNICIEN",
        service="Informatique"
    )

    utilisateur = Utilisateur(
        login="user1",
        password="user123",
        nom="Dabo",
        prenom="Fama",
        email="user1@entreprise.sn",
        role="UTILISATEUR",
        service="Comptabilité"
    )

    dao.create(admin)
    dao.create(technicien)
    dao.create(utilisateur)

    print("Données de test insérées avec succès !")

if __name__ == "__main__":
    inserer_donnees_test()