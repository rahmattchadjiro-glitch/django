from django.db import models
from .personne import Personne

class EnseignantReferent(Personne):
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"


