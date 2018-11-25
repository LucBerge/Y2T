#!/usr/bin/python
# coding: utf8

import os
import Y2T_Log as log

class Torrent:

	tracker = None

	def __init__(self, tracker):
		self.tracker = tracker

	def create(self, album):
		if(os.path.exists(album + ".torrent")):
			os.remove(album + ".torrent")
		log.log("Création du fichier \"" + album + ".torrent\"")
		os.popen("transmission-create -p -t \"" + self.tracker + "\" -o \"" + album + ".torrent\" \"" + album + "\"")
		os.popen("transmission-gtk \"" + album + ".torrent\" &")
			
		