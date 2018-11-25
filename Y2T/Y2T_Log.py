#!/usr/bin/python
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

#############
# AFFICHAGE #
#############

def log(texte, CR=False):
	if(CR==True):
		print(bcolors.CR + bcolors.OKGREEN + "LOG : " + bcolors.ENDC + texte)
	else:
		print(bcolors.OKGREEN + "LOG : " + bcolors.ENDC + texte)

def warning(texte):
	print(bcolors.WARNING + "ATTENTION : " + bcolors.ENDC + texte)

def error(texte):
	print(bcolors.FAIL + "ERREUR : " + bcolors.ENDC + texte)