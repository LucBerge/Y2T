# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
import youtube_dl
import os, glob, fnmatch
from Y2T.__init__ import ydl_opts
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
	album = None
	year = None
	month = None
	duration = None
	trackNumber = None
	cover = None

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, info, artist):
		self.url = info['webpage_url']
		self.artist = artist

		self.title = info['title']
		date = info["upload_date"]

		self.year = int(date[0:4])
		self.month = int(date[5:7])
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
			if(ydl_opts['postprocessors'][0]['key'] == 'FFmpegExtractAudio'):
				if(ydl_opts['postprocessors'][0]['preferredcodec'] == 'mp3'):
					self.setTags()

		except youtube_dl.utils.DownloadError:
			logger.warning("Impossible de télécharger " + self.url)

		os.chdir("..")

	def setTags(self):
		musique = ID3(max(glob.glob("*"), key=os.path.getctime))

		musique.add(TPE1(encoding=3, text=str(self.artist)))
		musique.add(TALB(encoding=3, text=str(self.album)))
		musique.add(TIT2(encoding=3, text=str(self.title)))

		self.trackNumber = len(fnmatch.filter(os.listdir("."), '*.mp3'))
		musique.add(TRCK(encoding=3, text=str(self.trackNumber)))

		if(self.year != None):
			musique.add(TDRC(encoding=3, text=str(self.year)))

		musique.add(COMM(encoding=3, text=str(self.comment)))

		image = open("../" + self.cover,"rb").read()
		musique.add(APIC(3, 'image/png', 3, 'Front cover', image))
				
		musique.save(v2_version=3)
