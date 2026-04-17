class CompteBancaire:
    """
    Une classe simple representant un compte de banque.
    Utilisee pour demontrer l'instanciation, les attributs et les mÃ©thodes.
    """

    def __init__(self, titulaire, solde_initial=0.0):
        # Attributs de l'objet (les donnÃ©es)
        self.titulaire = titulaire
        self.solde = solde_initial
        print(f"--- CrÃ©ation du compte pour {self.titulaire} avec {self.solde}$ ---")

    def depot(self, montant):
        # MÃ©thode pour ajouter de l'argent (une action)
        if montant > 0:
            self.solde += montant
            print(f"[Succes] Depot de {montant}$ sur le compte de {self.titulaire}.")
        else:
            print("[Erreur] Le montant du depot doit etre positif.")

    def retrait(self, montant):
        # Methode pour retirer de l'argent (une action avec vÃ©rification)
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"[SuccÃ¨s] Retrait de {montant}$ sur le compte de {self.titulaire}.")
            else:
                print(f"[Erreur] Fonds insuffisants pour {self.titulaire}. Solde actuel: {self.solde}$")
        else:
            print("[Erreur] Le montant du retrait doit Ãªtre positif.")

    def afficher_solde(self):
        # Methode utilitaire
        print(f"-> Solde actuel de {self.titulaire} : {self.solde}$")
    