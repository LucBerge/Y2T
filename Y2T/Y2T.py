#!/usr/bin/python
# coding: utf8

import Playlist, Presentation, Nfo, Torrent, Log, os

nfo_package = "mediainfo"
torrent_package = "transmission-cli"

class Upload:

	playlist = None
	presentation = None
	nfo = None
	torrent = None

	def __init__(self, playlist_url, artist, url_couverture, description, url_video, description_video, format, tracker):
		self.playlist = Playlist(playlist_url, artist, format)
		self.presentation = Presentation(artist, url_couverture, description, url_video, description_video, artist, format)
		self.nfo = Nfo()
		self.torrent = Torrent(tracker)

	def upload(self, album, cover, year=None, month=None, maximumDuration=600):

		#Téléchargement
		self.playlist.telecharger(album, cover, year, month, maximumDuration)

		#Création de la presentation	
		self.presentation.create(album)

		#Creation du nfo
		if(nfo_package in os.popen("dpkg -l | grep " + nfo_package).read()):
			self.nfo.create(album)
		else:
			log.erreur("Impossible de créer le fichier \"" + album + ".nfo\". Vous devez installer " + nfo_package)

		#Création du .torrent
		if(torrent_package in os.popen("dpkg -l | grep " + torrent_package).read()):
			self.torrent.create(album)
		else:
			log.erreur("Impossible de créer le fichier \"" + album + ".torrent\". Vous devez installer " + torrent_package)
