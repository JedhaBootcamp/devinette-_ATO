import random

print("Bienvenue dans le jeu de devinette. Vous avez 5 parties")

class devinette:

    __init__(self, points):
    self.points = points

    def jouer(self, max_num):
        chiffre = random.randint(1, max_num)
        dev = input("Veuillez choisir un chiffre entre 1 et {} ".format(max_num))
        if chiffre == dev:
            self.points += 1
            print(bien joué!)
        else:
            print(réessayez)
