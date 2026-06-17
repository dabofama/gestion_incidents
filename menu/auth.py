from dao.utilisateur_dao import UtilisateurDAO

def connexion():

    print("=" * 40)
    print("CONNEXION - Gestion des Tickets d'Incidents")
    print("=" * 40)

    login = input("Login: ")
    password = input("Password: ")

    dao = UtilisateurDAO()
    utilisateur = dao.authenticate(login, password)

    if utilisateur is None:
        print("Login ou mot de passe incorrect")
        return None

    print(f"Bienvenue sur {utilisateur.prenom} {utilisateur.nom} {utilisateur.role}")
    return utilisateur
