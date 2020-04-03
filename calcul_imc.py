m=int(input("masse en kilo : "))
t=int(input("taille en centimètre : "))
IMC=m/(t*t)*10000
print()
print ("Ton IMC est de :", round(IMC,2))
if IMC < 16.5 :
    a = "Anorexie ou dénutrition"
    print("Tu es dans la classe :",a)
if (IMC >= 16.5 and IMC < 18.5) :
    b = "Maigreur"
    print("Tu es dans la classe :", b)
if IMC >= 18.5 and IMC < 25:
    c = "Corpulence normale"
    print("Tu es dans la classe :", c)
if IMC >= 25 and IMC < 30 :
    d = "Surpoids"
    print("Tu es dans la classe :", d)
if IMC >= 30 and IMC < 35 :
    e = "Obésité modérée (Classe 1)"
    print("Tu es dans la classe :", e)
if IMC >= 35 and IMC < 40 :
    f = "Obésité élevée (Classe 2)"
    print("Tu es dans la classe :", f)
if IMC > 40 :
    g = "Obésité morbide ou massive"
    print("Tu es dans la classe :", g)