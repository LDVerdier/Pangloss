Attributs de la classe :

V1 : DONE

. orthographe (variable)
. traduction (variable)
. récupération de la variable orthographe
. édition de la variable orthographe
. idem pour traduction

V2 : DONE
. ID (variable) : générée par l'appel à une fonction Entree.id_number
. consultation de la variable ID

fonction SetID : 
i=valeur en mémoire de le fichier saveID.txt + 1
save i
return i

V3 : DONE
. variables sont en fait des listes : liste d'orthographes, liste de traductions...
. methodes d'ajout d'ortho, de trad...

V4 :
. methode permettant de rechercher une entree par son id_number
. message d'erreur si l'entree n'existe plus

ajout de mot :

saisir le mot -> enregistré dans "mot"
saisir la traduction => enregistré dans "traduction"
création de la nouvelle entrée et sauvegarde

recherche de mot :
créer une liste_ortho contenant toutes les ortho de chaque entrée


liste_ortho = []
i=0
j=0
while i<len(liste):
	
	while j<len(liste[i].ortho):
		liste_ortho.append(liste[i].ortho)
		j=j+1
	i=i+1
	j=0

comparer motrech à liste_ortho
