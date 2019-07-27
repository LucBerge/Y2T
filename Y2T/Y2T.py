# coding: utf8

###########
# IMPORTS #
###########

import os
from Y2T.__init__ import ydl_opts
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

	def __init__(self, playlistUrl, artist, coverUrl, description, tracker):
		self.playlist = Playlist(playlistUrl, artist)
		self.presentation = Presentation(artist, coverUrl, description, artist)
		self.nfo = Nfo()
		self.torrent = Torrent(tracker)

	#################
	# PARAM METHODS #
	#################
	
	def setAudio(self, codec, quality):
		possible_codec = ["best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", "wav"]

		if(not codec in possible_codec):
			raise Exception("codec " + codec + "does not exist. Have to be " + str(possible_codec))

		possible_quality = [128, 160, 192, 320]

		if(not quality in possible_quality):
			raise Exception("quality " + quality + "does not exist. Have to be " + str(possible_quality))


		ydl_opts['postprocessors'][0] = {
        	'key': 'FFmpegExtractAudio',
        	'preferredcodec': 'mp3',
        	'preferredquality': '192'
        }

	def setVideo(self, format):
		possible_format = ["avi", "flv", "mkv", "mp4", "ogg", "webm"]

		if(not format in possible_format):
			raise Exception("format " + format + "does not exist. Have to be " + str(possible_format))

		ydl_opts['postprocessors'][0] = {
        	'key': 'FFmpegVideoConvertor',
        	'preferedformat': format,
        }

	def addVideo(self, videoUrl, videoDescription):
		self.presentation.videoUrl = videoUrl
		self.presentation.videoDescription = videoDescription

	def addAuthor(self, author, signatureUrl):
		self.presentation.author = author
		self.presentation.signatureUrl = signatureUrl

	###########
	# METHODS #
	###########

	def upload(self, album, cover, year=None, month=None, maximumDuration=600):
		self.download(album, cover, year, month, maximumDuration)
		self.createPresentation(album)
		self.createNfo(album)
		self.createTorrent(album)

	def download(self, album, cover, year=None, month=None, maximumDuration=600):
		self.playlist.download(album, cover, year, month, maximumDuration)

	def createPresentation(self, album):
		self.presentation.create(album)

	def createNfo(self, album):
		if(nfoPackage in os.popen("dpkg -l | grep " + nfoPackage).read()):
			self.nfo.create(album)
		else:
			logger.warning("Impossible de créer le fichier \"" + album + ".nfo\". Vous devez installer " + nfoPackage)

	def createTorrent(self, album):
		if(torrentPackage in os.popen("dpkg -l | grep " + torrentPackage).read()):
			self.torrent.create(album)
		else:
			logger.warning("Impossible de créer le fichier \"" + album + ".torrent\". Vous devez installer " + torrentPackage)