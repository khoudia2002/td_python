#Exercice : Écrire un programme qui demande à l'utilisateur d'entrer une note. Selon la
#note, afficher un message indiquant la mention obtenue :
#a. "Excellent" pour les notes de 18 et plus
#b. "Très bien" pour les notes entre 16 et 18
#c. "Bien" pour les notes entre 14 et 16
#d. "Satisfaisant" pour les notes entre 12 et 14
#e. “Passable” pour les notes entre 10 et 12
#f. "Échec" pour les notes inférieures à 10

#Écrire un programme qui demande à l'utilisateur d'entrer une note

note= (input("Entrez une note: "))
#conditions de validité de la note
while not note.isdigit():
    print("Entrez invalide, mettez des chiffres!!!")
    note= input("Entrez une note: ")
#a. "Excellent" pour les notes de 18 et plus
if int(note) >= 18:
    print("Excellent")
#b. "Très bien" pour les notes entre 16 et 18
elif int(note) >= 16 and int(note )<18:
    print("Très bien ")
#c. "Bien" pour les notes entre 14 et 16
elif int(note) >= 14 and int(note )<16:
    print("Bien ")
#d. "Satisfaisant" pour les notes entre 12 et 14
elif int(note) >= 12 and int(note )<14:
    print("Satisfaisant ")
#e. “Passable” pour les notes entre 10 et 12
elif int(note) >=10 and int(note )<12:
    print("Satisfaisant ")
#f. "Échec" pour les notes inférieures à 10
else:
    print("echec")