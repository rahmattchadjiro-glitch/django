from django.db import models

class Personne(models.Model):
    choix_de_sexe = [
        ('M','masculaire'),
        ('F','feminin')
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=choix_de_sexe)
    date_naissance = models.DateField()
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True  

    def __str__(self):
        return f"{self.nom} et {self.prenom}"



