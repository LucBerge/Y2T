# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
import youtube_dl, os, glob, fnmatch
from Y2T.__init__ import ydl_opts
from Y2T.Utils import *
from Y2T.Log import logger
from mutagen.id3 import ID3, COMM, TALB, TCON, TDRC, TIT2, TPE1, TRCK, APIC

#########
# CLASS #
#########

class Video:

	#############
	# CONSTANTS #
	#############

	comment = "Create with Y2T. See https://github.com/Esisar-Pro-G/Y2T"

	############
	# ATRIBUTS #
	############

	url = None
	artist =  None
	title = None
	year = None
	month = None
	duration = None

	album = None
	cover = None
	track = None
	weight = None
	downloaded = None

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, info, artist):
		self.url = info['webpage_url']
		self.artist = artist

		self.title = info['title']

		self.year = int(info["upload_date"][0:4])
		self.month = int(info["upload_date"][4:6])
		self.day = int(info["upload_date"][6:8])
		self.duration = info["duration"]

	##############
	# DOWNLOADED #
	##############

	def isDownloaded(self):
		out = False
		if(os.path.exists(downloaded_file)):
			file = open(downloaded_file,"r+")
			out = (self.url in file.read())
			file.close()
		return out

	def setDownoaded(self):
		file = open(downloaded_file,"a")
		file.write(self.url+"\n") 
		file.close()

	###########
	# METHODS #
	###########

	def download(self, album, cover):
		self.album = album
		self.cover = cover

		if(not os.path.isdir(self.album)):
			os.mkdir(self.album, 755)

		os.chdir(self.album)
		ydl = youtube_dl.YoutubeDL(ydl_opts)
		
		try :
			ydl.download([self.url])
			self.track = len(fnmatch.filter(os.listdir("."), '*'))
			self.weight = os.path.getsize(max(glob.glob("*"), key=os.path.getctime))
			self.downloaded = True

			if(ydl_opts['postprocessors'][0]['key'] == 'FFmpegExtractAudio'):
				if(ydl_opts['postprocessors'][0]['preferredcodec'] == 'mp3'):
					self.setTags()

		except youtube_dl.utils.DownloadError:
			self.downloaded = False
			logger.warning("Impossible de télécharger " + self.url)

		os.chdir("..")
		return self.downloaded

	def setTags(self):
		musique = ID3(max(glob.glob("*"), key=os.path.getctime))

		musique.add(TPE1(encoding=3, text=str(self.artist)))
		musique.add(TALB(encoding=3, text=str(self.album)))
		musique.add(TIT2(encoding=3, text=str(self.title)))

		musique.add(TRCK(encoding=3, text=str(self.track)))

		if(self.year != None):
			musique.add(TDRC(encoding=3, text=str(self.year)))

		musique.add(COMM(encoding=3, text=str(self.comment)))

		image = open("../" + self.cover,"rb").read()
		musique.add(APIC(3, 'image/png', 3, 'Front cover', image))
				
		musique.save(v2_version=3)

	def __str__(self):
		return str(self.track) + " : " + self.title + " [" + secondsToHHMMSS(self.duration) + "]"