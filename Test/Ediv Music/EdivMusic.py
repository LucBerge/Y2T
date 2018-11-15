#!/usr/bin/python
# coding: utf8

import Y2T

########
# MAIN #
########

def main():
	Discographie = Y2T.Upload("Ediv Music",
		"https://www.pixenli.com/image/dE2gZ6EV",
		"Ediv Music try to bring you the best music out there, so they don’t have to search SoundCloud, YouTube and Spotify channels 24/7. We seperate the men from the boys and the rubbish from the diamonds. ",
		"https://www.youtube.com/watch?v=bNppHOYIgRE",
		"Every day should feel like valentinesday right? That's why this channel brings you all the new Tropical, Summer and Deep House every day.",
		"mp3",
		"https://www.youtube.com/channel/UCBVwKRYmERFiIbheXEATDqw/videos",
		"___TRACKER___")
	
	Discographie.upload("Collection 2015", "Collection 2015.jpg",2015)
	Discographie.upload("Collection 2016", "Collection 2016.jpg",2016)
	Discographie.upload("Collection 2017", "Collection 2017.jpg",2017)

##########
# GLOBAL #
##########

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		None