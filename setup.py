#!/usr/bin/python

from distutils.core import setup

setup(name='Y2T',
      version='1.0',
      description='Create torrents from youtube playlist',
      author='Esisar Pro-G',
      author_email='esisar.pro.g@gmail.com',
      url='https://github.com/Esisar-Pro-G/Y2T',
      packages=['beautifulsoup4 ', 'youtube-dl', 'mutagen'],
     )