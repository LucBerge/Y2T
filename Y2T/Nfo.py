# coding: utf8

###########
# IMPORTS #
###########

from Log import *
from __init__ import log
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
			log.debug("Création du fichier \"" + album + ".nfo\"")
		else:
			log.error("Impossible de créer le fichier \"" + album + ".nfo\", le dossier \"" + album + "\" n'existe pas")
