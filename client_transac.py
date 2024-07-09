transactions = []
customers = []

def menu():
    choice = input("""Menu :
        ○ 1 - Gestion des clients
        ○ 2 - Gestion des transactions
        ○ 3 - Sortir
        Que choisissez-vous ? : """)
    return choice

#GESTION CLIENTS
def afficher_clients():
    for client in customers:
        print(client)

def ajout_client():      
    code = input("Entrez le code du nouveau client : ")
    for client in customers:
        if client["code"] == code:
            print("Ce client existe déjà.")
            return
    nom = input("Entrez votre nom : ")
    tel = input("Entrez votre numéro de téléphone : ")
    adresse = input("Entrez votre adresse : ")
    email = input("Entrez votre adresse mail : ")
    solde = float(input("Entrez le solde : "))
    client = {"code": code, "nom": nom, "tel": tel, "adresse": adresse, "email": email, "solde": solde}
    customers.append(client)
    print("Client ajouté.")

def supp_client():
    code = input("Entrez le code du client à supprimer : ")
    for client in customers:
        if client["code"] == code:
            customers.remove(client)
            print("Le client a été supprimé.")
            return
    print("Le code n'existe pas.")

def mod_client():
    code = input("Entrez le code du client à modifier : ")
    for client in customers:
        if client["code"] == code:
           client['nom'] = input("Entrez le nouveau nom du client : ")
           client['tel'] = input("Entrez le nouveau téléphone du client : ")
           client['adresse'] = input("Entrez la nouvelle adresse du client : ")
           client['email'] = input("Entrez le nouvel email du client : ")
           client['solde'] = float(input("Entrez le nouveau solde : "))
           print("Client modifié avec succès.")
           return
    print("Code invalide.")

def afficher_solde_client():
    code = input("Entrez le code du client : ")
    for client in customers:
        if client['code'] == code:
            print(f"Solde du client : {client['solde']}")
            return
    print("Code invalide.")

#GESTION DES TRANSACTIONS
#Afficher toutes les transactions
def afficher_trans():
    for transaction in transactions:
        print(transaction)

# Afficher les transactions d'un client
def afficher_unetrans():
    ref_paiement = input("Entrez le numéro de référence : ")
    for transaction in transactions:
        if transaction["reference"] == ref_paiement:
            print(transaction)
            return
    print("Cette référence n'existe pas.")

# Ajouter la transaction entre deux clients
def ajout_transaction():
    ref_paiement = input("Entrez le numéro de référence : ")
    code_emetteur = input("Entrez le code émetteur : ")
    code_recepteur = input("Entrez le code récepteur : ")
    date_transaction = input("Entrez la date de la transaction : ")
    montant = float(input("Entrez le montant : "))
    canal = input("Entrez le canal (ORANGE MONEY, WAVE, FREE MONEY, VIREMENT BANCAIRE) : ")
    transaction = {"reference": ref_paiement, "emetteur": code_emetteur, "recepteur": code_recepteur, "date": date_transaction, "montant": montant, "canal": canal}
    transactions.append(transaction)
    print("Transaction ajoutée.")

#Modifier le solde d'un client
def modifier_soldet():
    ref_paiement = input("Entrez le numéro de référence : ")
    for transaction in transactions:
        if transaction["reference"] == ref_paiement:
            nouveau_solde = float(input("Entrez le nouveau solde : "))
            for client in customers:
                if client["code"] == transaction["emetteur"] or client["code"] == transaction["recepteur"]:
                    client["solde"] = nouveau_solde
                    print("Solde modifié avec succès.")
                    return
    

#UTILISATION DES FONCTIONS 
while True:
    choice = menu()

    if int(choice) == 1:
        while True:
            choix_client = input("""
    1 Afficher la liste des clients
    2 Ajouter un client
    3 Supprimer un client
    4 Modifier les informations d'un client
    5 Afficher le solde d'un client
    6 Aller au menu
    Quel est votre choix ? : """)
            if int(choix_client) == 1 :
                afficher_clients()
            elif int(choix_client) == 2 :
                ajout_client()
            elif int(choix_client) == 3 :
                supp_client()
            elif int(choix_client) == 4 :
                mod_client()
            elif int(choix_client) == 5 :
                afficher_solde_client()
            else:
                break
            
    elif int(choice) == 2:
        while True:
            choix_trans = input("""
1 Afficher toutes les transactions
2 Afficher les transactions d'un client
3 Ajouter une transaction
4 Modifier le solde d'un client
5 Aller au menu
Quel est votre choix ? : """)
            if int(choix_trans) == 1 :
                afficher_trans()
            elif int(choix_trans) == 2 :
                afficher_unetrans()
            elif int(choix_trans) == 3 :
                ajout_transaction()
            elif int(choix_trans) == 4 :
                modifier_soldet()
            else:
                break
    else:
        print("Au revoir !")
        break