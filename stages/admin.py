from django.contrib import admin

# Register your models here.

from .models import Entreprise
from .models import Etudiant
from .models import Candidature
from .models import Competence
from .models import TuteurEntreprise
from .models import EnseignantReferent
from .models import Offre
from .models import Stage


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","ville","secteur"]
    search_fields = ["nom","ville"]


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'promotion')



@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('libelle',)



@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'entreprise')



@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom')



@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description','date_debut','date_fin','entreprise', 'nb_places')



@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'offre', 'statut','date_depot')



@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('sujet','candidature', 'tuteur', 'enseignant')




