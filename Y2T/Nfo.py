# coding: utf8

###########
# IMPORTS #
###########

from Log import *
import Log, os

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
			log("Création du fichier \"" + album + ".nfo\"")
		else:
			error("Impossible de créer le fichier \"" + album + ".nfo\", le dossier \"" + album + "\" n'existe pas")
