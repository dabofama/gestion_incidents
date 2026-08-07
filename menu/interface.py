from dao.incident_dao import IncidentDAO
from dao.intervention_dao import InterventionDAO
from dao.utilisateur_dao import UtilisateurDAO
from models.incident import Incident
from models.intervention import Intervention

# ==================== MENU UTILISATEUR ====================

def menu_utilisateur(utilisateur):
    while True:
        print("\n" + "=" * 40)
        print(f"MENU UTILISATEUR — {utilisateur.prenom} {utilisateur.nom}")
        print("=" * 40)
        print("1. Créer un nouvel incident")
        print("2. Consulter mes incidents")
        print("3. Filtrer mes incidents par statut")
        print("4. Filtrer mes incidents par priorité")
        print("0. Se déconnecter")
        print("=" * 40)

        choix = input("Votre choix : ")

        if choix == "1":
            creer_incident(utilisateur)
        elif choix == "2":
            mes_incidents(utilisateur)
        elif choix == "3":
            filtrer_par_statut(utilisateur)
        elif choix == "4":
            filtrer_par_priorite(utilisateur)
        elif choix == "0":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide !")

def creer_incident(utilisateur):
    print("\n--- Créer un incident ---")
    titre = input("Titre : ")
    description = input("Description : ")
    print("Priorité : 1.BASSE  2.MOYENNE  3.HAUTE  4.CRITIQUE")
    choix = input("Votre choix : ")
    priorites = {"1": "BASSE", "2": "MOYENNE", "3": "HAUTE", "4": "CRITIQUE"}
    priorite = priorites.get(choix)
    if not priorite:
        print(" Priorité invalide !")
        return
    incident = Incident(
        titre=titre,
        description=description,
        priorite=priorite,
        utilisateur_id=utilisateur.id
    )
    dao = IncidentDAO()
    dao.create(incident)

def mes_incidents(utilisateur):
    print("\n--- Mes incidents ---")
    dao = IncidentDAO()
    incidents = dao.get_by_utilisateur(utilisateur.id)
    if not incidents:
        print("Aucun incident trouvé.")
        return
    for i in incidents:
        print(f"ID:{i['id']} | {i['titre']} | {i['priorite']} | {i['statut']}")

def filtrer_par_statut(utilisateur):
    print("\nStatut : 1.OUVERT  2.EN_COURS  3.RESOLU  4.FERME")
    choix = input("Votre choix : ")
    statuts = {"1": "OUVERT", "2": "EN_COURS", "3": "RESOLU", "4": "FERME"}
    statut = statuts.get(choix)
    if not statut:
        print(" Statut invalide !")
        return
    dao = IncidentDAO()
    incidents = dao.get_by_utilisateur(utilisateur.id)
    filtres = [i for i in incidents if i["statut"] == statut]
    if not filtres:
        print("Aucun incident trouvé.")
        return
    for i in filtres:
        print(f"ID:{i['id']} | {i['titre']} | {i['priorite']} | {i['statut']}")

def filtrer_par_priorite(utilisateur):
    print("\nPriorité : 1.BASSE  2.MOYENNE  3.HAUTE  4.CRITIQUE")
    choix = input("Votre choix : ")
    priorites = {"1": "BASSE", "2": "MOYENNE", "3": "HAUTE", "4": "CRITIQUE"}
    priorite = priorites.get(choix)
    if not priorite:
        print(" Priorité invalide !")
        return
    dao = IncidentDAO()
    incidents = dao.get_by_utilisateur(utilisateur.id)
    filtres = [i for i in incidents if i["priorite"] == priorite]
    if not filtres:
        print("Aucun incident trouvé.")
        return
    for i in filtres:
        print(f"ID:{i['id']} | {i['titre']} | {i['priorite']} | {i['statut']}")

# ==================== MENU TECHNICIEN ====================

def menu_technicien(utilisateur):
    while True:
        print("\n" + "=" * 40)
        print(f"MENU TECHNICIEN — {utilisateur.prenom} {utilisateur.nom}")
        print("=" * 40)
        print("1. Voir les incidents OUVERTS et EN_COURS")
        print("2. Prendre en charge un incident")
        print("3. Ajouter une intervention")
        print("4. Résoudre un incident")
        print("5. Fermer un incident")
        print("6. Mon historique d'interventions")
        print("0. Se déconnecter")
        print("=" * 40)

        choix = input("Votre choix : ")

        if choix == "1":
            voir_incidents_ouverts()
        elif choix == "2":
            prendre_en_charge()
        elif choix == "3":
            ajouter_intervention(utilisateur)
        elif choix == "4":
            resoudre_incident()
        elif choix == "5":
            fermer_incident()
        elif choix == "6":
            mon_historique(utilisateur)
        elif choix == "0":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide !")

def voir_incidents_ouverts():
    print("\n--- Incidents OUVERTS et EN_COURS ---")
    dao = IncidentDAO()
    incidents = dao.get_ouverts_et_en_cours()
    if not incidents:
        print("Aucun incident trouvé.")
        return
    for i in incidents:
        print(f"ID:{i['id']} | {i['titre']} | {i['priorite']} | {i['statut']}")

def prendre_en_charge():
    print("\n--- Prendre en charge un incident ---")
    id_incident = input("ID de l'incident : ")
    dao = IncidentDAO()
    dao.update_statut(int(id_incident), "EN_COURS")

def ajouter_intervention(utilisateur):
    print("\n--- Ajouter une intervention ---")
    id_incident = input("ID de l'incident : ")
    commentaire = input("Commentaire : ")
    duree = input("Durée en minutes : ")
    intervention = Intervention(
        commentaire=commentaire,
        duree_minutes=int(duree),
        incident_id=int(id_incident),
        technicien_id=utilisateur.id
    )
    dao = InterventionDAO()
    dao.create(intervention)

def resoudre_incident():
    print("\n--- Résoudre un incident ---")
    id_incident = input("ID de l'incident : ")
    dao = IncidentDAO()
    dao.update_statut(int(id_incident), "RESOLU")

def fermer_incident():
    print("\n--- Fermer un incident ---")
    id_incident = input("ID de l'incident : ")
    dao = IncidentDAO()
    dao.update_statut(int(id_incident), "FERME")

def mon_historique(utilisateur):
    print("\n--- Mon historique d'interventions ---")
    dao = InterventionDAO()
    interventions = dao.get_by_technicien(utilisateur.id)
    if not interventions:
        print("Aucune intervention trouvée.")
        return
    for i in interventions:
        print(f"ID:{i['id']} | Incident:{i['incident_id']} | {i['commentaire']} | {i['duree_minutes']} min")


# ==================== MENU ADMIN ====================

def menu_admin(utilisateur):
    while True:
        print("\n" + "=" * 40)
        print(f"MENU ADMIN — {utilisateur.prenom} {utilisateur.nom}")
        print("=" * 40)
        print("--- Gestion Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Liste de tous les utilisateurs")
        print("3. Rechercher un utilisateur")
        print("4. Modifier un utilisateur")
        print("5. Supprimer un utilisateur")
        print("--- Gestion Incidents ---")
        print("6. Voir tous les incidents")
        print("7. Voir les incidents OUVERTS et EN_COURS")
        print("8. Prendre en charge un incident")
        print("9. Ajouter une intervention")
        print("10. Résoudre un incident")
        print("11. Fermer un incident")
        print("12. Mon historique d'interventions")
        print("--- Statistiques ---")
        print("13. Voir les statistiques")
        print("0. Se déconnecter")
        print("=" * 40)

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_utilisateur()
        elif choix == "2":
            liste_utilisateurs()
        elif choix == "3":
            rechercher_utilisateur()
        elif choix == "4":
            modifier_utilisateur()
        elif choix == "5":
            supprimer_utilisateur()
        elif choix == "6":
            tous_les_incidents()
        elif choix == "7":
            voir_incidents_ouverts()
        elif choix == "8":
            prendre_en_charge()
        elif choix == "9":
            ajouter_intervention(utilisateur)
        elif choix == "10":
            resoudre_incident()
        elif choix == "11":
            fermer_incident()
        elif choix == "12":
            mon_historique(utilisateur)
        elif choix == "13":
            statistiques()
        elif choix == "0":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide !")

# ---- Fonctions CRUD Utilisateurs ----

def ajouter_utilisateur():
    from models.utilisateur import Utilisateur
    print("\n--- Ajouter un utilisateur ---")
    login = input("Login : ")
    password = input("Mot de passe : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    email = input("Email : ")
    print("Rôle : 1.UTILISATEUR  2.TECHNICIEN  3.ADMIN")
    choix = input("Votre choix : ")
    roles = {"1": "UTILISATEUR", "2": "TECHNICIEN", "3": "ADMIN"}
    role = roles.get(choix)
    if not role:
        print(" Rôle invalide !")
        return
    service = input("Service : ")
    utilisateur = Utilisateur(
        login=login, password=password, nom=nom,
        prenom=prenom, email=email, role=role, service=service
    )
    dao = UtilisateurDAO()
    dao.create(utilisateur)

def liste_utilisateurs():
    print("\n--- Liste des utilisateurs ---")
    dao = UtilisateurDAO()
    utilisateurs = dao.get_all()
    if not utilisateurs:
        print("Aucun utilisateur trouvé.")
        return
    for u in utilisateurs:
        print(f"ID:{u['id']} | {u['login']} | {u['nom']} {u['prenom']} | {u['role']} | {u['service']}")

def rechercher_utilisateur():
    print("\n--- Rechercher un utilisateur ---")
    terme = input("Rechercher (nom, login ou service) : ")
    dao = UtilisateurDAO()
    resultats = dao.rechercher(terme)
    if not resultats:
        print("Aucun utilisateur trouvé.")
        return
    for u in resultats:
        print(f"ID:{u['id']} | {u['login']} | {u['nom']} {u['prenom']} | {u['role']} | {u['service']}")

def modifier_utilisateur():
    from models.utilisateur import Utilisateur
    print("\n--- Modifier un utilisateur ---")
    id_user = input("ID de l'utilisateur à modifier : ")
    dao = UtilisateurDAO()
    data = dao.get_by_id(int(id_user))
    if not data:
        print(" Utilisateur introuvable !")
        return
    print(f"Utilisateur actuel : {data['login']} | {data['nom']} | {data['role']}")
    login = input(f"Nouveau login ({data['login']}) : ") or data['login']
    nom = input(f"Nouveau nom ({data['nom']}) : ") or data['nom']
    prenom = input(f"Nouveau prénom ({data['prenom']}) : ") or data['prenom']
    email = input(f"Nouvel email ({data['email']}) : ") or data['email']
    service = input(f"Nouveau service ({data['service']}) : ") or data['service']
    print("Rôle : 1.UTILISATEUR  2.TECHNICIEN  3.ADMIN")
    choix = input(f"Nouveau rôle ({data['role']}) : ")
    roles = {"1": "UTILISATEUR", "2": "TECHNICIEN", "3": "ADMIN"}
    role = roles.get(choix) or data['role']
    utilisateur = Utilisateur(
        id=int(id_user), login=login, nom=nom,
        prenom=prenom, email=email, role=role, service=service
    )
    dao.update(utilisateur)

def supprimer_utilisateur():
    print("\n--- Supprimer un utilisateur ---")
    id_user = input("ID de l'utilisateur à supprimer : ")
    dao = UtilisateurDAO()
    dao.delete_by_id(int(id_user))

def tous_les_incidents():
    print("\n--- Tous les incidents ---")
    dao = IncidentDAO()
    incidents = dao.get_all()
    if not incidents:
        print("Aucun incident trouvé.")
        return
    for i in incidents:
        print(f"ID:{i['id']} | {i['titre']} | {i['priorite']} | {i['statut']}")

def statistiques():
    print("\n" + "=" * 40)
    print("STATISTIQUES ET RAPPORTS")
    print("=" * 40)

    dao = IncidentDAO()

    # 1. Incidents par statut
    print("\n Incidents par statut :")
    dao.cursor.execute("SELECT statut, COUNT(*) as total FROM incident GROUP BY statut")
    resultats = dao.cursor.fetchall()
    if resultats:
        for r in resultats:
            print(f"  {r['statut']} : {r['total']}")
    else:
        print("  Aucune donnée.")

    # 2. Incidents par priorité
    print("\n Incidents par priorité :")
    dao.cursor.execute("SELECT priorite, COUNT(*) as total FROM incident GROUP BY priorite")
    resultats = dao.cursor.fetchall()
    if resultats:
        for r in resultats:
            print(f"  {r['priorite']} : {r['total']}")
    else:
        print("  Aucune donnée.")

    # 3. Top 3 techniciens les plus actifs
    print("\n Top 3 techniciens les plus actifs :")
    dao.cursor.execute("""
        SELECT u.nom, u.prenom, COUNT(i.id) as nb_interventions
        FROM intervention i
        JOIN utilisateur u ON i.technicien_id = u.id
        GROUP BY i.technicien_id
        ORDER BY nb_interventions DESC
        LIMIT 3
    """)
    resultats = dao.cursor.fetchall()
    if resultats:
        for r in resultats:
            print(f"  {r['nom']} {r['prenom']} : {r['nb_interventions']} interventions")
    else:
        print("  Aucune donnée.")

