#!/usr/bin/python

import setuptools

long_description = open("README.md", "r").read()

setuptools.setup(name='Y2T',
      version='1.2',
      author='Esisar Pro-G',
      author_email='esisar.pro.g@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Esisar-Pro-G/Y2T',
      packages=setuptools.find_packages(),
      install_requires=['beautifulsoup4 ', 'youtube-dl', 'mutagen', 'requests'],
      platforms='Linux',
     )
