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

	bannerUrl = "https://www.pixenli.com/image/tSOeR53I"
	seedUrl = "https://www.pixenli.com/image/8pFkx2gL"
	author = "MRDOMOO"
	signatureUrl = "https://www.pixenli.com/image/lJQnyjCh"

	############
	# ATRIBUTS #
	############

	title = None
	coverUrl = None
	description = None
	videoUrl = None
	videoDescription = None
	artist = None
	album = None
	format = None
	bitrate = "192 kbps"

	fileNumber = None
	weigth = None

	files = ""
	
	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, title, coverUrl, description, videoUrl, videoDescription, artist, format):

		self.title = title
		self.coverUrl = coverUrl
		self.description = description
		self.videoUrl = videoUrl
		self.videoDescription = videoDescription
		self.artist = artist
		self.format = format

	###########
	# METHODS #
	###########
	
	def create(self, album):
		if(os.path.exists(album)):
			self.album = album
			self.fileNumber = len(os.listdir(album))
			self.files = ""
			for music in os.listdir(album):
				self.files += music + "\n"
			self.weigth = subprocess.check_output(['du','-sh', album]).split()[0].decode('utf-8')

			texte =  self.toString()

			os.popen("echo \"" + texte + "\" > \"" + album + ".txt\"")
			log("Création du fichier \"" + album + ".txt\"")

		else:
			error("Impossible de créer le fichier \"" + album + ".txt\", le dossier \"" + album + "\" n'existe pas")
	
	def toString(self):
		return ("[center][u][b][size=200]" + self.title + "[/size][/b][/u]\n"
			"\n"
			"[img]" + self.coverUrl + "[/img]\n"
			"\n"
			"[b]" + self.description + "\n"
			#""
			#"[video]" + self.videoUrl + "[/video]\n"
			#"\n"
			"" + self.videoDescription + "[/b]\n"
			"\n"
			"[img]" + self.bannerUrl + "[/img]\n"
			"\n"
			"[b]artist(s)[/b] : " + self.artist + "\n"
			"[b]Album[/b] : " + self.album + "\n"
			"[b]Format[/b] : " + self.format + "\n"
			"[b]Nombre de fichiers[/b] : " + str(self.fileNumber) + "\n"
			"[b]weigth totale[/b] : " + self.weigth + "o\n"
			"\n"
			"[b]Liste des pistes[/b] :\n"
			"" + str(self.files) + "\n"
			"[img]" + self.seedUrl + "[/img]\n"
			"\n"
			"[b]UPLOAD PAR [color=crimson]" + self.author + "[/color][/b]\n"
			"\n"
			"[img]" + str(self.signatureUrl) + "[/img][/center]")
