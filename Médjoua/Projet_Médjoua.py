test1 = "Quelle est l unité de la tension électrique ?"
choix1 = "Ampère"
choix2 = "Volt ✅"
choix3 = "Ohm"

def reponse_(choix1, choix2, choix3) : 
 print("------------------------------")
 print(f"1: {choix1}")
 print(f"2: {choix2}")
 print(f"3: {choix3}")
 decision = int(input("Veuillez choisir votre reponse :"))

 return decision

choix1 = "test1"
choix2 = "test2"
choix3 = "test3"

print("fait votre choix")

reponse_(choix1, choix2, choix3)















































