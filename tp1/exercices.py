#Exercice 1

print(type("bonjour"))
print(type(2))
print(type(2.5))

#Exercice 2



#Exercice 3

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


#Exercice 4

i = 1
n = int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))
while(n <= 0 or n >= 101):
    n=int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))

while (i >= 1 and i <= n):
    print(i)
    i = i + 1
print("STOP ! C'est fini !")