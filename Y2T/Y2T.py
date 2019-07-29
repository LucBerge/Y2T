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
		self._playlist = Playlist(playlistUrl, artist)
		self._presentation = Presentation(artist, coverUrl, description)
		self._nfo = Nfo(artist)
		self._torrent = Torrent(tracker)

	###########
	# GETTERS #
	###########

	@property
	def playlist(self):
		return self._playlist

	@property
	def presentation(self):
		return self._presentation
		
	@property
	def nfo(self):
		return self._nfo
		
	@property
	def torrent(self):
		return self._torrent

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

	###########
	# METHODS #
	###########

	def upload(self, album, cover, year=None, month=None, maximumDuration=600):
		collection = self.playlist.download(album, cover, year, month, maximumDuration)

		if(collection):
			try:
				self.presentation.create(album, year, month, collection)
			except Exception as e:
				logger.error(str(e))

			try:
				self.nfo.create(album, year, month, collection)
			except Exception as e:
				logger.error(str(e))

			try:
				self.torrent.create(album)
			except Exception as e:
				logger.error(str(e))