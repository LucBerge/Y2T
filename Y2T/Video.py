# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import log, os, sys, glob, requests, fnmatch
from mutagen.id3 import ID3, COMM, TALB, TCON, TDRC, TIT2, TPE1, TRCK, APIC

#############
# CONSTANTS #
#############

downloaded_file = "downloaded.txt"

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

	def __init__(self, url, artist):

		self.url = url
		self.artist = artist

	##############
	# DOWNLOADED #
	##############

	def isDownoaded(self):
		file = open(downloaded_file,"r+")
		out = self.url in file.read()
		file.close()
		return out

	def setDownoaded(self):
		file = open(downloaded_file,"a")
		file.write(self.url+"\n") 
		file.close()

	###########
	# METHODS #
	###########

	def getInformations(self):

		if(not isDownloaded()):
			req = requests.get(self.url)
			soup = BeautifulSoup(req.text, "html.parser")

			for i in soup.find_all('meta'):
				meta = str(i).decode('utf-8')
				if "itemprop" in meta:
					if "name" in meta:
						self.title = i["content"]
					if "datePublished" in meta:
						date=str(i["content"])
						self.year = int(date[0:4])
						self.month = int(date[5:7])
					if "duration" in meta:
						duration_str = i["content"]
						T=duration_str.index('T')
						M=duration_str.index('M')
						self.duration = int(duration_str[T+1:M])*60 + int(duration_str[M+1:-1])

	def telecharger(self, album, cover):
		
		self.album = album
		self.cover = cover

		if(not isDownloaded()):
			if(not os.path.isdir(self.album)):
				os.mkdir(self.album, 0755)

			os.chdir(self.album)
			Telechargment=os.popen("youtube-dl -x --audio-format mp3 --audio-quality 192 -o \"" + self.album + "\%(title)s.%(ext)s\" " + self.url).read()
				
			if "100%" in Telechargment:
				setTags()
				os.chdir("..")
				setDownoaded()

			else:
				os.chdir("..")
				erreur("Impossible de télécharger " + self.url)
		else:
			warning(self.title + " déjà téléchargé")

	def setTags(self):
		musique = ID3(max(glob.glob("\"" + self.album + "/*\""), key=os.path.getctime))

		musique.add(TPE1(encoding=3, text=unicode(self.artist)))
		musique.add(TALB(encoding=3, text=unicode(self.album)))
		musique.add(TIT2(encoding=3, text=unicode(self.title)))

		self.trackNumber = len(fnmatch.filter(os.listdir("\"" + self.album + "/\""), '*.mp3'))
		musique.add(TRCK(encoding=3, text=unicode(self.trackNumber)))

		if(self.year != None):
			musique.add(TDRC(encoding=3, text=unicode(self.year)))

		musique.add(COMM(encoding=3, text=unicode(self.commentaire)))

		image = open("../"+self.cover,"rb").read()
		musique.add(APIC(3, 'image/png', 3, 'Front cover', image))
				
		musique.save(v2_version=3)