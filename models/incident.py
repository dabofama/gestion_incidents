class Incident:
    def __init__(self,id = None,
                 titre = None,
                 description = None,
                 priorite = None,
                 statut = "OUVERT",
                 date_creation = None,
                 utilisateur_id = None):
        self.id = id
        self.titre = titre
        self.description = description
        self.priorite = priorite
        self.statut = statut
        self.date_creation = date_creation
        self.utilisateur_id = utilisateur_id


    def __str__(self):
        return (f"INCIDENT : {self.id} | {self.titre} | {self.description} | {self.priorite} | "
                f"{self.statut} | {self.date_creation} | {self.utilisateur_id}")
