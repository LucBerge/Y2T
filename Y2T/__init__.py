# coding: utf8

from __future__ import unicode_literals
from Y2T.Y2T import *

ydl_opts = {
	'outtmpl' : '%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'download_archive': '../downloaded.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}