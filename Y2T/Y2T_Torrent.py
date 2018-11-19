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
		os.popen("ctorrent -t -u \"" + self.tracker + "\" -s \"" + album + ".torrent\" \"" + album + "\"")
		#os.popen("ctorrent \"" + album + ".torrent\"")
		log.log("Création du fichier \"" + album + ".torrent\"")
			
		