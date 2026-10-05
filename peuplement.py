# peuplement.py
from stages.models import Entreprise, Competence, Etudiant, TuteurEntreprise, EnseignantReferent, Offre, Candidature, Stage
from datetime import date


# 1. Cinq compétences
competence_django = Competence.objects.create(libelle="Django")
competence_sql = Competence.objects.create(libelle="SQL")
competence_js = Competence.objects.create(libelle="JavaScript")
competence_docker = Competence.objects.create(libelle="Docker")
competence_git = Competence.objects.create(libelle="Git")

# 2. Trois entreprises
entreprise_sokotech = Entreprise.objects.create(nom="SokoTech", ville="Sokodé", secteur="Informatique")
entreprise_agroplus = Entreprise.objects.create(nom="AgroPlus", ville="Sokodé", secteur="Agriculture")
entreprise_lomedigital = Entreprise.objects.create(nom="Lomé Digital", ville="Lomé", secteur="Numérique")

# 3. Deux tuteurs rattachés à leurs entreprises respectives
tuteur_koffi = TuteurEntreprise.objects.create(
    nom="Koffi", prenom="Jean", sexe="M", date_naissance=date(1985, 4, 12), 
    email="j.koffi@sokotech.tg", entreprise=entreprise_sokotech
)
tuteur_lawson = TuteurEntreprise.objects.create(
    nom="Lawson", prenom="Awa", sexe="F", date_naissance=date(1990, 8, 24), 
    email="a.lawson@lomedigital.tg", entreprise=entreprise_lomedigital
)

# 4. Deux enseignants référents
enseignant_amadou = EnseignantReferent.objects.create(
    nom="Amadou", prenom="Ali", sexe="M", date_naissance=date(1978, 1, 15), email="a.ali@ifnti.tg"
)
enseignant_tchagnao = EnseignantReferent.objects.create(
    nom="Tchagnao", prenom="Fati", sexe="F", date_naissance=date(1983, 11, 2), email="f.tchagnao@ifnti.tg"
)

# 5. Cinq étudiants avec leurs compétences attribuées
etudiant_marie = Etudiant.objects.create(matricule="IFNTI01", nom="Adjo", prenom="Marie", sexe="F", date_naissance=date(2004, 3, 5), email="marie@ifnti.tg", promotion=2026)
etudiant_marie.competences.add(competence_django, competence_git, competence_sql)

etudiant_salif = Etudiant.objects.create(matricule="IFNTI02", nom="Ouro", prenom="Salif", sexe="M", date_naissance=date(2005, 6, 20), email="salif@ifnti.tg", promotion=2026)
etudiant_salif.competences.add(competence_sql, competence_git)

etudiant_yao = Etudiant.objects.create(matricule="IFNTI03", nom="Kparo", prenom="Yao", sexe="M", date_naissance=date(2004, 9, 14), email="yao@ifnti.tg", promotion=2026)
etudiant_yao.competences.add(competence_django, competence_js)

etudiant_abla = Etudiant.objects.create(matricule="IFNTI04", nom="Essi", prenom="Abla", sexe="F", date_naissance=date(2003, 12, 25), email="abla@ifnti.tg", promotion=2025)
etudiant_abla.competences.add(competence_js, competence_docker, competence_git)

etudiant_kossi = Etudiant.objects.create(matricule="IFNTI05", nom="Mani", prenom="Kossi", sexe="M", date_naissance=date(2005, 1, 30), email="kossi@ifnti.tg", promotion=2026)
etudiant_kossi.competences.add(competence_django, competence_docker)

# 6. Trois offres avec compétences demandées (Correction de l'attribut)
offre_django = Offre.objects.create(titre="Dev Django", description="Création d'un portail web", date_debut=date(2027, 2, 1), date_fin=date(2027, 7, 31), nb_places=1, entreprise=entreprise_sokotech)
offre_django.competences_attendu.add(competence_django, competence_sql)

offre_js = Offre.objects.create(titre="Intégrateur JS", description="Refonte d'interface", date_debut=date(2027, 3, 1), date_fin=date(2027, 8, 31), nb_places=1, entreprise=entreprise_lomedigital)
offre_js.competences_attendu.add(competence_js)

offre_sql = Offre.objects.create(titre="Admin SQL", description="Optimisation de BDD", date_debut=date(2027, 2, 15), date_fin=date(2027, 6, 15), nb_places=1, entreprise=entreprise_agroplus)
offre_sql.competences_attendu.add(competence_sql)

# 7. Six candidatures de statuts variés
candidature_un = Candidature.objects.create(etudiant=etudiant_marie, offre=offre_django, statut="RETENUE")
candidature_deux = Candidature.objects.create(etudiant=etudiant_salif, offre=offre_django, statut="REFUSEE")
candidature_trois = Candidature.objects.create(etudiant=etudiant_yao, offre=offre_js, statut="DEPOSEE")
candidature_quatre = Candidature.objects.create(etudiant=etudiant_abla, offre=offre_js, statut="RETENUE")
candidature_cinq = Candidature.objects.create(etudiant=etudiant_kossi, offre=offre_sql, statut="DEPOSEE")
candidature_six = Candidature.objects.create(etudiant=etudiant_marie, offre=offre_sql, statut="REFUSEE")

# 8. Deux stages issus de candidatures retenues
stage_un = Stage.objects.create(sujet="Développement de SokoGestion", candidature=candidature_un, tuteur=tuteur_koffi, enseignant=enseignant_amadou)
stage_deux = Stage.objects.create(sujet="Déploiement Infrastructure", candidature=candidature_quatre, tuteur=tuteur_lawson, enseignant=enseignant_tchagnao)

