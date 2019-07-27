# coding: utf8

###########
# IMPORTS #
###########

from Y2T.__init__ import ydl_opts
from Y2T.Log import logger
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

	############
	# ATRIBUTS #
	############

	title = None
	coverUrl = None
	description = None
	artist = None
	album = None

	videoUrl = None
	videoDescription = None
	
	author = None
	signatureUrl = None
	
	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, title, coverUrl, description, artist):

		self.title = title
		self.coverUrl = coverUrl
		self.description = description
		self.artist = artist

	###########
	# METHODS #
	###########
	
	def create(self, album):
		if(os.path.exists(album)):
			fileNumber = len(os.listdir(album))
			files = ""
			for music in os.listdir(album):
				files += music + "\n"
			weigth = subprocess.check_output(['du','-sh', album]).split()[0].decode('utf-8')

			text =  self.toString(album, fileNumber, files, weigth)

			file = open(album + ".txt", "w")
			file.write(text)
			file.close()
			logger.debug("Création du fichier \"" + album + ".txt\"")

		else:
			logger.error("Impossible de créer le fichier \"" + album + ".txt\", le dossier \"" + album + "\" n'existe pas")
	
	def toString(self, album, fileNumber, files, weigth):
		text = ("[center][u][b][size=200]" + self.title + "[/size][/b][/u]"
			"\n\n[img]" + self.coverUrl + "[/img]"
			"\n\n[b]" + self.description + "[/b]")

		if(self.videoUrl and self.videoDescription):
			text += ("\n[video]" + self.videoUrl + "[/video]"
				"\n[b]" + self.videoDescription + "[/b]")

		text += ("\n\n[img]" + self.bannerUrl + "[/img]"
			"\n\n[b]Artist[/b] : " + self.artist +
			"\n[b]Album[/b] : " + album)

		if(ydl_opts['postprocessors'][0]['key'] == "FFmpegExtractAudio"):
			text += ("\n[b]Codec[/b] : " + ydl_opts['postprocessors'][0]['preferredcodec'] +
				"\n[b]Quality[/b] : " + ydl_opts['postprocessors'][0]['preferredquality'] + " kbps")
		else:
			text += "\n[b]Format[/b] : " + ydl_opts['postprocessors'][0]['preferedformat']
		
		text += ("\n[b]Nombre de fichiers[/b] : " + str(fileNumber) +
			"\n[b]Taille totale[/b] : " + weigth + "o"
			"\n\n[b]Liste des fichiers[/b] :"
			"\n" + str(files) +
			"\n[img]" + self.seedUrl + "[/img]")

		if(self.author and self.signatureUrl):
			text += ("\n\n[b]UPLOAD PAR [color=crimson]" + self.author + "[/color][/b]\n\n"
				"[img]" + self.signatureUrl + "[/img]")

		return (text + "[/center]")
