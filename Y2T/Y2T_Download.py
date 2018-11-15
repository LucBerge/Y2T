#!/usr/bin/python
# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import eyed3, os, sys, youtube_dl, glob, requests, fnmatch, inspect

################
# ENUMERATIONS #
################

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CR = '\033[F'

#############
# PREREQUIS #
#############

reload(sys)
sys.setdefaultencoding('utf-8')
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

##############
# CONSTANTES #
##############

downloaded_file = "downloaded.txt"

###########
# CLASSES #
###########

class Playlist:
	playlist_url = "defaut"
	urls = []
	urls_a_telecharger = []
	videos = []
	artist =  "defaut"

	def __init__(self, playlist_url, artist):
		self.playlist_url = playlist_url
		self.artist = artist
		self.urls = self.get_playlist_links(self.playlist_url)

		if(not os.path.exists(downloaded_file)):
			os.mknod(downloaded_file)

		for playlist_url in self.urls:
			if (playlist_url not in open(downloaded_file).read()):
				self.urls_a_telecharger.append("https://www.youtube.com/watch?v=" + playlist_url)
		
		log(str(len(self.urls)) + " vidéos détectées")

		if(len(self.urls) != len(self.urls_a_telecharger)):
			attention(str(len(self.urls)-len(self.urls_a_telecharger)) + " vidéos déjà téléchargées")
		
		log("Analyse de " + str(len(self.urls_a_telecharger)) + " vidéos en cours...veuillez patienter...\n")

		for i in range(len(self.urls_a_telecharger)):
			self.videos.append(Video(self.urls_a_telecharger[i], self.artist))
			log(str(i+1) + "/" + str(len(self.urls_a_telecharger)),True)

	def get_playlist_links(self, playlist_url):
		ids = []
		RSS_videos=os.popen("youtube-dl -j --flat-playlist \"" + playlist_url + "\" | jq -r '.id'").read()
		ids = RSS_videos.split("\n")
		ids.pop(len(ids)-1)
		return ids

		req = requests.get(playlist_url)
		soup = BeautifulSoup(req.text, "html.parser")

		for i in soup.find_all('link'):
			if "watch" in i["href"]:
				ids.append(i['href'])
		return ids

	def telecharger(self, album, couverture, annee=None, mois=None, duree_max=600):
		videos_a_telecharger = self.filtrer(annee, mois, duree_max)

		if(len(videos_a_telecharger)!=0):
			log(str(album) + " : Téléchargement de " + str(len(videos_a_telecharger)) + " videos en cours...veuillez patienter...")
		else:
			log(str(album) + " : Aucune video à télécharger")
		

		compteur = 0
		for video in videos_a_telecharger :
			compteur+=1
			log(str(compteur) + "/" + str(len(videos_a_telecharger)) + " : " + str(video.numero) + " " + str(video.titre))
			video.telecharger(album, couverture)

	def filtrer(self, annee, mois, duree_max):
		videos_a_telecharger = []

		compteur = 0
		for video in self.videos:

			if(video.duree <= duree_max and (annee == None or video.annee == annee) and (mois == None or video.mois == mois)):				
				compteur+=1
				video.numero = compteur
				videos_a_telecharger.append(video)

		return videos_a_telecharger


class Video:

	url = "defaut"
	artist =  "defaut"
	titre = "defaut"
	annee = 0
	mois = 0
	duree = 0
	numero = 0

	def __init__(self, url, artist):

		self.url = url
		self.artist = artist

		req = requests.get(self.url)
		soup = BeautifulSoup(req.text, "html.parser")

		for i in soup.find_all('meta'):
			meta = str(i).decode('utf-8')
			if "itemprop" in meta:
				if "name" in meta:
					self.titre = i["content"]
				if "datePublished" in meta:
					date=str(i["content"])
					self.annee = int(date[0:4])
					self.mois = int(date[5:7])
				if "duration" in meta:
					duree_str = i["content"]
					T=duree_str.index('T')
					M=duree_str.index('M')
					self.duree = int(duree_str[T+1:M])*60 + int(duree_str[M+1:-1])

	def telecharger(self, album, couverture):
		
		if(not os.path.isdir(album)):
			os.mkdir(album, 0755)

		os.chdir(album)
		Telechargment=os.popen("youtube-dl -x --audio-format mp3 --audio-quality 192 -o \"%(title)s.%(ext)s\" " + self.url).read()
			
		if "100%" in Telechargment:

			musique = eyed3.load(max(glob.glob("*"), key=os.path.getctime))
			musique.tag.artist = unicode(self.artist.encode('iso8859_1'),'iso8859_1')
			musique.tag.album = unicode(album)
			musique.tag.title = unicode(self.titre)
			musique.tag.track_num = len(fnmatch.filter(os.listdir('.'), '*.mp3'))

			image = open("../"+couverture,"rb").read()
			musique.tag.images.set(3,image,"image/png")
				
			musique.tag.save()
			os.chdir("..")

			file = open(downloaded_file,"a")
			file.write(self.url+"\n") 
			file.close()

		else:
			os.chdir("..")
			erreur("Impossible de télécharger " + self.url)

#############
# AFFICHAGE #
#############

def log(texte, CR=False):
	if(CR==True):
		print(bcolors.CR + bcolors.OKGREEN + "LOG : " + bcolors.ENDC + texte)
	else:
		print(bcolors.OKGREEN + "LOG : " + bcolors.ENDC + texte)

def attention(texte):
	print(bcolors.WARNING + "ATTENTION : " + bcolors.ENDC + texte)

def erreur(texte):
	print(bcolors.FAIL + "ERREUR : " + bcolors.ENDC + texte)