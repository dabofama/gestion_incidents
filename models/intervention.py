class Intervention:
    def __init__(self, id = None,
                 commentaire = None,
                 duree_minutes = None,
                 date_intervention = None,
                 incident_id = None,
                 technicien_id = None):
        self.id = id
        self.commentaire = commentaire
        self.duree_minutes = duree_minutes
        self.date_intervention = date_intervention
        self.incident_id = incident_id
        self.technicien_id = technicien_id

    def __str__(self):
        return f"INTERVENTION {self.id } | {self.commentaire} | {self.duree_minutes} | {self.date_intervention} | {self.incident_id} | {self.technicien_id}"
