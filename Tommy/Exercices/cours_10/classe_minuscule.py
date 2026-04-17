class Minuscule:

    def __init__(self, phrase):
        self.phrase = phrase
    

    def petit(self, phrase):
        minuscule = phrase.lower()
        minuscule_final = minuscule.replace(" ", "-")

        if minuscule_final.endswith("?"):
            print("True")
        else:
            print("False")

        return minuscule_final
    