from django.db import models

class Stage(models.Model):
    sujet = models.CharField(max_length=250)
    candidature = models.OneToOneField('Candidature', on_delete=models.PROTECT, related_name='stage')
    tuteur = models.ForeignKey('TuteurEntreprise', on_delete=models.PROTECT, related_name='stages')
    enseignant = models.ForeignKey('EnseignantReferent', on_delete=models.PROTECT, related_name='stages')

    def __str__(self):
        return f"Stage : {self.sujet}"




