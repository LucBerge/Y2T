#!/usr/bin/python
# coding: utf8

import Y2T_Download, Y2T_Presentation, Y2T_Torrent, os

class Upload:

	playlist = None
	presentation = None
	tracker = None

	def __init__(self, artist, url_couverture, description, url_video, description_video, format, playlist_url, tracker):
		self.playlist = Y2T_Download.Playlist(playlist_url, artist)
		self.presentation = Y2T_Presentation.Presentation(artist, url_couverture, description, url_video, description_video, artist, format)
		self.tracker = tracker

	def upload(self, album, cover, annee=None, mois=None, duree_max=600):

		#Téléchargement
		self.playlist.telecharger(album, cover, annee, mois, duree_max)

		#Creation du nfo
		os.popen("mediainfo \"" + album + "\" > \"" + album + ".nfo\"").read()

		#Création du .torrent
		if(os.path.exists(album + ".torrent")):
			os.remove(album + ".torrent")
		
		os.popen("ctorrent -t -u \"" + tracker + "\" -s \"" + album + ".torrent\" \"" + album + "\"")
		os.popen("ctorrent \"" + album + ".torrent\"")

		#Création de la presentation
		self.presentation.save(album)