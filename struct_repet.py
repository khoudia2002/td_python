#Exercice : Créer un programme qui affiche les 10 premiers nombres pairs en utilisant
#une boucle For . Ensuite, utiliser une boucle while pour afficher les 10 premiers nombres
#impairs.
print("Exercice 1")
num=1
pairs=0
impairs=0

while pairs<10:
    if num %2==0:
        
        print(num)
        pairs+=1
    num +=1

while impairs<10:
    if num % 2 != 0:
        print(num)
        impairs+=1
    num +=1
        



#Exercice: Créer un programme qui va demander un nombre à l’utilisateur, va s’assurer
#que c’est bien un nombre qui a été inséré et enfin va afficher les nombres entier entre le 1
#et le nombre fourni par l’utilisateur.
#Vous utiliserez les boucles For et While.

print("Exercice 2")
number=input("Entrez un nombre")
while not number.isdigit():
    ("Entrée invalide, mettez un nombre!!!")
    number=input("Entrez un nombre")
for i in range(1,int(number)):
    print(i)
