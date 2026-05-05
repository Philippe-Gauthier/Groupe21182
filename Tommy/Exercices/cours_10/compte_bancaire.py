class CompteBancaire:
    """
    
    """
    # __init__ pour creer un objet. Creer les attributs initials.
    def __init__(self, titulaire, solde_initial=0.0):
        self.titulaire = titulaire
        self.solde = solde_initial
        print(f"--- Creation du compte pour {self.titulaire} avec {self.solde}$ ---")

    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"[succes] depot de {montant}$ sur le compte de {self.titulaire}.")
        else:
            print("[erreur] Le montant du depot doit etre positif")

    def retrait(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"[succes] Retrait de {montant}$ sur le compte de {self.titulaire}.")

        else:
            print(f"[erreur] fonds insuffisants pour {self.titulaire}. Solde actuel: {self.solde}.")

    def afficher_solde(self):
        # Methode utilitaire
        print(f"-> Solde actuel de {self.titulaire} : {self.solde}$")