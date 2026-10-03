# 1. Un modèle par fichier 
- après avoire lancer uv run manage.py makemigrations je constate que rien na changer (No changes detected)

- Django n'identifie pas un modèle par le chemin absolu du fichier .py dans lequel il est écrit           Il s'appuie sur deux éléments clés lors du chargement de l'application

- Une migration est un historique des changements de la structure de la base de données .

# 2. La parole de la responsable des stages



# 2.2 Ce qu’elle ne dit pas
- Non, Personne ne doit pas avoir sa propre table.
- La responsable ne demande jamais « toutes les personnes » sans distinction. Elle gère uniquement des étudiants,  des enseignants ou des tuteurs On utilise donc une classe abstraite (abstract = True).

- Il appartient à l'entreprise.
Le tuteur est d'abord un employé de la structure partenaire avant d'encadrer un stage

- Non  Une candidature ne peut donner lieu qu'à un seul stage au maximum, et un stage ne peut pas exister sans une candidature , C'est le champ OneToOneField(Candidature) placé dans le modèle Stage qui l'interdit et cette contrainte agit aux deux niveaux .En base de données : Elle crée une clé étrangère unique , ce qui empêche d'associer une deuxième fois la même candidature à un autre stage et
 Au niveau Python : Elle valide l'existence obligatoire de la candidature lors de la création et l'empêche d'être vide 
