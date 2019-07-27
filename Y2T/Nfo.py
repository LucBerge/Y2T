# coding: utf8

###########
# IMPORTS #
###########

from Y2T.Log import logger
import os

#########
# CLASS #
#########

class Nfo:

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self):
		None

	###########
	# METHODS #
	###########
	
	def create(self, album):

		if(os.path.exists(album)):
			os.popen("mediainfo \"" + album + "\" > \"" + album + ".nfo\"").read()
			logger.debug("Création du fichier \"" + album + ".nfo\"")
		else:
			logger.error("Impossible de créer le fichier \"" + album + ".nfo\", le dossier \"" + album + "\" n'existe pas")
