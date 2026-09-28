
# le model entreprise 
- La combinaison des champs nom et ville identifie une entreprise sans ambiguïté dans votre application
- Oui, Ecobank à Sokodé et Ecobank à Lomé doivent être considérées comme deux entreprises distinctes

<!-- 
Gestion des doublons : Associer le nom et la ville permet d'enregistrer ces différentes agences tout en empêchant qu'une même personne saisisse deux fois l'agence de Lomé par erreur. -->

~ EmailField
- Il faut qu'on utilise le type EmailField.parce que ce champ intègre une sécurité qui vérifie le format de la saisie 
 par exemple présence du @ et d'un nom de domaine comme rahma.com, ce qui va nous empecher d'enregistrer un champ invalide et

- pourquoi pas simplement du texte ? Un simple champ texte (CharField) va accepter n'importe quelle frappe accidentelle ce qui rend inutilisable le mail

~ Secteur d'activité

- Il faut opter pour une liste de valeurs imposée (choices en Django)
    - le cout de chaque choie :
        - Du text libre cout aujourd'hui on n'a zero effort et dans 3 mois il y'aura trop de déchet dans la base de donnee a cause des erreurs de frappe cela
        va faire que le filtre des secteur ne sera inutilisable
        - Du champ imposer aujourd'hui ça demande quelques minutes pour définir et coder la liste des secteurs et dans 3 mois  on n'a une base de donnere propre
        et les recherches seront toujours fiable 
- La dernière phrase parle de l'affichage du nom de l'entreprise à l'écran, ce qui correspond à la méthode __str__() en Django.

# Migrer
- a contrainte qui interdit les doublons s'appelle unique
- La colonne concernée est la colonne id

- Il y a maintenant 2 fichiers de migration dans le dossier stages/migrations/ 
        (le fichier initial 0001_initial.py et le nouveau fichier 0002_...py) et pour revenir en arriere on relance en precisant
        uv run manage.py migrate stages 0001

# L’administration
- L'erreur apparaît en validant le formulaire
- Oui, le message est compréhensible si xa exite il va interpreter cela soit disant que le nom ou ville est unique

# La première page 
- je ne sais pas
- Non, cette page d'erreur détaillée ne s'affichera pas lorsque l'application sera en production (en ligne).

# Le dépôt git





