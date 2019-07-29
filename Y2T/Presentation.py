# coding: utf8

###########
# IMPORTS #
###########

import os, subprocess
from Y2T.__init__ import ydl_opts
from Y2T.Utils import *
from Y2T.Log import logger

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

	artist = None
	coverUrl = None
	description = None
	album = None

	videoUrl = None
	videoDescription = None
	
	author = None
	signatureUrl = None
	
	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, artist, coverUrl, description):
		self.artist = artist
		self.coverUrl = coverUrl
		self.description = description

	##########
	# PARAMS #
	##########

	def addVideo(self, videoUrl, videoDescription):
		self.videoUrl = videoUrl
		self.videoDescription = videoDescription

	def addAuthor(self, author, signatureUrl):
		self.author = author
		self.signatureUrl = signatureUrl

	###########
	# METHODS #
	###########
	
	def create(self, album, year, month, collection):
		if(not os.path.exists(album)):
			raise Exception("Impossible de créer le fichier \"" + album + ".txt\", le dossier \"" + album + "\" n'existe pas")

		file = open(album + ".txt", "w")
		file.write(self.toString(album, year, month, collection))
		file.close()
		logger.debug("Création du fichier \"" + album + ".txt\"")
	
	def toString(self, album, year, month, collection):
		text = "[center][u][b][size=200]" + self.artist + "[/size][/b][/u]\n\n[img]" + self.coverUrl + "[/img]\n\n[b]" + self.description + "[/b]"

		if(self.videoUrl and self.videoDescription):
			text += "\n[video]" + self.videoUrl + "[/video]\n[b]" + self.videoDescription + "[/b]"

		text += "\n\n[img]" + self.bannerUrl + "[/img]\n\n[b]Artiste[/b] : " + self.artist + "\n[b]Album[/b] : " + album
		
		if(year):
			text += "\n[b]Annee[/b] : " + str(year)
		if(month):
			text += "\n[b]Mois[/b] : " + str(month)

		text += "\n\n[b]Source[/b] : WebRip"

		if(ydl_opts['postprocessors'][0]['key'] == "FFmpegExtractAudio"):
			text += ("\n[b]Codec[/b] : " + ydl_opts['postprocessors'][0]['preferredcodec'] + "\n[b]Bitrate[/b] : " + ydl_opts['postprocessors'][0]['preferredquality'] + " kbps")
		else:
			text += "\n[b]Format[/b] : " + ydl_opts['postprocessors'][0]['preferedformat']
		
		text += "\n\n[b]Nombre de fichiers[/b] : " + str(len(collection.files)) + "\n[b]Temps de lecture totale[/b] : " + secondsToHHMMSS(collection.duration) + "\n[b]Taille totale[/b] : " + str(bytesToMeagebytes(collection.weight)) + " Mo\n\n[b]Liste des fichiers[/b] :\n" + str(collection) + "\n[img]" + self.seedUrl + "[/img]"

		if(self.author and self.signatureUrl):
			text += "\n\n[b]UPLOAD PAR [color=crimson]" + self.author + "[/color][/b]\n\n[img]" + self.signatureUrl + "[/img]"

		return text + "[/center]"
