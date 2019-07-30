# coding: utf8

###########
# IMPORTS #
###########

import os
from Y2T.Log import logger

#########
# CLASS #
#########

class Torrent:

	#############
	# CONSTANTS #
	#############

	torrentPackage = "transmission-cli"

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

		if(not os.path.exists(album)):
			raise Exception("Impossible de créer le fichier \"" + album + ".torrent\", le dossier \"" + album + "\" n'existe pas")

		if(os.path.exists(album + ".torrent")):
			os.remove(album + ".torrent")

		process = os.popen("transmission-create -p -t \"" + self.tracker + "\" -o \"" + album + ".torrent\" \"" + album + "\"")
		result = process.read()
		process.close()
		if("bad announce URL" in result):
			raise Exception("Impossible de créer le fichier \"" + album + ".torrent\", merci de vérifier votre tracker")
		
		logger.debug("Création du fichier \"" + album + ".torrent\"")


			
		