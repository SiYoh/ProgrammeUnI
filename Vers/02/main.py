#!/usr/bin/env python
# -*- coding: utf-8 -*-




# Modules dirs
from os import *
from os.path import *
from glob import *


from ClassRepertories import DataBase,Data,Outils


# Mise en place de la Base de données
Cube = DataBase(Data())

inputUser = "test a faire :"

# initialisation des instances de classe : Data

#BaseDeDonnees["test"] = color('#00ff00')



# Initialisation des clés de la BDD
	# 
Cube
print(Cube)

Cube[test] = input(inputUser)

print(Cube[test])