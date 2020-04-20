#Exercice 1

print(type("bonjour"))
print(type(2))
print(type(2.5))

#Exercice 2

for i in range (20) : # pour i allant de 0 à 20
    if (i%2 == 0): # si i est pair
        print("Le chiffre",i,"est pair !") # écrire "Le chiffre i est pair"
        i += 1 # ajouter 1 à i
    else: #sinon
        i += 1 # ajouter 1 à i

while i <= 20: # tant que i est inférieur ou égal à 20
    if (i%2 == 0): # si i est pair
        print("Le chiffre",i,"est pair !")
        i += 1 # ajouter 1 à i
    else: #sinon
        i += 1 # ajouter 1 à i

#Exercice 3

n=int(input("Saisissez une valeur positive : ")) #demander à l'utilisateur de rentrer un entier n
s=0 # initialiser s à 0
for x in range (n): # pour i allant de 0 à n
     if(x%2 != 0): # si x modulo 2 est différent de 0 (impair)
         print(x) # écrire x
         s=s+x # ajouter x à s
     else: # sinon
         print("faux") # écrire "faux"
print("La somme des impairs est", s) #écrire "La somme des impairs est s"


#Exercice 4

i = 1
n = int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : ")) # demander à l'utilisateur d'entrer un entier n compris entre 1 et 100 inclus
while(n <= 0 or n >= 101): # tant que n est inférieur ou égal à 0 OU supérieur ou égal à 100 :
    n=int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : ")) # redemander à l'utilisateur d'entrer un entier n compris entre 1 et 100 inclus

while (i >= 1 and i <= n): # tant que i est supérieur ou égal à 1 ET inférieur ou égal à n :
    print(i)# écrire i
    i = i + 1 # ajouter 1 à i
print("STOP ! C'est fini !")

#Exercice 5

nb1 = int(input("Donnez le premier nombre : "))
print(nb1)
nb2 = int(input("Donnez le deuxième nombre : "))
print(nb2)
op = input("Donnez le symbole de l'opération: ")
print(op)
print()
if(op=='+'):
    print('Le résultat est', a+b)
if(op=='-'):
    print('Le résultat est', a-b)
if(op=='*'):
    print('Le résultat est', a*b)
if (op == '/'):
    if(b==0):
        print("Opération impossible")
    else:
        print('Le résultat est', a/b)
if (op!='+' and op!='-' and op!='*' and op!='/'):
    print("Opération inexistante. Veuillez choisir un opérateur ( + , - , * , /)")




print("BANDE DE VOLEURS !")





