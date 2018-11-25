# coding: utf8

###########
# IMPORTS #
###########

from Log import *
import os, subprocess

#########
# CLASS #
#########

class Presentation:

	#############
	# CONSTANTS #
	#############

	url_banniere = "https://www.pixenli.com/image/tSOeR53I"
	url_seed = "https://www.pixenli.com/image/8pFkx2gL"
	auteur = "MRDOMOO"
	url_signature = "https://www.pixenli.com/image/lJQnyjCh"

	############
	# ATRIBUTS #
	############

	titre = ""
	url_couverture = ""
	description = ""
	url_video = ""
	description_video = ""
	artiste = ""
	album = ""
	format = ""

	nb_fichiers = 0
	taille = 0

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, titre, url_couverture, description, url_video, description_video, artiste, format):

		self.titre = titre
		self.url_couverture = url_couverture
		self.description = description
		self.url_video = url_video
		self.description_video = description_video
		self.artiste = artiste
		self.format = format

	###########
	# METHODS #
	###########
	
	def create(self, album):

		if(os.path.exists(album)):
			self.album = album
			self.nb_fichiers = len(os.listdir(album + "/"))
			self.taille = subprocess.check_output(['du','-sh', album]).split()[0].decode('utf-8')

			texte =  ("[center][u][b][size=200]" + self.titre + "[/size][/b][/u]\n"
			"\n"
			"[img]" + self.url_couverture + "[/img]\n"
			"\n"
			"[b]" + self.description + "\n"
			""
			"[video]" + self.url_video + "[/video]\n"
			"\n"
			"" + self.description_video + "[/b]\n"
			"\n"
			"[img]" + self.url_banniere + "[/img]\n"
			"\n"
			"[b]Artiste(s)[/b] : " + self.artiste + "\n"
			"[b]Album[/b] : " + self.album + "\n"
			"[b]Format[/b] : " + self.format + "\n"
			"[b]Nombre de fichiers[/b] : " + str(self.nb_fichiers) + "\n"
			"[b]Taille totale[/b] : " + self.taille + "o\n"
			"\n"
			"[img]" + self.url_seed + "[/img]\n"
			"\n"
			"[b]UPLOAD PAR [color=crimson]" + self.auteur + "[/color][/b]\n"
			"\n"
			"[img]" + str(self.url_signature) + "[/img][/center]")

			os.popen("echo \"" + texte + "\" > \"" + album + ".txt\"")
			log("Création du fichier \"" + album + ".txt\"")

		else:
			error("Impossible de créer le fichier \"" + album + ".txt\", le dossier \"" + album + "\" n'existe pas")
