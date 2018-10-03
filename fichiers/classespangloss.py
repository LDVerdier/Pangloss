import pickle

class Entree : # Définition de notre classe Personne
    """Classe définissant une entrée du dictionnair par :
    - son orthographe
    - sa ou ses définitions
    - son registre de langage
    - le niveau de maîtrise des différents apprenants
    - un ou plusieurs exemples"""
    
    id_number=0
    verif=0
    while verif==0:
        try:
            with open('save_id.txt','rb') as data:
                depickler=pickle.Unpickler(data)
                id_number=depickler.load()
        except:
            with open('save_id.txt','wb') as data:
                pickler=pickle.Pickler(data)
                pickler.dump(0)
            verif=1
        verif=1
    
    def __init__(self,mot,traduction): # constructeur à deux paramètres
        self.ortho = [mot]
        self.defin = [traduction]
        self.registre='courant'
        Entree.id_number += 1
        self.id_number=Entree.id_number
        with open('save_id.txt','wb') as data:
            pickler=pickle.Pickler(data)
            pickler.dump(self.id_number)

    
        
