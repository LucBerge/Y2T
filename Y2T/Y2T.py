# coding: utf8

###########
# IMPORTS #
###########

import os
from Playlist import *
from Presentation import *
from Nfo import *
from Torrent import *
from Log import *


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
		self.playlist = Playlist(playlistUrl, artist, format)
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
			error("Impossible de créer le fichier \"" + album + ".nfo\". Vous devez installer " + nfoPackage)

		#Création du .torrent
		if(torrentPackage in os.popen("dpkg -l | grep " + torrentPackage).read()):
			self.torrent.create(album)
		else:
			error("Impossible de créer le fichier \"" + album + ".torrent\". Vous devez installer " + torrentPackage)
