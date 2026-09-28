from django.db import models

class Entreprise(models.Model):
    """ Une entreprise suseptible d'acceuillir un stagiaire"""

    nom = models.CharField(max_length = 130,unique=True)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(max_length=80)
    contact = models.CharField()

    class Meta:
        ordering = ["nom"]
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"

    def __str__(self):
        return f"{self.nom} ({self.ville})"






