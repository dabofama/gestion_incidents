# Gestion des Tickets d'Incidents

Application console en Python (POO) avec base de données MySQL pour la gestion des incidents informatiques (Help Desk).

---

## Membre du groupe

| Nom | Prénom |
|-----|--------|
|Dabo |  Fama  |

---

## Description du projet

La DSI d'une grande entreprise sénégalaise souhaite mettre en place un système de gestion des incidents informatiques. Cette application permet :

- Aux **utilisateurs** de signaler des incidents
- Aux **techniciens** de prendre en charge et résoudre les incidents
- À l'**administrateur** de gérer les utilisateurs et de superviser l'ensemble

---

##  Structure de la base de données

3 tables principales :
- `utilisateur` — stocke tous les comptes (utilisateurs, techniciens, admins)
- `incident` — stocke tous les tickets d'incidents
- `intervention` — stocke les interventions des techniciens sur les incidents

---

## Workflow des statuts

```
OUVERT → EN_COURS → RESOLU → FERME
```

---

## Architecture du projet

```
gestion_incidents/
├── database/
│   ├── config.py         # Configuration de la base de données
│   └── connexion.py      # Singleton de connexion MySQL
├── models/
│   ├── utilisateur.py    # Classe Utilisateur
│   ├── incident.py       # Classe Incident
│   └── intervention.py   # Classe Intervention
├── dao/
│   ├── base_dao.py       # Classe abstraite BaseDAO
│   ├── utilisateur_dao.py
│   ├── incident_dao.py
│   └── intervention_dao.py
├── menu/
│   ├── auth.py           # Authentification
│   └── interface.py      # Menus par rôle
├── create_tables.py      # Création des tables
├── insert_test_data.py   # Données de test
├── requirements.txt
└── main.py               # Point d'entrée
```

---

##  Installation

### Prérequis
- Python 3.10+
- MySQL 8.0+

### Étapes

**1. Cloner le dépôt**
```bash
git clone https://github.com/dabofama/gestion_incidents.git
cd gestion_incidents
```

**2. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3. Créer la base de données MySQL**
```sql
CREATE DATABASE gestion_incidents;
```

**4. Configurer la connexion**

Modifier le fichier `database/config.py` :
```python
CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "votre_mot_de_passe",
    "database": "gestion_incidents"
}
```

**5. Créer les tables**
```bash
python create_tables.py
```

**6. Insérer les données de test**
```bash
python insert_test_data.py
```

**7. Lancer l'application**
```bash
python main.py
```

---

##  Utilisation

Au lancement, l'application demande un login et un mot de passe.

### Comptes de test

| Login | Mot de passe | Rôle |
|-------|-------------|------|
| admin | admin123 | ADMIN |
| tech1 | tech123 | TECHNICIEN |
| user1 | user123 | UTILISATEUR |

### Menus disponibles

**UTILISATEUR**
- Créer un incident
- Consulter mes incidents
- Filtrer par statut ou priorité

**TECHNICIEN**
- Voir les incidents ouverts
- Prendre en charge un incident
- Ajouter une intervention
- Résoudre / Fermer un incident

**ADMIN**
- Toutes les fonctions technicien
- Gestion complète des utilisateurs (CRUD)
- Statistiques et rapports

---

## Technologies utilisées

- **Python 3.10+** — Langage principal
- **MySQL** — Base de données
- **mysql-connector-python** — Connecteur Python/MySQL
- **POO** — Programmation Orientée Objet (héritage, abstraction, Singleton)


---

## Concepts POO utilisés

- **Singleton** — Une seule instance de connexion à la base de données
- **Héritage** — `BaseDAO` héritée par tous les DAO
- **Abstraction** — Méthodes génériques dans `BaseDAO`
- **Encapsulation** — Attributs privés dans les classes modèles

---

##  Enseignant

M. DIALLO — Licence 2 Génie Logiciel — Groupe ISI
