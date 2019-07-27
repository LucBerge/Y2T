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

class Log(object):
    def debug(self, msg, CR=False):
        if(CR==True):
            print(bcolors.CR + "[Y2T] " + msg)
        else:
            print("[Y2T] " + msg)

    def warning(self, msg):
        print(bcolors.WARNING + "WARNING : " + bcolors.ENDC + msg)

    def error(self, msg):
        print(bcolors.FAIL + "ERROR : " + bcolors.ENDC + msg)

logger = Log()