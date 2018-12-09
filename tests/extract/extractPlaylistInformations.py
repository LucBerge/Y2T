#!/usr/bin/python


from __future__ import unicode_literals
import youtube_dl, sys
from pprint import pprint
import youtube_dl
from Y2T import Log
sys.path.insert(0, '../../Y2T')

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'logger': Log(),
    'progress_hooks': [my_hook],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)
info = ydl.extract_info('https://www.youtube.com/watch?v=HoCw_gaCHXE&list=PLRBp0Fe2Gpgls1yxsv4NK1uuqX8B-g1T9', download=False)

urls = [video['webpage_url'] for video in info['entries']]

for url in urls:
	print(url)

pprint(info)