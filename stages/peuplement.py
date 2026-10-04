# peuplement.py
from stages.models import Entreprise, Competence, Etudiant, TuteurEntreprise, EnseignantReferent, Offre, Candidature, Stage
from datetime import date

print("Début du peuplement...")

# 1. Cinq compétences
c_django, _ = Competence.objects.get_or_create(libelle="Django")
c_sql, _ = Competence.objects.get_or_create(libelle="SQL")
c_js, _ = Competence.objects.get_or_create(libelle="JavaScript")
c_docker, _ = Competence.objects.get_or_create(libelle="Docker")
c_git, _ = Competence.objects.get_or_create(libelle="Git")

# 2. Trois entreprises (dont deux à Sokodé demandées par l'énoncé)
ent1, _ = Entreprise.objects.get_or_create(nom="SokoTech", ville="Sokodé", secteur="Informatique")
ent2, _ = Entreprise.objects.get_or_create(nom="AgroPlus", ville="Sokodé", secteur="Agriculture")
ent3, _ = Entreprise.objects.get_or_create(nom="Lomé Digital", ville="Lomé", secteur="Numérique")

# 3. Deux tuteurs rattachés à leurs entreprises respectives
tut1, _ = TuteurEntreprise.objects.get_or_create(
    nom="Koffi", prenom="Jean", sexe="M", date_naissance=date(1985, 4, 12), 
    email="j.koffi@sokotech.tg", entreprise=ent1
)
tut2, _ = TuteurEntreprise.objects.get_or_create(
    nom="Lawson", prenom="Awa", sexe="F", date_naissance=date(1990, 8, 24), 
    email="a.lawson@lomedigital.tg", entreprise=ent3
)

# 4. Deux enseignants référents
ens1, _ = EnseignantReferent.objects.get_or_create(
    nom="Amadou", prenom="Ali", sexe="M", date_naissance=date(1978, 1, 15), email="a.ali@ifnti.tg"
)
ens2, _ = EnseignantReferent.objects.get_or_create(
    nom="Tchagnao", prenom="Fati", sexe="F", date_naissance=date(1983, 11, 2), email="f.tchagnao@ifnti.tg"
)

# 5. Cinq étudiants avec leurs compétences attribuées
et1, _ = Etudiant.objects.get_or_create(matricule="IFNTI01", nom="Adjo", prenom="Marie", sexe="F", date_naissance=date(2004, 3, 5), email="marie@ifnti.tg", promotion=2026)
et1.competences.add(c_django, c_git, c_sql)

et2, _ = Etudiant.objects.get_or_create(matricule="IFNTI02", nom="Ouro", prenom="Salif", sexe="M", date_naissance=date(2005, 6, 20), email="salif@ifnti.tg", promotion=2026)
et2.competences.add(c_sql, c_git)

et3, _ = Etudiant.objects.get_or_create(matricule="IFNTI03", nom="Kparo", prenom="Yao", sexe="M", date_naissance=date(2004, 9, 14), email="yao@ifnti.tg", promotion=2026)
et3.competences.add(c_django, c_js)

et4, _ = Etudiant.objects.get_or_create(matricule="IFNTI04", nom="Essi", prenom="Abla", sexe="F", date_naissance=date(2003, 12, 25), email="abla@ifnti.tg", promotion=2025)
et4.competences.add(c_js, c_docker, c_git)

et5, _ = Etudiant.objects.get_or_create(matricule="IFNTI05", nom="Mani", prenom="Kossi", sexe="M", date_naissance=date(2005, 1, 30), email="kossi@ifnti.tg", promotion=2026)
et5.competences.add(c_django, c_docker)

# 6. Trois offres avec compétences demandées
off1, _ = Offre.objects.get_or_create(titre="Dev Django", description="Création d'un portail web", date_debut=date(2027, 2, 1), date_fin=date(2027, 7, 31), nb_places=1, entreprise=ent1)
# Note : on n'ajoute pas la compétence au get_or_create car c'est un ManyToManyField
off1.competences_attendues.add(c_django, c_sql)

off2, _ = Offre.objects.get_or_create(titre="Intégrateur JS", description="Refonte d'interface", date_debut=date(2027, 3, 1), date_fin=date(2027, 8, 31), nb_places=1, entreprise=ent3)
off2.competences_attendues.add(c_js)

off3, _ = Offre.objects.get_or_create(titre="Admin SQL", description="Optimisation de BDD", date_debut=date(2027, 2, 15), date_fin=date(2027, 6, 15), nb_places=1, entreprise=ent2)
off3.competences_attendues.add(c_sql)

# 7. Six candidatures de statuts variés
cand1, _ = Candidature.objects.get_or_create(etudiant=et1, offre=off1, statut="RETENUE")
cand2, _ = Candidature.objects.get_or_create(etudiant=et2, offre=off1, statut="REFUSEE")
cand3, _ = Candidature.objects.get_or_create(etudiant=et3, offre=off2, statut="DEPOSEE")
cand4, _ = Candidature.objects.get_or_create(etudiant=et4, offre=off2, statut="RETENUE")
cand5, _ = Candidature.objects.get_or_create(etudiant=et5, offre=off3, statut="DEPOSEE")
cand6, _ = Candidature.objects.get_or_create(etudiant=et1, offre=off3, statut="REFUSEE")

# 8. Deux stages issus de candidatures retenues (avec le nom de ton champ "enseignant" de l'admin)
stg1, _ = Stage.objects.get_or_create(sujet="Développement de SokoGestion", candidature=cand1, tuteur=tut1, enseignant=ens1)
stg2, _ = Stage.objects.get_or_create(sujet="Déploiement Infrastructure", candidature=cand4, tuteur=tut2, enseignant=ens2)

print("Peuplement terminé avec succès ! 🎉")
