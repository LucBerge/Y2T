#!/usr/bin/python

from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
	'outtmpl' : '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'download_archive': 'downloaded.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook]
}
ydl = youtube_dl.YoutubeDL(ydl_opts)
ydl.download(["https://www.youtube.com/watch?v=HoCw_gaCHXE"])