'''
Started creation on Oct 25, 2016

@author: Rosemary
'''
import os
from xml.etree import cElementTree as ET
from datetime import  date, time
import math

class Fix():

 
    def __init__(self,logFile = "log.txt"):
        if (logFile == None):
            raise ValueError("Fix.__init__:  Hey! You did not insert any File")
        if (not ( isinstance(logFile, str))):
            raise ValueError("Fix.__init__:  Hey! The parameter is not a string")
        if (len(logFile) < 1):
            raise ValueError("Fix.__init__:  Hey! The Length of file is less than one.")
        
        self.logFile = logFile
        s  = os.path.abspath(self.logFile)
        s = s.replace( "\\","\\\\" ) 
        self.sightfile = None
        self.writeinfilelog('Log file:\t'+s)
        pass;

    def writeinfilelog (self, s):
        try:
            t = datetime.now()
            correctformula = datetime(t.year, t.month, t.day, t.hour, t.minute , t.second ,  tzinfo=TZ()).isoformat(' ')
             
            totalstring = "LOG: "+correctformula+"\t"+s
            f = open(self.logFile, 'a')
            f.write(totalstring)
        except ValueError:
            raise ValueError("Fix.__init__:  Hey! The file name violates the parameter specification.")
        pass
    
#-------------------------------------------------
    def setSightingFile(self,sightingFile = None):
        if (sightingFile == None):
            raise ValueError("Fix.setSightingFile: Hey! There is no file")
        if (not ( isinstance(sightingFile, str))):
            raise ValueError("Fix.setSightingFile: Hey! The parameter is not string")   
        filename, file_extension = os.path.splitext(sightingFile)
        if (len(filename)< 1 or file_extension != '.xml'):
            raise ValueError("Fix.setSightingFile: Hey! The file name violates the parameter specification.")
        if (os.path.exists(sightingFile)):
            s  = os.path.abspath(sightingFile )
            s = s.replace( "\\","\\\\" ) 
            self.writeinfilelog("Sighting file: \t" +s)
        else:
            raise ValueError("Fix.setSightingFile: Hey! The File does not exist.")
        self.sightfile = s
        return self.sightfile
#-----------------------------------------------------

    def setAriesFile(self,ariesFile = None):
        if (ariesFile == None):
            raise ValueError("Fix.setAriesFile: Hey! There is no file")
        if (not ( isinstance(ariesFile, str))):
            raise ValueError("Fix.setAriesFile: Hey! The parameter is not string")   
        filename, file_extension = os.path.splitext(ariesFile)
        if (len(filename)< 1 or file_extension != '.txt'):
            raise ValueError("Fix.setAriesFile: Hey! The file name violates the parameter specification.")
        if (os.path.exists(ariesFile)):
            s  = os.path.abspath(ariesFile )
            s = s.replace( "\\","\\\\" ) 
            self.writeinfilelog("Aries file: \t" +s)
        else:
            raise ValueError("Fix.setAriesFile: Hey! The File does not exist.")
        self.ariesfile = s
        return self.ariesfile
#----------------------------------------------------

    def setStarFile(self,starFile = None):
        if (starFile == None):
            raise ValueError("Fix.setStarFile: Hey! There is no file")
        if (not ( isinstance(starFile, str))):
            raise ValueError("Fix.setStarFile: Hey! The parameter is not string")   
        filename, file_extension = os.path.splitext(starFile)
        if (len(filename)< 1 or file_extension != '.txt'):
            raise ValueError("Fix.setStarFile: Hey! The file name violates the parameter specification.")
        if (os.path.exists(starFile)):
            s  = os.path.abspath(starFile )
            s = s.replace( "\\","\\\\" ) 
            self.writeinfilelog("Star file: \t" +s)
        else:
            raise ValueError("Fix.setStarFile: Hey! The File does not exist.")
        self.starfile = s
        return self.starfile
    
# ---------------------------------------------------------
    def getSightings(self):
        if ((self.sightfile == None) or (self.ariesfile == None) or (self.starfile == None)):
            raise ValueError("Fix.getSightings: Hey! The Sighting/aries/star file has not been setup yet.")
           
        approximateLatitude = "0d0.0"           
        approximateLongitude = "0d0.0" 
        with open (self.sightfile, "r") as myfile:
            xmlstr=myfile.read()
        
        try:
            if (self.iscontain_valid(xmlstr)):
                root = ET.fromstring(xmlstr)
                if (root.tag == 'fix'):
                    sight = []
                    for page in root:
                       
# --------------------------------------------------------------------------                       
                        if (page.find('body') == None or page.find('body').text == None):
                            raise ValueError("Fix.getSightings: Hey! No body")
                        body = page.find('body').text
# --------------------------------------------------------------------------                       
                        if (page.find('date') == None):
                            raise ValueError("Fix.getSightings: Hey! No date")
                        da = page.find('date').text
                        d = da.split('-')[2]
                        mm = da.split('-')[1]
                        y = da.split('-')[0]
                        date1 = date(int(y),int(mm),int(d))
# --------------------------------------------------------------------------                       
                        if (page.find('time') == None):
                            raise ValueError("Fix.getSightings: Hey! No time")
                        t = page.find('time').text
                        if (":" not in t ):
                            raise ValueError("Fix.getSightings:Hey! The format for time is not correct")
                        h = t.split(':')[0]
                        m = t.split(':')[1]
                        s = t.split(':')[2]
                        time1 = time(int(h),int(m),int(s))
# --------------------------------------------------------------------------                       
                        if (page.find('observation') == None):
                            raise ValueError("Fix.getSightings: Hey! No observation")
                        al = page.find('observation').text
                        if ("d" not in al ):
                            raise ValueError("Fix.getSightings: Hey! The format for observation is not correct")
                        aa1  = int (al.split('d')[0])
                        aa2  = float(al.split('d')[1] )
                        if ( (aa2 + aa1) <= 0 ):
                            raise ValueError("Fix.getSightings: Hey! The altitude Less than 0.1")
                        if ( aa1 < 0 or aa1 >= 90):
                            raise ValueError("Fix.getSightings: Hey! degree portion of the altitude out of range")
                        if ( aa2 < 0 or aa2 >= 60):
                            raise ValueError("Fix.getSightings: Hey! The minute portion of the altitude")
                        observation =  str(aa1)+"d"+str(aa2)
# --------------------------------------------------------------------------                        
                        if (page.find('height') == None):
                            height = 0
                        else:
                            height = page.find('height') .text
                        try :
                            x = float(height)
                            if (x < 0 ):
                                raise ValueError("Fix.getSightings: Hey! No temperature")
                        except ValueError:                       
                                raise ValueError("Fix.getSightings: Hey! No temperature")
                        height = float(height)
# --------------------------------------------------------------------------                       
                        if (page.find('temperature') == None):
                            temperature = 72
                        else:
                            temperature = page.find('temperature').text
                        try:
                            x = int (temperature)
                            if (x < -20 or x > 120 ):
                                raise ValueError("Fix.getSightings: Hey! Temperature is out of the range")                       
                        except ValueError:
                                raise ValueError("Fix.getSightings: Hey! Temperature is not Integer")
                        temperature = int(temperature)                       
# --------------------------------------------------------------------------                       
                        if (page.find('pressure') == None):
                            pressure = 1010
                        else:
                            pressure = page.find('pressure').text  
                        try:
                            x= int(pressure)
                            if (x < 100 or x > 1100):
                                raise ValueError("Fix.getSightings: Hey! Pressure is out of the range")                       
                        except ValueError:
                                raise ValueError("Fix.getSightings: Hey! Pressure is not Integer")                       
                        pressure = int(pressure) 
# --------------------------------------------------------------------------                       
                        if (page.find('horizon') == None):
                            horizon = "natural"
                        else:
                            horizon = page.find('horizon').text                      
                        if (horizon.lower() != "natural" and horizon.lower() != "artificial"):
                            raise ValueError("Fix.getSightings: Hey! No horizon")                       
# --------------------------------------------------------------------------                        
                        try :
                            X = (body ,date1 , time1, observation, height, temperature, pressure, horizon)
                            sight.append(X)
                        except ValueError:
                            raise ValueError("Fix.getSightings:: Hey! The file contains invalid information")
                else:
                    raise ValueError("Fix.getSightings:: Hey! The file contains invalid information")
            else:
                    raise ValueError("Fix.getSightings:: Hey! The file contains invalid information")
                   
        except ValueError:
            raise ValueError("Fix.getSightings: Hey! The file contains invalid information")
 
        ss = sight
        ss = sorted(ss,key=lambda x: (x[1],x[2],x[0]))
        self.write_sight(ss)
        self.wirteinfilelog ("End of sighting file "+self.sightfile + "\n")
 
        return (approximateLatitude,approximateLongitude)
    
from datetime import tzinfo, timedelta, datetime
class TZ(tzinfo):
    def utcoffset(self, dt): 
        return timedelta(hours=-6)   