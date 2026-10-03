from django.db import models

class Candidature(models.Model):
    choix_de_status = [
        ('deposee', 'Déposée'),
        ('retenue', 'Retenue'),
        ('refusee', 'Refusée'),
    ]
    date_depot = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=15, choices=choix_de_status, default='deposee')
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, related_name='candidatures')
    offre = models.ForeignKey('Offre', on_delete=models.CASCADE, related_name='candidatures')

    class Meta:
        unique_together = ('etudiant', 'offre')

    def __str__(self):
        return f"Candidature de {self.etudiant} pour {self.offre.titre}"





