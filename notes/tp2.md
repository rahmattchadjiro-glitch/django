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

- On le garantit avec une contrainte d'unicité combinée sur l'étudiant et l'offre.

- La promotion doit être un nombre entier comme 2026,la statistique que ifniti vaudra des nombre car s'il prend un chaine de caractere on n'aura des erreur ds la base de donner

- Le statut doit être une liste fermée de choix (choices en Django), par exemple : Déposée, Retenue ou Refusée
   - avec du text libre : on n'aura des erreurs lors du saisi l'utilisateur peut ecrit retenue et la base de donner va cracher une erreur
   - avec une liste fermer : l'application bloque la saisie avant meme que l'erreur soit arriver a la base donc l'utilisateur ne que peut choisir dans la liste


- la suppression va refuser car on ne pert jamais  l'historique d'un stage protected ,on ne peut pas supprimer

# 3. Lire le SQL 
- La migration crée 10 tables parmi elle ya   etudiant_competences
 stages,offre,competences car il on une relation plusieurs a plusieurs

- Non, il n'y a aucune table pour Personne , c'est cohérent avec le choix de la partie 2

- la règle apparaît sous la forme d'une contrainte d'unicité UNIQUE elle appareil sous la forme 
UNIQUE ("etudiant_id", "offre_id")

- la trace est la suivante CREATE TABLE "stages_stage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "sujet" varchar(250) NOT NULL, "candidature_id" bigint NOT NULL UNIQUE REFERENCES "stages_candidature" ("id") DEFERRABLE INITIALLY DEFERRED, "enseignant_id" bigint NOT NULL REFERENCES "stages_enseignantreferent" ("id") DEFERRABLE INITIALLY DEFERRED, "tuteur_id" bigint NOT NULL REFERENCES "stages_tuteurentreprise" ("id") DEFERRABLE INITIALLY DEFERRED);
CASCADE quand t'on supprime le grand les enfant aussi part, PROTECT on ne peut mm pas supprimer,et ces regle sont 
appliquer a la base de donner

# 4. L’administration 

- a) Django bloque la suppression et affiche un message d'erreur rouge (une erreur de type ProtectedError)
- Oui, c'est exactement ce que la responsable voulait : cela empêche une fausse manipulation d'effacer accidentellement l'historique et les traces des stages passés au sein de l'école 

- b) L'admin aurait affiché une page d'alerte listant tous les éléments liés (offres, candidatures, stages) et aurait tout supprimé définitivement, détruisant ainsi tout l'historique 

# 5. Peupler, puis interroger 








