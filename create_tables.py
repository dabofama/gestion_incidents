
from database.connexion import DatabaseConnection

def creer_tables():
    db = DatabaseConnection()
    if not db.connect():
        print("Erreur de connexion")
        return
    try:
        # Table utilisateur
        db.execute("""
        CREATE TABLE IF NOT EXISTS utilisateur (
        id INT AUTO_INCREMENT PRIMARY KEY ,
        login VARCHAR(32) UNIQUE NOT NULL,
        password VARCHAR(32) NOT NULL,
        nom VARCHAR(32) NOT NULL,
        prenom VARCHAR(32) NOT NULL,
        email VARCHAR(32) NOT NULL,
        role ENUM ('UTILISATEUR', 'TECHNICIEN', 'ADMIN'),
        service VARCHAR(32) NOT NULL,
        date_creation DATE DEFAULT (CURRENT_DATE)
        )
        """)
        ##Table incident
        db.execute("""
        CREATE TABLE IF NOT EXISTS incident (
        id INT AUTO_INCREMENT PRIMARY KEY ,
        titre VARCHAR(32) NOT NULL,
        description TEXT NOT NULL,
        priorite ENUM ('BASSE', 'MOYENNE', 'HAUTE','CRITIQUE'),
        statut ENUM ('OUVERT', 'EN_COURS', 'RESOLU', 'FERME'),
        date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
        utilisateur_id INT NOT NULL,
        FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id)
        )
        """)

        ##Table intervention
        db.execute("""
        CREATE TABLE IF NOT EXISTS intervention (
        id INT AUTO_INCREMENT PRIMARY KEY ,
        commentaire TEXT NOT NULL,
        duree_minutes INT DEFAULT 0,
        date_intervention DATETIME DEFAULT CURRENT_TIMESTAMP,
        incident_id INT NOT NULL,
        technicien_id INT NOT NULL,
        FOREIGN KEY (incident_id) REFERENCES incident(id),
        FOREIGN KEY (technicien_id) REFERENCES utilisateur(id)
        )
        """)

        db.commit()
        print("Table creer avec succee!!")

    except Exception as e:
        db.rollback()
        print(f"Erreur lors de la creation de tables {e}")

if __name__ == "__main__":
    creer_tables()

