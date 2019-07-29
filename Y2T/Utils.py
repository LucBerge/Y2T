# coding: utf8

###########
# IMPORTS #
###########

import time

#########
# CLASS #
#########

def bytesToMeagebytes(bytes):
	return round(bytes/1048576, 2)

def secondsToHHMMSS(seconds):
	if(seconds < 3600):
		return time.strftime('%M:%S', time.gmtime(seconds))
	else:
		return time.strftime('%H:%M:%S', time.gmtime(seconds))