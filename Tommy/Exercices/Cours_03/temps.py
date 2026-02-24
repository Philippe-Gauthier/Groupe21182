def calculer_heure_minute(minutes):
    heure = minutes // 60
    restant_minute = minutes % 60
    temps = f"{heure}heure {restant_minute}minutes"
    return temps

question = int(input("Nombre de minutes "))
print(calculer_heure_minute(question))