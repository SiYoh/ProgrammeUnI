#!/usr/bin/env python
# -*- coding: utf-8 -*-




# Modules dirs
from os import *
from os.path import *
from glob import *
#
#
#
#
##################################################
#	
#      Développement des classes nécessaires
#
#################################################

# classe permettant le pointage en coordonnées 
# des différentes données existantes au sein du Cube


class Coordonnees:
	x = 0
	y = 0
	z = 0
	def __init__(self,abs,ord,pro):
		self.x = abs
		self.y = ord
		self.z = abs/ord
		# Coordonnée de la base de la donnée 
		self.Coordonnees = ([self.x,self.y,self.z])

		


#################################################


class Data:
	"""docstring for Data"""
	global Composant,FileName, dataVarName, dataValue, dataAttribut, categorie, TypeData
	
	Composant = []

	

	def __init__(self):
		
		
		
		# nom du fichier de la donnée
		self.Composant[0] = ""
		
		
		# nom de la variable appelant la valeur de la donnée
		self.Composant[1] = ""
		
		# valeur de la donnée
		self.Composant[2] = ""
		self.Composant[3] = {}
		self.Composant[4] = []
		
		# Attribut relatif à la donnée
		self.Composant[5] = ""
		self.Composant[6] = []
		self.Composant[7] = {}

		# Categories auxquelles peut appartenir la donnée
		self.Composant[8] = ""
		self.Composant[9] = []
		
		# definit le type de la donnée
		self.Composant[10] = (["",self])

		self.Composant[11] = """"""

	#Méthode
	def Emplacement(self,x,y,z):
		if exist(Data.x,Data.y,Data.z):
			x = x + 1
			y = y + 1
			z = z + 1
		else:
			Coordonnees(Data,x,y,z)


#Composant = Composant.append(FileName,dataVarName,dataValue,dicoValues,listValues,Attribut,dataAttributes,AssociatedAttributs,Categorie,Categories,TypeData,Note)
	






class DataBase : 
	def __init__(self,Data):
		self = {}
		listeCle = ["Fichier","Variable","Valeur","Dico de valeurs","Liste de valeurs","Attibuts","Attribut","Attributs associés","Categorie","Type"]
		self[listeCle[0]] = {}
		self[listeCle[1]] = {}
	#
		self[listeCle[2]] = {}
		self[listeCle[3]] = {}
		self[listeCle[4]] = {}
	#
		self[listeCle[5]] = {}
		self[listeCle[6]] = {}
		self[listeCle[7]] = {}
	#
		self[listeCle[8]] = {}
		self[listeCle[9]] = {}

#
		Data.dataAttributes = [Data.Attribut,Data.Categorie,Data.TypeData]

		def InitializeDB(self,Data):
			for listeCle in DataBase:
				for x in listeCle:
					self[listeCle] = input (listeCle[x]," : ")
			



class XML :
	global Balise
	def __init__(self,numComposant):
		self.Data.Composant ="<"+Balise+">"
		self.Data = ""
		self.Data.Composant = "</"+Balise+">"


class Outils:

# Inverser l'ordre des fonction une fois 
	# qu'elles euent été toutes écrites

	# une caisse à outils de fonctions
	def Outils(choix): 
	 	pass 
	# accéssible à chaque menu ou choix utilisateur
	# fonctions sollicitable :
		# Trouver un fichier au sein de la structure de base de données de l'Imaginarium
	def FindFile(FileName):
		pass
		# Trouver une donnée
	def FindData(dataName):
		pass
		# Incorporer une donnée au sein d'un fichier
	def CreateData(choix):
		#insert_(Data)
		pass
		# Associer un attribut à une donnée

		# Sélectionner une donnée 

		# Copier la donnée sélectionnée

		# Coller la donnée Copiée ou Coupée

		# Couper la donnée sélectionner

		# Isoler la donnée avec les objets et fichiers reliés à elle

		# Incorporer

		# Aperçu de l'ensemble de l'arborence des fichier Timeline sélectionné
		#












class Formulaire:
	def __init__(self):
		pass



##################################################

#classe et methode trouvée, à remodifier
class Server:
    nbServerOnline = 0

    def __init__(self):
        print("creation objet de type Serveur")
        Serveur.nbServerOnline = Serveur.nbServerOnline + 1
        print("il y en a maintenant ", Serveur.nbServerOnline)

    @classmethod
    def get_nbServerOnline(cls):
        return Serveur.nbServerOnline



		

#class Commandes:
#	def Quitter(choix):
#		pass
#	def Continuer(choix):
#		pass
#   def Commande(type):
#	# Commandes générales
#		#Continuer()
#		#Retour()
#		#Quitter()
#		## Process de Connexion()
#		#Deconnexion()
#		pass
#	#



#Code couleur avec Turtle et Tkinter
	# coul = '#{:02x}{:02x}{:02x}'
	# coul.format(255,255,255)
	# coul.format(0,0,0)
	# coul.format(255,0,0)
	# 
	# 	# Code color	
		# coul = '#{:06x}'
		# coul.format(0)