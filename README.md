# Pangloss
Programme de stockage et consultation de vocabulaire en langue étrangère

Associations de mots sont stockées dans un fichier à part.

Gestion des orthographes alternatives (waacklig, waackelig).
Gestion des homographes
Suggestion de synonymes
Interdiction de caractères (nombres, ponctuation…)

COMMENT AJOUTER UN NOUVEAU MOT
>>> listemots=[]
>>> listemots.append(Personne())  PAS DE SIGNE EGAL
>>> listemots[0]
<__main__.Personne object at 0x03615830>

Pour supprimer : del(listemots[0])

Classe mot :
A une orthographe (différent du nom de l’instance)
A une ou plusieurs définitions, qui peuvent être propres ou figurées
A un registre de langage (courant, familier, soutenu)
A un ou plusieurs thèmes
Niveau de maîtrise de l’apprenant (acquis, en cours, non acquis)
Sous-classes et propriétés de mots :
Nom
Genre (masc, fém, neut)
Si masculin, faible ou non
pluriel
adjectif/adverbe
Verbe
Fort ou faible
Si fort : indication des formes
Etre à particule ou non
Si oui, séparable ou inséparable
Transitif ou intransitif
Si transitif, direct ou indirect
Si transitif direct, cas
Admission d’un second complément (donner qc à qqn, convaincre qqn de qc…)
Particule
Cas introduit
Position, post ou préposée
Expression

Déroulement du programme (interface en lignes de texte défilantes) :

Invite de choix :
Enregistrer ou modifier ou supprimer un mot
Rechercher un mot
Afficher le vocabulaire par ordre alphabétique (pertinence ?)
Faire un quiz
Statistiques : voir combien de mots en tout, de chaque sous classe, de chaque registre, niveau de maîtrise global...

Enregistrer ou modifier un mot :
Demander la saisie
Contrôler si mot existe déjà
Si non : demander la saisie de toutes les propriétés
Si oui : proposer une modification des propriétés ou création d’un nouveau mot ou suppression
Rechercher un mot :
Inviter à la saisie
Comparer avec la base
Si existe pas, proposer création
Si existe, proposer consultation, rectification/ajout, suppression
