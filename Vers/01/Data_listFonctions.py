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
#	dir : vers/02/ClassRepertories
#################################################






def input_texte():
	# booléen sur la conditionnelle de insert_type(Data)
	# pour un retour au menu 

	retour = "1"
	ListeData = []

	

	while retour == "1" :

		Data = input("\n\nInscrire la donnée : ")
		print(Data)
		data = Data
		print(data)
		ListeData = [data]
		print(ListeData)
		if Data != ListeData[0]:
			ListeData = ListeData.append(Data)

		print("\n\nLa donnée : {} \na été inséré dans la liste : {} \nà incorporer dans la base de donnée.\n\n\n".format(Data,ListeData[0]))
		
		print("\n\nCe choix est-il correct ?\n\t'c' pour terminer, tout autre pour ajouter une donnée à la liste : ",ListeData)
		choix = input("\nreponse : ")


		if choix == "c" :
			retour = "0"
			return ListeData
		
			



def input_list() :
	LData = []
	retour = "1"
	print("\tInscription du titre \n\n")
	titre_list = input_texte()
	# tout les list[0] seront des titres informels
	LData = [titre_list]

	while retour == "1" :
		element_list = input_texte()
		liste = liste.append(element_list)
		print("\n\tVoici ce que contient la liste :", liste)
		choix = input("\n\nFaut-il ajouter un élément ?'c' pour continuer, tout autre pour terminer.")
		if choix == "c":
			retour = "0"
		else : 
			return LData




def input_dico():
	






	pass

























def insert_Type():

	# initialisation des variables
	temp_list = []
	global Data 
	global LData	 # L pour "liste"
	# variable commande à coupler avec 
	# les différents boutons des modules graphique
	quitter = "0"
	continuer = "0"

	while quitter != "x" :

		while continuer != "c":
			# c'est pour plus tard, quand les écrits des différents menus et autres seront mis en fichiers
			# et que le flux entrant pourra afficher la valeur de la variable choix :
			# choix = Interface_User(InsertTypeData)

			choix = input("\n\n\t\t\t\tMenu : \n\nchoisissez votre mode d'inscription de donnée:\n\t1- Un seul mot ou texte\n\t2- Liste\n\t3- Tableaux\n\tx-quitter\n")

		# conditionnelle selon choix user

			if choix == "1" :
				# possibilité de donner une catégorie 
				# afin de trier la donnée
				Data = input_texte()
				temp_list = temp_list.append(Data)
				continuer = "b"

			elif choix == "2" :
				Data = input_list()
				temp_list = temp_list.append(Data)
				continuer = "b"

			elif choix == "x" :
				continuer = "c"

			#phase test
			print(temp_list)

	Data = temp_list
	return Data
	


				# là bas je suis devenu ceux qui, autrefois m'avaient jeté.
				# et rejeté par moi-même, au point de devenir timbré. (inspi du jour)



	# l'ouverture fichier ne marche pas...
##
	# l'inscription data est en passe de se faire
	# reste qu'à espérer qu'à la fermeture du fichier, il se crée !






















def Interface_User(IDInterface):
	# selectionne dans la liste des interfaces, l'affichage correspondant au numero de l'interface 
		# (le numero de l'interface vient de son ordre de passage dans une certaine timeline en relation
		# avec la donnée qui est la cause du choix de l'utilisateur)
		# Menu 
		pass


def TimeLine():
	pass






















# Fonctions ouverture et fermeture des fichiers du Cube

def  openFile(File, openModeFile):
	
	print("test File")
	dirs = "Cube/"
	FileExtend = [dirs,File,".txt"]
	Articulateur = "".join(FileExtend)
	f = open(Articulateur, "a")
	return f

def closeFile(File):
	f.close()



















def EcritureFile(File,openModeFile):
	dirs = "Cube/"
	FileExtend = [dirs,File,".txt"]
	Articulateur = "".join(FileExtend)
	print("Voici le fichier : ",Articulateur)
	#f = open('Articulateur','openModeFile')
	insert_Type()
	if Data :
		f.write(Data)
		f.close()
		return "Ecriture de la donnée : Terminée"
	else :
		return "Echec de l'écriture de la donnée"



def LireFile(File,openModeFile):
	dirs = "Cube/"
	FileExtend = [dirs,File,".txt"]
	Articulateur = "".join(FileExtend)
	f = open(Articulateur, openModeFile)
	print(f.read())
	f.close()

















def insert_(File,openModeFile):
	#to database
	EcritureFile(File,openModeFile)
	#couche sécuritéà mettre autours des données insérées
	return Data




def export_(File,Data):
	#from database
	LireFile(Data)
	return Data




















def BaseDeDonnees(): #(Mode):
#ecriture

# initialisation des variables globales concernant la gestion de données et de fichiers
	global File
	global openModeFile
	global Data 

	File = ""
	openModeFile = ""
	Data = ""
	#if Mode == Ecriture :
		
	
	print("\n\n\n\n\t\tSommaire : \n\n\tChoisir le type d'ouverture du fichier '",File,"' :\n0 - Lecture\n1 - Ecriture\n")
	choix = input("Mode : ")

	choixmenu = "0"
	again = "1"
	loop = "0"
	rep = "0"
	print("\n\n\n")
	while choixmenu != "1" :
		while again == "1":

			if loop == "0":
				File = input("Inscrire le nom d'un fichier : ")
				
			

			if rep == "1":
				print("\n\n\n\t\t   Le nom du fichier, sur lequel \n\t\tfaire les opérations,est à présent : \n\n\t\t\t      ", File)
		
			

			#Paramétrage Lecture
			if choix == "0" :
				#FileFinded(DataCategory)
				openModeFile = "r"
				again = "0"
				export_(Data)
				return Data


			# Paramétrage Ecriture
				#while choixmenu != "0" :	
			if choix == "1" :
				openModeFile = "a"
				again = "0"
				insert_(File,openModeFile)
				#dico = {}
	#
	#						#if dico[0]:
				#	choixmenu ="0"
						

			elif choix != "0" and choix != "1" :
				print("\n\nrecommencez.\n\n")
				#point de départ de la variable again 
				again = "1"
				choixmenu ="0"
				rep = "1"
				#point de départ de la variable rep(eat)
				loop = "1"
			
			
			print("Faire autre chose ?\n\n\t0-Insérer une donnée \n\t1- Terminer")
			choixmenu = input("Réponse :")

			if choixmenu == "0":
				again = "1"

			#print("test1")
			print("le nom du fichier choisi est : ", File)

		if again != "1":
			#print("test2")
			choixmenu = "1"













def select(item):
	#selon couche de gestion :
		# <>ConstructeurStructureImagirarium

		# <>ConstructeurReseauDataImaginarium
	pass


def Grue(Action, Direction):
	pass

def DataCenter(data):
	# traitement des données générées par l'activité de la grue
	# traitement des données à incorporer dans dans les flux 
		# entrant et sortant de l'interfaceUser()
	# traitement des données liées à l'organisation de la DataBank()
	pass


