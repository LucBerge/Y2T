import sys
if sys.version_info < (3, 5):
    sys.exit('Y2T requires Python 3.5+')

long_description = open("README.md", "r").read()

import setuptools
setuptools.setup(
	name='Y2T',
	version='1.4',
	author='Esisar Pro-G',
	author_email='esisar.pro.g@gmail.com',
	description="Youtube to Torrent",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/Esisar-Pro-G/Y2T',
	packages=setuptools.find_packages(),
	install_requires=['youtube-dl', 'mutagen'],
	platforms='Linux'
)
