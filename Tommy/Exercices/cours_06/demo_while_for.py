import time

essai = ""

while essai != "1234":
    essai = input("entrez le mot de passe: ")

for i in range(3,0,-1):
    time.sleep(1)
    print(i)