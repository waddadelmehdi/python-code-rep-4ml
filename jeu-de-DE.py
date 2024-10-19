import random


def lancer_de():

    return random.randint(1, 6)


def jeu_de_de():
    print("Bienvenue dans le jeu de dés !")
    print("Appuyez sur 'Entrée' pour lancer le dé ou 'q' pour quitter.")

    while True:

        choix = input("Votre choix : ")

        if choix.lower() == 'q':
            print("Vous avez quitté le jeu. À bientôt !")
            break
        elif choix == '':

            tirage = lancer_de()
            print(f"Tirage : {tirage}")
        else:
            print("Choix invalide. Appuyez sur 'Entrée' pour lancer le dé ou 'q' pour quitter.")



jeu_de_de()
