class Robot:
    """
    Une classe reprÃ©sentant un robot virtuel avec une batterie.
    Les Ã©tudiants doivent instancier cette classe et utiliser ses mÃ©thodes.
    """

    def __init__(self, nom):
        # Le robot commence toujours avec 100% de batterie Ã  sa crÃ©ation
        self.nom = nom
        self.batterie = 100
        print(f"SystÃ¨me initialisÃ©. Robot {self.nom} en ligne. Batterie Ã  100%.")

    def parler(self, message):
        """Affiche un message Ã  l'Ã©cran et consomme 1% de batterie."""
        if self.batterie >= 1:
            print(f"[{self.nom}] dit :{message}")
            self.batterie -= 1
        else:
            print(f"[{self.nom}] : *Silence* (Batterie vide)")

    def se_deplacer(self, distance):
        """
        Simule un dÃ©placement. 
        Chaque mÃ¨tre parcouru coÃ»te 1% de batterie.
        """
        if self.batterie >= distance:
            print(f"[{self.nom}] se dÃ©place de {distance} mÃ¨tres.")
            self.batterie -= distance
        elif self.batterie > 0:
            # S'il reste un peu de batterie, mais pas assez pour tout le trajet
            print(f"[{self.nom}] n'a pas assez d'Ã©nergie. Il avance de {self.batterie} mÃ¨tres puis s'arrÃªte.")
            self.batterie = 0
        else:
            print(f"[{self.nom}] ne peut pas bouger. Batterie vide.")