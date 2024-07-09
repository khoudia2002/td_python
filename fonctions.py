panier=[]
choix=input("""
    Choisissez parmi les 5 options suivantes:
    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter
    Quel est votre choix? :""")

def afficher_menu():
    choix=input("""
    Choisissez parmi les 5 options suivantes:
    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter
    Quel est votre choix? :""")
    
    

def ajout_art_prix():
    
    article=input("Entrez le nom de l'article: ")
    price= input("Entrez le prix de l'article : ")
    ajout={"article":article,"price":price}
    panier.append(ajout)

def supp_art():
    pop_article=input("Entrez le nom de l'article à supprimer: ")
    for i in panier:
        if i["article"]==pop_article:
            panier.remove(i)
                
        else:
            ("Aucun aricle de ce nom ")

def afficher_panier():
    for i in panier:
        print(i)

def supprimer_all():
    panier.clear()
    print("votre panier a été vidé")

def sortir():
    print("fin du programmme")
    exit()
