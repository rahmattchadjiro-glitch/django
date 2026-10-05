
### 1. les offres des entreprises situées à Sokodé 

```python
from stages.models import Offre

# Recherche des offres dont l'entreprise est localisée à Sokodé
offres_sokode = Offre.objects.filter(entreprise__ville="Sokodé")
```


### 2. Les étudiants qui possèdent la compétence « Django »

```python
from stages.models import Etudiant

# Filtrage en suivant la relation ManyToMany vers les compétences
etudiants_django = Etudiant.objects.filter(competences__libelle="Django")
```

### 3. les candidatures d’un étudiant donné, en partant de l’objet étudiant 

```python
from stages.models import Etudiant

# 1. On récupère l'étudiant
mon_etudiant = Etudiant.objects.get(matricule="IFNTI01")
# 2. On liste ses candidatures
ses_candidatures = mon_etudiant.candidatures.all()
```

### 4. le nombre de candidatures retenues, sans charger les candidatures en mémoire 
```python
from stages.models import Candidature

nb_retenues = Candidature.objects.filter(statut="RETENUE").count()

```


### 5. les stages dont l’offre vient d’une entreprise de Sokodé 
```python 
from stages.models import Stage
stages_sokode = Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
```

### 6. les offres qui demandent au moins une compétence que possède un étudiant donné.

```python
from stages.models import Etudiant, Offre

# 1. On récupère l'étudiant donné
mon_etudiant = Etudiant.objects.get(matricule="IFNTI01")
# 2. On récupère les offres qui demandent ses compétences (avec distinct pour éviter les doublons)
offres_cibles = Offre.objects.filter(competences_attendu__in=mon_etudiant.competences.all()).distinct()

```









