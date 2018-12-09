#!/usr/bin/python

from distutils.core import setup

setup(name='Y2T',
      author='Esisar Pro-G',
      description='Create torrents from youtube playlist',
      author_email='esisar.pro.g@gmail.com',
      url='https://github.com/Esisar-Pro-G/Y2T',
      version='1.2',
      packages=['Y2T'],
      download_url='https://github.com/Esisar-Pro-G/Y2T',
      install_requires=['beautifulsoup4 ', 'youtube-dl', 'mutagen'],
      platforms='Linux',
     )
