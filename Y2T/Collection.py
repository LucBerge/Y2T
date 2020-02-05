# coding: utf8

#########
# CLASS #
#########

class Collection:

	###############
	# CONSTRUCTOR #
	###############

	def __init__(self, artist):
		self.artist = artist
		self.duration = 0
		self.weight = 0
		self.files = []

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