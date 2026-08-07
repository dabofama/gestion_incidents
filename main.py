from menu.auth import connexion
from menu.interface import menu_utilisateur, menu_technicien, menu_admin

def main():
    utilisateur = connexion()

    if utilisateur is None:
        print(" Connexion échouée. Au revoir !")
        return

    # Redirection selon le rôle
    if utilisateur.role == "UTILISATEUR":
        menu_utilisateur(utilisateur)
    elif utilisateur.role == "TECHNICIEN":
        menu_technicien(utilisateur)
    elif utilisateur.role == "ADMIN":
        menu_admin(utilisateur)

if __name__ == "__main__":
    main()