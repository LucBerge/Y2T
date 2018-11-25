# coding: utf8

################
# ENUMERATIONS #
################

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CR = '\033[F'

############
# DISPLAYS #
############

def log(text, CR=False):
	if(CR==True):
		print(bcolors.CR + bcolors.OKGREEN + "LOG : " + bcolors.ENDC + text)
	else:
		print(bcolors.OKGREEN + "LOG : " + bcolors.ENDC + text)

def warning(text):
	print(bcolors.WARNING + "WARNING : " + bcolors.ENDC + text)

def error(text):
	print(bcolors.FAIL + "ERROR : " + bcolors.ENDC + text)