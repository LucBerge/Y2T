#!/usr/bin/python
# coding: utf8

###########
# IMPORTS #
###########

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import os, sys, youtube_dl, glob, requests, fnmatch, inspect
from mutagen.id3 import ID3, COMM, TALB, TCON, TDRC, TIT2, TPE1, TRCK, APIC
import Y2T_Log as log

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
		
		log.log(str(len(self.urls)) + " vidéos détectées")

		if(len(self.urls) != len(self.urls_a_telecharger)):
			log.attention(str(len(self.urls)-len(self.urls_a_telecharger)) + " vidéos déjà téléchargées")
		
		if(len(self.urls_a_telecharger) > 0):
			log.log("Analyse de " + str(len(self.urls_a_telecharger)) + " vidéos en cours...veuillez patienter...\n")

			for i in range(len(self.urls_a_telecharger)):
				self.videos.append(Video(self.urls_a_telecharger[i], self.artist))
				log.log(str(i+1) + "/" + str(len(self.urls_a_telecharger)),True)

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
			log.log(str(album) + " : Téléchargement de " + str(len(videos_a_telecharger)) + " videos en cours...veuillez patienter...")
		else:
			log.log(str(album) + " : Aucune video à télécharger")
		

		compteur = 0
		for video in videos_a_telecharger :
			compteur+=1
			log.log(str(compteur) + "/" + str(len(videos_a_telecharger)) + " : " + str(video.numero) + " " + str(video.titre))
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
	commentaire = "Créé avec Y2T"

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

			musique = ID3(max(glob.glob("*"), key=os.path.getctime))

			musique.add(TPE1(encoding=3, text=unicode(self.artist)))
			musique.add(TALB(encoding=3, text=unicode(album)))
			musique.add(TIT2(encoding=3, text=unicode(self.titre)))
			musique.add(TRCK(encoding=3, text=unicode(len(fnmatch.filter(os.listdir('.'), '*.mp3')))))

			if(self.annee != 0):
				musique.add(TDRC(encoding=3, text=unicode(self.annee)))

			musique.add(COMM(encoding=3, text=unicode(self.commentaire)))

			image = open("../"+couverture,"rb").read()
			musique.add(APIC(3, 'image/png', 3, 'Front cover', image))
				
			musique.save(v2_version=3)
			os.chdir("..")

			file = open(downloaded_file,"a")
			file.write(self.url+"\n") 
			file.close()

		else:
			os.chdir("..")
			log.erreur("Impossible de télécharger " + self.url)