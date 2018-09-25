from classespangloss import *
import pickle

"""récupère le contenu de la sauvegarde """

liste=['0','1']

with open('save.txt','rb') as data:
        depickler=pickle.Unpickler(data)
        liste=depickler.load()


def debut():

    """message de bienvenue"""
    print("Bienvenue dans Pangloss !")
    

def invite():

    """Choisir en tapant le nombre correspondant
        1 : ajout
        2 : consultation
        3 : quitter """

    choix=0

    while choix ==0:
        print("Que voulez-vous faire ?")
        print("1 : Ajout")
        print("2 : Consultation")
        print("3 : Quitter")
        choix=input()
        try:
            choix=int(choix)
        except ValueError:
            print("Saisie incorrecte.")
            choix=0
            continue # redemande entrée jusqu'à saisie valide
        if choix==1:
            i=0
            while i==0:
                
                newmot=input("Saisir le nouveau mot : ")
                i=verifsaisie(newmot)  # verifie que la saisie est conforme
            
            liste.append('0')           # ajoute un objet à la liste
            liste[len(liste)-1]=newmot   # assigne la saisie à cet objet (dernier créé)
            with open('save.txt','wb') as data:  # sauvegarde (ecrase)  la liste
                pickler=pickle.Pickler(data)
                pickler.dump(liste)
            print(newmot, " a été enregistré.")
                
            invite()
        elif choix==2:
            print("en cours")
            choix=0
            invite()
        elif choix==3:
            print("Bye bye !")
            choix=0
            break
        else :
            print("option non disponible... bye bye")
            choix=0
            debut()
            invite()
            
"""def saisiealpha(saisie):
    """"""Verifie que la saisie ne contient
    que des caractères alphabétiques""""""
    i=1
    caracauto="abcdefghijklmnopqrstuvwxyz"
    for lettre in saisie:
        if lettre.lower() in caracauto:
            continue
        else:
            print("saisie incorrecte !")
            i=0
            break
    if i:
        return saisie
    else:
        invite()"""
        
def verifsaisie(saisie):
    caracauto="abcdefghijklmnopqrstuvwxyz"
    for lettre in saisie:
        if lettre.lower() in caracauto:
            continue
        else:
            print("saisie incorrecte !")
            return 0
    return 1

        
