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
			process = os.popen("transmission-create -p -t \"" + self.tracker + "\" -o \"" + album + ".torrent\" \"" + album + "\"")
			result = process.read()
			process.close()
			if("bad announce URL" in result):
				logger.error("Impossible de créer le fichier \"" + album + ".torrent\", merci de vérifier votre tracker")
			else:
				logger.debug("Création du fichier \"" + album + ".torrent\"")
		else:
			logger.error("Impossible de créer le fichier \"" + album + ".torrent\", le dossier \"" + album + "\" n'existe pas")


			
		