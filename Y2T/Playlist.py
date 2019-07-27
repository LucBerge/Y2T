# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
from Y2T.Video import *
from Y2T.__init__ import ydl_opts
from Y2T.Log import logger
import os, sys, youtube_dl

#############
# PREREQUIS #
#############

#reload(sys)
#sys.setdefaultencoding('utf-8')

###########
# CLASSES #
###########

class Playlist:

	############
	# ATRIBUTS #
	############

	url = None
	artist =  None
	videos = []

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, url, artist):
		self.url = url
		self.artist = artist

	###########
	# METHODS #
	###########

	def getInformations(self):

		logger.debug("Analyse de  la playlist en cours...veuillez patienter...")
		ydl = youtube_dl.YoutubeDL(ydl_opts)
		info = ydl.extract_info(self.url, download=False)

		for videoInfo in info['entries']:
			self.videos.append(Video(videoInfo, self.artist))

	def download(self, album, cover, year=None, month=None, maximumDuration=600):

		if(not len(self.videos)):
			self.getInformations()

		filteredVideos = self.filter(year, month, maximumDuration)

		if(len(filteredVideos)!=0):
			logger.debug(str(album) + " : Téléchargement de " + str(len(filteredVideos)) + " videos en cours...veuillez patienter...")
		
			for video in filteredVideos :
				logger.debug(str(filteredVideos.index(video)+1) + "/" + str(len(filteredVideos)) + " : " + str(video.url))
				video.download(album, cover)

		else:
			logger.debug(str(album) + " : Aucune video à télécharger")

	def filter(self, year, month, maximumDuration):
		filteredVideos = []
		for video in self.videos:
			if(video.duration <= maximumDuration and (year == None or video.year == year) and (month == None or video.month == month)):
				filteredVideos.append(video)
		return filteredVideos