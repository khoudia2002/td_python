#Afficher au user le menu 
panier=[]
while True: 
    choix =input("""
    Choisissez parmi les 5 options suivantes:
    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter
    Quel est votre choix? : """)

#conditions de validité
    while not choix.isdigit() and choix not in range(1,6):
        print("Entrée invalide")
        choix =input("""
            Choisissez parmi les 5 options suivantes:
            1- Ajouter un article dans le panier
            2- Supprimer un article du panier
            3- Afficher tous les articles
            4- Vider le panier
            5- Quitter
            Quel est votre choix? : """)

    #liste vide 
 

        
    if int(choix)== 1:
        article=input("Entrez le nom de l'article: ")
        price= input("Entrez le prix de l'article : ")
        ajout={"article":article,"price":price}
        panier.append(ajout)
       
    

    elif int(choix)==2:
        pop_article=input("Entrez le nom de l'article à supprimer: ")
        for i in panier:
            if i["article"]==pop_article:
                panier.remove(i)
                

            else:
                ("Aucun aricle de ce nom ")
                

    elif int(choix)==3:
        for i in panier:
            print(i)
            
    elif int(choix)==4:
        panier.clear()
        print("votre panier a été vidé")
       

    else:
        print("fin du programmme")
        exit()