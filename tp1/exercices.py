#Exercice 1

print(type("bonjour"))
print(type(2))
print(type(2.5))

#Exercice 2

for i in range (20) :
    if (i%2 == 0):
        print("Le chiffre",i,"est pair !")
        i += 1
    else:
        i += 1

while i <= 20:
    if (i%2 == 0):
        print("Le chiffre",i,"est pair !")
        i += 1
    else:
        i += 1

#Exercice 3

n=int(input("Saisissez une valeur positive : "))
s=0
for x in range (n):
     if(x%2 != 0):
         print(x)
         s=s+x
     else:
         print("faux")
print("La somme des impairs est", s)


#Exercice 4

i = 1
n = int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))
while(n <= 0 or n >= 101):
    n=int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))

while (i >= 1 and i <= n):
    print(i)
    i = i + 1
print("STOP ! C'est fini !")

#Exercice 5

a = int(input("Donnez le premier nombre : "))
print(a)
b = int(input("Donnez le premier nombre : "))
print(b)
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




print(BANDE DE VOLEURS !)





