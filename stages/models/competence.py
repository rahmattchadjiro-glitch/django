from django.db import models


class Competence(models.Model):
    libelle = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.libelle



