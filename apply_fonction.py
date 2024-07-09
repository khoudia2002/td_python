#j'ai utilisé les fonctions définies dans fonctions.py pour les appliquer dans mon programme
from fonctions import *

while True: 
    afficher_menu()

        
    if int(choix)== 1:
        ajout_art_prix()
        

    elif int(choix)==2:
        supp_art()

    elif int(choix)==3:
        afficher_panier()
            
    elif int(choix)==4:
        supprimer_all  ()

    else:
        sortir()