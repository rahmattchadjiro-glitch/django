from django.db import models

class Offre(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.PositiveIntegerField(default=1)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.PROTECT, related_name='offres')
    competences_attendu = models.ManyToManyField('Competence', related_name='offres')

    def __str__(self):
        return f"{self.titre} - {self.entreprise.nom}"

