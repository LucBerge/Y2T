#!/usr/bin/python
# coding: utf8

import json

options = {
	"outtmpl" : "%(title)s.%(ext)s",
	"audioFormat" : "mp3",
	"audioQuality" : 192,
	"maxDuration" : 600
}

data = {
	"playlistUrl" : "https://www.youtube.com/channel/UCBVwKRYmERFiIbheXEATDqw/videos",
	"artist" : "Ediv Music",
	"coverUrl" : "https://www.pixenli.com/image/dE2gZ6EV",
	"description" : "Ediv Music try to bring you the best music out there, so they don't have to search SoundCloud, YouTube and Spotify channels 24/7. We seperate the men from the boys and the rubbish from the diamonds. ",
	"videoUrl" : "https://www.youtube.com/watch?v=bNppHOYIgRE",
	"videoDescription" : "Every day should feel like valentinesday right? That's why this channel brings you all the new Tropical, Summer and Deep House every day.",
	"tracker" : "___TRACKER___",
	"options" : options
}

#json = json.dumps(data)

f = open("data.json", 'w')
json.dump(data, f, indent=4, sort_keys=False, ensure_ascii=False)

#f = open("data.json","w")
#f.write(json)
f.close()