# coding: utf8

###########
# IMPORTS #
###########

import os
from Y2T.Playlist import *
from Y2T.Presentation import *
from Y2T.Nfo import *
from Y2T.Torrent import *
from Y2T.Log import logger


#############
# CONSTANTS #
#############

nfoPackage = "mediainfo"
torrentPackage = "transmission-cli"

#########
# CLASS #
#########

class Upload:

	############
	# ATRIBUTS #
	############

	playlist = None
	presentation = None
	nfo = None
	torrent = None

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, playlistUrl, artist, coverUrl, description, videoUrl, videoDescription, format, tracker):
		self.playlist = Playlist(playlistUrl, artist)
		self.presentation = Presentation(artist, coverUrl, description, videoUrl, videoDescription, artist, format)
		self.nfo = Nfo()
		self.torrent = Torrent(tracker)

	###########
	# METHODS #
	###########
	
	def upload(self, album, cover, year=None, month=None, maximumDuration=600):

		#Téléchargement
		self.playlist.download(album, cover, year, month, maximumDuration)

		#Création de la presentation	
		self.presentation.create(album)

		#Creation du nfo
		if(nfoPackage in os.popen("dpkg -l | grep " + nfoPackage).read()):
			self.nfo.create(album)
		else:
			logger.warning("Impossible de créer le fichier \"" + album + ".nfo\". Vous devez installer " + nfoPackage)

		#Création du .torrent
		if(torrentPackage in os.popen("dpkg -l | grep " + torrentPackage).read()):
			self.torrent.create(album)
		else:
			logger.warning("Impossible de créer le fichier \"" + album + ".torrent\". Vous devez installer " + torrentPackage)
