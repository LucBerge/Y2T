#!/usr/bin/python
# coding: utf8

import os
import Y2T_Log as log

class Nfo:

	def __init__(self):
		None

	def create(self, album):
		log.log("Création du fichier \"" + album + ".nfo\"")
		os.popen("mediainfo \"" + album + "\" > \"" + album + ".nfo\"").read()
