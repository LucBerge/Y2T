# coding: utf8

#########
# CLASS #
#########

class Collection:

	############
	# ATRIBUTS #
	############

	artist = None

	duration = 0
	weight = 0
	files = []

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, artist):
		self.artiste = artist

	###########
	# METHODS #
	###########

	def add(self, file):
		self.duration += file.duration
		self.weight += file.weight
		self.files.append(file)
	
	def __str__(self):
		result = ""
		for file in self.files:
			result += str(file) + "\n"
		return result