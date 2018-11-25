# coding: utf8

###########
# IMPORTS #
###########

from Video import *
from Log import *
import os, sys

#############
# PREREQUIS #
#############

reload(sys)
sys.setdefaultencoding('utf-8')

##############
# CONSTANTES #
##############

downloaded_file = "downloaded.txt"

###########
# CLASSES #
###########

class Playlist:
	url = None
	artist =  None
	format =  None
	urls = []
	videos = []

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, url, artist, format):
		self.url = url
		self.artist = artist
		self.format = format
		self.urls = self.getUrls(self.url)

		log(str(len(self.urls)) + " vidéos détectées")

		for url in self.urls:
			self.videos.append(Video(url, self.artist))
		
		self.getInformations()

	def getUrls(self, url):
		urls = []
		RSS_videos=os.popen("youtube-dl -j --flat-playlist \"" + url + "\" | jq -r '.id'").read()
		urls = RSS_videos.split("\n")
		urls.pop(len(urls)-1)
		return urls

	###########
	# METHODS #
	###########

	def getInformations(self):

		log("Analyse de " + str(len(self.videos)) + " vidéos en cours...veuillez patienter...\n")

		for videos in self.videos:
			video.getInformations()
			log(str(videos.index(video)+1) + "/" + str(len(self.videos)),True)

	def download(self, album, cover, year=None, month=None, maximumDuration=600):
		filteredVideos = self.filter(year, month, maximumDuration)

		if(len(filteredVideos)!=0):
			log(str(album) + " : Téléchargement de " + str(len(filteredVideos)) + " videos en cours...veuillez patienter...")
		
			compteur = 0
			for video in filteredVideos :
				compteur+=1
				log(str(compteur) + "/" + str(len(filteredVideos)) + " : " + str(video.numero) + " " + str(video.titre))
				video.download(album, cover)

		else:
			log(str(album) + " : Aucune video à télécharger")

	def filter(self, year, month, maximumDuration):
		filteredVideos = []
		for video in self.videos:
			if(video.duration <= maximumDuration and (year == None or video.year == year) and (month == None or video.month == month)):
				filteredVideos.append(video)
		return filteredVideos