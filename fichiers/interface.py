from classespangloss import *
#import picle (non nécessaire car importé dans classespangloss)

###############################################

"""récupère le contenu de la sauvegarde """

liste=[]
try:
    with open('save.txt','rb') as data:
        depickler=pickle.Unpickler(data)
        liste=depickler.load()

except:
    pass

###############################################

def debut():

    """message de bienvenue"""
    print("Bienvenue dans Pangloss !")
    
###############################################


def invite(choix=0):

    """Choisir en tapant le nombre correspondant
        1 : ajout
        2 : recherche
        3 : quitter """
   

    while choix==0:
        print("Que voulez-vous faire ?")
        print("1 : Ajout")
        print("2 : Recherche")
        print("3 : Quitter")
        choix=input()
        try:
            choix=int(choix)
        except ValueError:
            print("Saisie incorrecte.")
            choix=0
            continue # redemande entrée jusqu'à saisie valide
        if choix==1:
            ajout()
            
        elif choix==2:
            recherche()
            
        elif choix==3:
            sortie()
            break            
        else :
            print("option non disponible... bye bye")
            debut()
            invite()
            


###############################################

        
def verifsaisie(saisie):
    caracauto="abcdefghijklmnopqrstuvwxyz01"
    for lettre in saisie:
        if lettre.lower() in caracauto:
            continue
        else:
            print("saisie incorrecte !")
            return 0
    return 1

###############################################


def ajout():
    
    """Demande la saisie d'un mot à ajouter à la base."""
    
    i=0
    while i==0:
        
        newmot=input("Saisir le nouveau mot : ")
        i=verifsaisie(newmot)  # verifie que la saisie est conforme
    
    i=0
    while i==0:

        traduction=input("Saisir la traduction : ")
        i=verifsaisie(traduction)

    print("Vous avez saisi : ",newmot,"avec pour traduction : ",traduction,".")
    
    #print("Vous avez saisi : ", newmot)
    verif=input("Voulez-vous le sauvegarder ? o/n ")
    while verif is not 'o' and verif is not 'n':
            verif=input("Répondez o pour Oui et n pour Non. ")
    if verif is "o":
        save(newmot, traduction)
        print("Mot enregistré.") 
    elif verif is "n":
        print("Mot non enregistré.")
    
    invite()

###############################################

def recherche():

    """Demande la saisie d'un mot qui sera comparé avec la base."""
    
    i=0
    while i==0:
        
        motrech=input("Saisir le mot à rechercher : ")
        i=verifsaisie(motrech)  # verifie que la saisie est conforme

    # création d'une liste de toutes les orthographes    
    j=0
    k=0
    liste_ortho=[]
    while j<len(liste):
        while k<len(liste[j].ortho):
            liste_ortho.append(liste[j].ortho[k])
            k=k+1
        j=j+1
        k=0
    # comparaison du mot recherché à chacun des éléments de la liste d'orthographes
    liste_result=[]
    m=0
    while m < len(liste_ortho):
        if motrech == liste_ortho[m]:
            liste_result.append(m)
        m=m+1

    if len(liste_result) == 0:
        print("pas trouvé")
    else:
        print("trouvé", len(liste_result),"fois")
        
    """for mot in liste_ortho:
        if motrech in liste_ortho:
            print('trouvé')"""
        
        
    """if motrech in liste:
        print("Le mot ", motrech," a été trouvé en position",liste.index(motrech),".")
        reponse=input("Voulez-vous le supprimer ? o / n : ")
        while reponse is not 'o' and reponse is not 'n':
            reponse=input("Répondez o pour Oui et n pour Non. ")
        if reponse is "o":
            suppression(motrech)            
        elif reponse is "n":
            print("Ah, on ne supprime pas.")
    else:
        print("Le mot ", motrech," n'existe pas dans la base.")
        reponse=input("Voulez-vous l'ajouter à la base ? o/n ")
        while reponse is not 'o' and reponse is not 'n':
            reponse=input("Répondez o pour Oui et n pour Non. ")
        if reponse is "o":
            save(motrech)
        elif reponse is "n":
            print("Ah, on ne l'ajoute pas.")"""
    invite()

###############################################

def sortie():

    """Quitte le programme."""
    
    print("Bye bye !")
    

###############################################

def suppression(motrech):

    """Efface le mot de la base et enregistre."""
    
    del liste[liste.index(motrech)]
    with open('save.txt','wb') as data:  # sauvegarde (ecrase)  la liste
        pickler=pickle.Pickler(data)
        pickler.dump(liste)
    print(motrech, "a été supprimé.")


def save(newmot, traduction):
    
    """Ajoute le mot dans la base et enregistre."""
    liste.append(Entree(newmot,traduction))
    with open('save.txt','wb') as data:   
        pickler=pickle.Pickler(data)
        pickler.dump(liste)
