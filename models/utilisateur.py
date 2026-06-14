class Utilisateur:
    def __init__(self,id = None,
                 login = None,
                 password = None,
                 nom = None,
                 prenom = None,
                 email = None,
                 role = None,
                 service = None,
                 date_creation = None):
        self.id = id
        self.login = login
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.role = role
        self.service = service
        self.date_creation = date_creation

    def __str__(self):
        return (f"UTILISATEUR {self.id} | {self.login} | {self.nom} | {self.prenom} |"
                f" {self.email} | {self.role} | {self.service} | {self.date_creation}")
