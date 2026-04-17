from compte_bancaire_prof import CompteBancaire

compte_01 = CompteBancaire("Marie")
compte_02 = CompteBancaire("John")

print(CompteBancaire.afficher_solde(compte_01))
CompteBancaire.depot(compte_01, 750)
print(CompteBancaire.afficher_solde(compte_01))