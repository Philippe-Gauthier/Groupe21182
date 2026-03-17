paquet_1 = ["As de carreau", "2 de carreau", "3 de carreau", "4 de carreau", "5 de carreau", "6 de carreau", "7 de carreau", "8 de carreau", "9 de carreau", "10 de carreau", "Valet de carreau", "Dame de carreau",]
paquet_2 = ["As de coeur", "2 de coeur", "3 de coeur", "4 de coeur", "5 de coeur", "6 de coeur", "7 de coeur", "8 de coeur", "9 de coeur", "10 de coeur", "Valet de coeur", "Dame de coeur",]

paquet_valide = set(paquet_1 + paquet_2)

if len(paquet_valide) != len(paquet_1 + paquet_2):
    print("Triche detectee, carte en double")
else:
    print("all good")