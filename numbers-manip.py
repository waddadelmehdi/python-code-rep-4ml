import random


nombre_a_deviner = random.randint(1, 100)


tentatives = 0


while True:

    nombre_utilisateur = int(input("Entrer un nombre : "))
    tentatives += 1


    if nombre_utilisateur > nombre_a_deviner:
        print("Trop grand")
    elif nombre_utilisateur < nombre_a_deviner:
        print("Trop petit")
    else:
        print(f"Bravo, vous l'avez trouvé après {tentatives} essais !")
        break
