# coding: utf8

###########
# IMPORTS #
###########

import os
from Y2T.__init__ import ydl_opts
from Y2T.Utils import *
from Y2T.Log import logger

#########
# CLASS #
#########

class Nfo:

	#############
	# CONSTANTS #
	#############

	nfoPackage = "mediainfo"

	############
	# ATRIBUTS #
	############

	artist = None
	mediainfo = None

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, artist):
		self.artist = artist
		self._mediainfo = False

	####################
	# GETTER & SETTERS #
	####################

	@property
	def mediainfo(self):
		return self._mediainfo

	@mediainfo.setter
	def mediainfo(self, mediainfo):
		self._mediainfo = mediainfo

	###########
	# METHODS #
	###########
	
	def create(self, album, year, month, collection):

		if(not os.path.exists(album)):
			raise Exception("Impossible de créer le fichier \"" + album + ".nfo\", le dossier \"" + album + "\" n'existe pas")

		if(self.mediainfo):
			process = os.popen("dpkg -l | grep " + nfoPackage)
			result = process.read()
			process.close()

			if(not nfoPackage in result):
				raise Exception("Impossible de créer le fichier \"" + album + ".nfo\" avec mediainfo. Vous devez installer " + nfoPackage)

			os.popen("mediainfo \"" + album + "\" > \"" + album + ".nfo\"").close()
					
		else:
			file = open(album + ".nfo", "w")
			file.write(self.toString(album, year, month, collection))
			file.close()

		logger.debug("Création du fichier \"" + album + ".nfo\"")

	def toString(self, album, year, month, collection):
		text = "========== " + self.artist + " ==========\n\nArtiste : " + self.artist + "\nAlbum : " + album
		
		if(year):
			text += "\nAnnee : " + str(year)
		if(month):
			text += "\nMois : " + str(month)

		text += "\n\nSource : WebRip"

		if(ydl_opts['postprocessors'][0]['key'] == "FFmpegExtractAudio"):
			text += ("\nCodec : " + ydl_opts['postprocessors'][0]['preferredcodec'] + "\nBitrate : " + ydl_opts['postprocessors'][0]['preferredquality'] + " kbps")
		else:
			text += "\nFormat : " + ydl_opts['postprocessors'][0]['preferedformat']
		
		text += "\n\nNombre de fichiers : " + str(len(collection.files)) + "\nTemps de lecture totale : " + secondsToHHMMSS(collection.duration) + "\nTaille totale : " + str(bytesToMeagebytes(collection.weight)) + " Mo\n\n========== Liste des fichiers ==========\n" + str(collection)

		return text + "\n\n========== Créé avec Y2T =========="