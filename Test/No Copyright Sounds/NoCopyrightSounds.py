#!/usr/bin/python

import YAD

########
# MAIN #
########

def main():
	
	Discographie = Y2T.Upload("NoCopyrightSounds",
		"https://www.pixenli.com/miniature/BbVhq96B",
		"Originaire du Royaume-Unis, NCS - NoCopyrightSounds est une coopérative de musique créée par plusieurs DJ et compositeurs. NCS tient à maintenir sa production musicale gratuite et à la disposition de quiconque. Conformément à leurs exigences, les noms des musiques n'ont pas été modifiées.",
		"https://www.youtube.com/watch?v=J2X5mJ3HDYE",
		"Vous pouvez les soutenir en suivant leur [url=https://www.youtube.com/user/NoCopyrightSounds]chaine youtube[/url] ou encore en vous rendant directement sur leur [url=http://www.ncsmusic.com/]site[/url].",
		"mp3",
		"https://www.youtube.com/user/NoCopyrightSounds/videos",
		"___TRACKER___")
	
	Discographie.upload("Collection 2015", "Collection 2015.jpg",2015)
	Discographie.upload("Collection 2016", "Collection 2016.jpg",2016)
	Discographie.upload("Collection 2017", "Collection 2017.jpg",2017)

	# Trap = Playlist("https://www.youtube.com/watch?v=-xKKo7t72Tg&list=PLRBp0Fe2GpglkzuspoGv-mu7B2ce9_0Fn","NoCopyrightSounds")
	# House = Playlist("https://www.youtube.com/watch?v=CkC5igeV_tM&list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK","NoCopyrightSounds")
	# Dubstep = Playlist("https://www.youtube.com/watch?v=V42iRj0Toq0&list=PLRBp0Fe2Gpglq-J-Hv0p-y0wk3lQk570u","NoCopyrightSounds")
	# DrumBass = Playlist("https://www.youtube.com/watch?v=7TFoiA8rNLc&list=PLRBp0Fe2GpgnzYdHtTCoBYPyIJG9_opMn","NoCopyrightSounds")
	# Electronic = Playlist("https://www.youtube.com/watch?v=tua4SVV-GSE&list=PLRBp0Fe2GpgnZOm5rCopMAOYhZCPoUyO5","NoCopyrightSounds")
	# MelodicDubstep = Playlist("https://www.youtube.com/watch?v=ZPuvoDZj2hM&list=PLRBp0Fe2Gpgm57nFVNM7qYZ9u64U9Q-Bf","NoCopyrightSounds")
	# IndieDance = Playlist("https://www.youtube.com/watch?v=-xKKo7t72Tg&list=PLRBp0Fe2GpglkzuspoGv-mu7B2ce9_0Fn","NoCopyrightSounds")

	# Trap.telecharger("Trap 2013","Trap.png",2013)
	# House.telecharger("House 2013","House.png",2013)
	# Dubstep.telecharger("Dubstep 2013","Dubstep.png",2013)
	# DrumBass.telecharger("Drum&Bass 2013","Drum&Bass.png",2013)
	# Electronic.telecharger("Electronic 2013","Electronic.png",2013)
	# MelodicDubstep.telecharger("Melodic Dubstep 2013","Melodic Dubstep.png",2013)
	# IndieDance.telecharger("Indie Dance 2013","Indie Dance.png",2013)

	# Trap.telecharger("Trap 2014","Trap.png",2014)
	# House.telecharger("House 2014","House.png",2014)
	# Dubstep.telecharger("Dubstep 2014","Dubstep.png",2014)
	# DrumBass.telecharger("Drum&Bass 2014","Drum&Bass.png",2014)
	# Electronic.telecharger("Electronic 2014","Electronic.png",2014)
	# MelodicDubstep.telecharger("Melodic Dubstep 2014","Melodic Dubstep.png",2014)
	# IndieDance.telecharger("Indie Dance 2014","Indie Dance.png",2014)

	# Trap.telecharger("Trap 2015","Trap.png",2015)
	# House.telecharger("House 2015","House.png",2015)
	# Dubstep.telecharger("Dubstep 2015","Dubstep.png",2015)
	# DrumBass.telecharger("Drum&Bass 2015","Drum&Bass.png",2015)
	# Electronic.telecharger("Electronic 2015","Electronic.png",2015)
	# MelodicDubstep.telecharger("Melodic Dubstep 2015","Melodic Dubstep.png",2015)
	# IndieDance.telecharger("Indie Dance 2015","Indie Dance.png",2015)

	# Trap.telecharger("Trap 2016","Trap.png",2016)
	# House.telecharger("House 2016","House.png",2016)
	# Dubstep.telecharger("Dubstep 2016","Dubstep.png",2016)
	# DrumBass.telecharger("Drum&Bass 2016","Drum&Bass.png",2016)
	# Electronic.telecharger("Electronic 2016","Electronic.png",2016)
	# MelodicDubstep.telecharger("Melodic Dubstep 2016","Melodic Dubstep.png",2016)
	# IndieDance.telecharger("Indie Dance 2016","Indie Dance.png",2016)

	# Trap.telecharger("Trap 2017","Trap.png",2017)
	# House.telecharger("House 2017","House.png",2017)
	# Dubstep.telecharger("Dubstep 2017","Dubstep.png",2017)
	# DrumBass.telecharger("Drum&Bass 2017","Drum&Bass.png",2017)
	# Electronic.telecharger("Electronic 2017","Electronic.png",2017)
	# MelodicDubstep.telecharger("Melodic Dubstep 2017","Melodic Dubstep.png",2017)
	# IndieDance.telecharger("Indie Dance 2017","Indie Dance.png",2017)

##########
# GLOBAL #
##########

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		None