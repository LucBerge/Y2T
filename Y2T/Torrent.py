# coding: utf8

###########
# IMPORTS #
###########

from Y2T.Log import logger
import os

#########
# CLASS #
#########

class Torrent:

	############
	# ATRIBUTS #
	############

	tracker = None

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, tracker):
		self.tracker = tracker

	###########
	# METHODS #
	###########

	def create(self, album):
		if(os.path.exists(album + ".torrent")):
			os.remove(album + ".torrent")

		if(os.path.exists(album)):
			os.popen("transmission-create -p -t \"" + self.tracker + "\" -o \"" + album + ".torrent\" \"" + album + "\"")
			#os.popen("transmission-gtk \"" + album + ".torrent\" &")
			logger.debug("Création du fichier \"" + album + ".torrent\"")
		else:
			logger.error("Impossible de créer le fichier \"" + album + ".torrent\", le dossier \"" + album + "\" n'existe pas")


			
		