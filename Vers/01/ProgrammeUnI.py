#!/usr/bin/env python3
import os
import pathlib

# Modules Graphique
# utiliser le module 'toga' ?
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# Pour commande DOS :
# "C:\Windows\System32\cmd.exe"


# on va partir de rien.
def pre_neant():
    fichier = open("data.txt", "a")
    fichier.write("Bonjour monde")
    fichier.close()

    # bonne méthode pour accéder à un fichier !
    with open("data.txt", "r") as fichier:
        print(fichier.read())

    rep = 1
#    f=open("neant.txt",'a')
#    print(f)
#    global Liste
#    Liste = ["initialisation","construction"]
#    Liste = ":".join(Liste)
#    f.write(Liste)
#    f.close()
#    return Liste
#
    return rep


def Neant():
    repa = pre_neant()
    print(repa)
    if programme == 0:
        phase = Liste[0]
        etape =  Liste[1]
        print("Nous voici dans la phase ", phase, " \nde la phase ", etape, " de  du logiciel.")

    elif programme == 1 :
            print("Voici les outils à disposition pour la phase d'initialisation :")


# Menu_ Initialisation

def Outils():
    programme = 1
    Action = []
    A_Faire = input("")
    Grue = Grue(Action[A_Faire])

    Menu_(programme)
    Liste_Outils = [Grue]


def Initialisation():
    programme = 0
    Menu_(programme)
    Outils()
    pass


# attention à ce genre d'appel, qui sera effectué à l'import du module !
# utiliser if __name__ == '__main__':
# si les appels doivent être faits lorsque le script est appelé à travers le terminal
programme = 0
Neant()
