'''
Created on Oct 14, 2016

@author: ora0002
'''
def __init__(self,logFile = "log.txt"):
    if (logFile == None):
        raise ValueError("Fix.__init__: Hey! You didn't insert any file")
    if (not(isinstance(logFile, str))):
        raise ValueError("Fix.__init__: Hey! The parameter is not a string")
    if (len(logFile) < 1):
        raise ValueError("Fix.__init__: Hey! The length of the file is less than one")
    self.logFile = logFile
    self.sightfile = None
    self.writeinfilelog('Start of log\n')