def kmh_vers_mph(kmh):
    mph = kmh / 1.609
    return mph

vitesse = int(input("Quelle vitesse "))
print(int(kmh_vers_mph(vitesse)))