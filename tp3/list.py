liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]

while liste.count(1) > 0:
  liste.remove(1)

print(liste)

liste.sort()

print(liste)


print("Minimum ", min(liste), "Maximum ", max(liste))
print("Somme", sum(liste))
