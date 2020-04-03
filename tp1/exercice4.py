#Exercice 4

i = 1
n = int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))
while(n <= 0 or n >= 101):
    n=int(input("Veuillez saisir une valeur comprise entre 1 et 100 inclus : "))

while (i >= 1 and i <= n):
    print(i)
    i = i + 1
print("STOP ! C'est fini !")