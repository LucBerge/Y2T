[![release](https://img.shields.io/badge/release-1.2-succes.svg)](https://pypi.org/project/Y2T/)

# Y2T - Youtube to Torrents

## Description

Youtube to Torrent est un outil python fonctionnant sous Linux permettant de créer un ou plusieurs fichiers torrents à partir d'une playlist youtube.
L'objectif est de simplifier la création des fichiers nécessaires au partage de contenu musical.

Y2T permet de :
- Analyser, filtrer et télécharger les vidéos d'une playlist au format mp3
- Ajouter les tags mp3
- Créer la présentation du torrent
- Créer le fichier .nfo
- Créer le fichier .torrent

## Prérequis

```
sudo apt-get install python-pip ffmpeg
```

**Optionnel**

Les paquets suivant peuvent ne pas être installé. Dans ce cas là, les fichiers correspondant ne seront pas générés.

- `mediainfo` permet de créer les fichiers .nfo
- `transmission-cli` permet de créer les fichiers .torrent

Il est recommandé de les installer avec la commande suivante :
```
sudo apt install mediainfo transmission-cli transmission-gtk
```

## Installation

Vous pouvez installer Y2T directement depuis le dépôt [PyPi](https://pypi.org/project/Y2T/) :
```
sudo pip install Y2T
```

**Mise à jour**
```
sudo pip install Y2T -U
```

## Désinstallation

Pour désinstaller Y2T :
```
sudo pip uninstall Y2T
```

## Utilisation

Le code ci-dessous permet de générer tous les fichiers nécessaires pour uploader la discographie de [Ediv Music](https://www.youtube.com/c/edivmusic).
Chaque album représente une année.
```
import Y2T
Discographie = Y2T.Upload("https://www.youtube.com/channel/UCBVwKRYmERFiIbheXEATDqw/videos",
		"Ediv Music",
		"https://www.pixenli.com/image/dE2gZ6EV",
		"Ediv Music try to bring you the best music out there, so they don’t have to search SoundCloud, YouTube and Spotify channels 24/7. We seperate the men from the boys and the rubbish from the diamonds. ",
		"https://www.youtube.com/watch?v=bNppHOYIgRE",
		"Every day should feel like valentinesday right? That's why this channel brings you all the new Tropical, Summer and Deep House every day.",
		"mp3",
		"___TRACKER___")
	
  Discographie.upload("Collection 2015", "Collection 2015.jpg",2015)
  Discographie.upload("Collection 2016", "Collection 2016.jpg",2016)
  Discographie.upload("Collection 2017", "Collection 2017.jpg",2017)
  Discographie.upload("Collection 2018", "Collection 2018.jpg",2018)
```

Vous pouvez aussi consulter les [exemples](https://github.com/LucBerge/Y2T/tree/master/examples) fournis.

## Contribution

Pour contribuer au projet, vous devez réaliser un fork du projet vers votre espace personnel. Vous pourrez alors faire un pull request en temps voulu. Merci de contacter [@LucBerge](https://github.com/LucBerge) pour plus d'informations sur les tâches à réaliser.
