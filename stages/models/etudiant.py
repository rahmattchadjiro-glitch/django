from django.db import models
from .personne import Personne

class Etudiant(Personne):
    matricule = models.CharField(max_length=20, unique=True)
    promotion = models.IntegerField()  
    competences = models.ManyToManyField('Competence', related_name='etudiants', blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"



