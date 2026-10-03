from django.db import models
from .personne import Personne

class TuteurEntreprise(Personne):
    entreprise = models.ForeignKey('Entreprise', on_delete=models.PROTECT, related_name='tuteur_entreprise')

    def __str__(self):
        return f"{self.prenom} {self.nom} (Tuteur - {self.entreprise.nom})"
