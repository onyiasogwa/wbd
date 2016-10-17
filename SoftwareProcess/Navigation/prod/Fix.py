'''
Started creation on Oct 9, 2016

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
        self.sightfile = None
        self.writeinfilelog('Start of log\n')
        pass;


    def setSightingFile(self,sightingFile = None):
        if (sightingFile == None):
            raise ValueError("Fix.setSightingFile:  Hey! There is no file")
        if (not ( isinstance(sightingFile, str))):
            raise ValueError("Fix.setSightingFile:  Hey! The parameter is not a string")    
        filename, file_extension = os.path.splitext(sightingFile)
        if (len(filename)< 1 or file_extension != '.xml'):
            raise ValueError("Fix.setSightingFile:  Hey! The file name violates the parameter specification.")
        if (os.path.exists(sightingFile)):
            self.writeinfilelog("Start of sighting file " +  sightingFile + "\n")
        else:
            raise ValueError("Fix.setSightingFile:  Hey! The File does not exist.")
        self.sightfile = sightingFile
        return sightingFile

# ---------------------------------------------------------

# ---------------------------------------------------------
    def getSightings(self):
        if (self.sightfile == None):
            raise ValueError("Fix.getSightings:  Hey! The Sighting File dose Not setup yet.")
            
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
                        if (page.find('body') == None):
                            raise ValueError("Fix.getSightingsFile:  Hey! No body")
                        body = page.find('body').text
# --------------------------------------------------------------------------                        
                        if (page.find('date') == None):
                            raise ValueError("Fix.getSightingsFile:  Hey! No date")
                        da = page.find('date').text
                        d = da.split('-')[2]
                        mm = da.split('-')[1]
                        y = da.split('-')[0]
                        date1 = date(int(y),int(mm),int(d))
# --------------------------------------------------------------------------                        
                        if (page.find('time') == None):
                            raise ValueError("Fix.getSightingsFile:  Hey! No time")
                        t = page.find('time').text
                        h = t.split(':')[0]
                        m = t.split(':')[1]
                        s = t.split(':')[2]
                        time1 = time(int(h),int(m),int(s))
# --------------------------------------------------------------------------                        
                        if (page.find('observation') == None):
                            raise ValueError("Fix.getSightingsFile:  Hey! No observation")
                        al = page.find('observation').text
                        aa1  = int (al.split('d')[0]) 
                        aa2  = float(al.split('d')[1] )
                        if ( (aa2 + aa1) <= 0 ):
                            raise ValueError("Fix.getSightingsFile:  Hey! The altitude is Less than 0.1")
                        if ( aa1 < 0 or aa1 >= 90):
                            raise ValueError("Fix.getSightingsFile:  Hey! The degree portion of the altitude is out of range")
                        if ( aa2 < 0 or aa2 >= 60):
                            raise ValueError("Fix.getSightingsFile: Hey! The minute portion of the altitude is out of range")
                        observation =  str(aa1)+"d"+str(aa2)
# --------------------------------------------------------------------------                        
                        if (page.find('height') == None):
                            height = 0
                        else: 
                            height = page.find('height') .text
                        try :
                            x = float(height)
                            if (x < 0 ):
                                raise ValueError("Fix.getSightingsFile:  Hey! No temperature")
                        except ValueError:                        
                                raise ValueError("Fix.getSightingsFile:  Hey! No temperature")
                        height = float(height)
# --------------------------------------------------------------------------                        
                        if (page.find('temperature') == None):
                            temperature = -72
                        else:
                            temperature = page.find('temperature').text
                            
                        try:
                            x = int (temperature)
                            if (x < -20 or x > 120 ):
                                raise ValueError("Fix.getSightingsFile:  Hey! Temperature is out of the range")                        
                        except ValueError:
                                raise ValueError("Fix.getSightingsFile:  Hey! Temperature is not an Integer")
                        temperature = int(temperature)                        
# --------------------------------------------------------------------------                        
                        if (page.find('pressure') == None):
                            pressure = 1010
                        else:
                            pressure = page.find('pressure').text   
                                                    
                        try:
                            x= int(pressure)
                            if (x < 100 or x > 1100):
                                raise ValueError("Fix.getSightingsFile:  Hey! Pressure is out of the range")                        
                        except ValueError:
                                raise ValueError("Fix.getSightingsFile:  Hey! Pressure is not an Integer")                        
                        pressure = int(pressure)  
# --------------------------------------------------------------------------                        
                        if (page.find('horizon') == None):
                            horizon = "natural"
                        horizon = page.find('horizon').text                       
                        if (horizon.lower() != "natural" and horizon.lower() != "artificial"):
                            raise ValueError("Fix.getSightingsFile:  Hey! No horizon")                        
# --------------------------------------------------------------------------                        
                        try :
                            X = (body ,date1 , time1, observation, height, temperature, pressure, horizon)
                            sight.append(X)
                        except ValueError:
                            raise ValueError("Fix.getSightingsFile:  Hey! The file contains invalid information")
                else:
                    raise ValueError("Fix.getSightingsFile:  Hey! The file contains invalid information")
            else:
                    raise ValueError("Fix.getSightingsFile:  Hey! The file contains invalid information")
                    
        except ValueError:
            raise ValueError("Fix.getSightingsFile:  Hey! The file contains invalid information")

        ss = sight
        ss = sorted(ss,key=lambda x: (x[1],x[2],x[0]))
        self.write_sight(ss)
        self.writeinfilelog ("End of sighting file "+self.sightfile + "\n")

        return (approximateLatitude,approximateLongitude)
        
 
        
    def iscontain_valid(self, root= None):
        if (root == None):
            return False
        if ('fix' in root and 'sighting' in root):
            return True
        else:
            return False    
    
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
  
    def write_sight(self, sight):
        for x in sight:
            sightstring = str( x[0]) + "\t" + str( x[1].strftime('%Y-%m-%d') ) + "\t"  + str( x[2].strftime('%H:%M:%S')) + "\t"  + str( self.Calculate_altitud(x) + "\n") 
            self.writeinfilelog (sightstring )
    
    def Calculate_altitud(self,x):
        if (x[7].lower() == "natural"):
            dip = ( -0.97 * math.sqrt( x[4]) ) / 60            
        else:
            dip = 0
        z= x[3].split("d")
        alt = float(z[0]) + (float(z[1])/ 60)
        refraction = ( -0.00452 * float(x[6])) / ( 273 +  ((x[5] - 32) * (5/9) ) ) / math.tan( math.radians(alt) )            
        adjustedAltitude = alt + dip + refraction 
        a = int(adjustedAltitude -  adjustedAltitude%1) 
        b = "d"  
        c = round( (adjustedAltitude %1) *60 , 1 ) 
        if (len(str(c)) == 3):
            c = "0"+str(c)
        d = str(a)+b+str(c)
        return d


from datetime import tzinfo, timedelta, datetime
class TZ(tzinfo):
    def utcoffset(self, dt): 
        return timedelta(hours=-6)    