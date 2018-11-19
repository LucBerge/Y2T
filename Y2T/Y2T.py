#!/usr/bin/python
# coding: utf8

import Y2T_Download, Y2T_Presentation, Y2T_Nfo, Y2T_Torrent, os
import Y2T_Log as log

nfo_package = "mediainfo"
torrent_package = "transmission-cli"

class Upload:

	playlist = None
	presentation = None
	nfo = None
	torrent = None

	def __init__(self, artist, url_couverture, description, url_video, description_video, format, playlist_url, tracker):
		self.playlist = Y2T_Download.Playlist(playlist_url, artist)
		self.presentation = Y2T_Presentation.Presentation(artist, url_couverture, description, url_video, description_video, artist, format)
		self.nfo = Y2T_Nfo.Nfo()
		self.torrent = Y2T_Torrent.Torrent(tracker)

	def upload(self, album, cover, annee=None, mois=None, duree_max=600):

		#Téléchargement
		self.playlist.telecharger(album, cover, annee, mois, duree_max)

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
