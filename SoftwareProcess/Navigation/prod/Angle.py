'''
Started creation on Sep 2, 2016

@author: Rosemary

'''
class Angle():
    
    def __init__(self):
        self.minutes = 0 ; 
        self.degrees = 0 ;  
        pass;
#   ----------------------------------------------------- 
    def setDegrees (self, degrees=0):
        try:
            int (degrees)
            self.degrees = int (degrees % 360)
            self.minutes =  degrees % 1
            return self.degrees + self.minutes
        except ValueError:
            raise ValueError("Angle.setDegrees: Hey! Degree is not a number.")
#   ----------------------------------------------------- 
    def setDegreesAndMinutes(self,angleString=None):
        # check None or not
        if (angleString == None):
            raise ValueError("Angle.setDegreesAndMinutes: Hey! It's Empty.")
        # check how much d have
        if (not (isinstance( angleString , basestring ) )):
            raise ValueError("Angle.setDegreesAndMinutes: Hey! It's not a String.")
        if (angleString.count('d') != 1):
            raise ValueError("Angle.setDegreesAndMinutes: Hey! The Formula is not true.")
        angleString = angleString.split('d')
        # check if the first part is integer
        try:
            angleString[0] = int(angleString[0])
        except ValueError :
            raise ValueError("Angle.setDegreesAndMinutes: Hey! The degree is not an integer.")
        # check if the second part is float
        try:
            if (angleString[1].count('.') == 1):
                checknumberofdecimal = angleString[1].split('.') 
                if (int (checknumberofdecimal[1]) > 9 ):
                    raise ValueError("Angle.setDegreesAndMinutes: Hey! Minutes must have only one decimal place.")
                angleString[1] = float(angleString[1])
            else:
                angleString[1] = int(angleString[1])
        except ValueError :
            raise ValueError("Angle.setDegreesAndMinutes: Hey! The minutes is not Number.")
        # check if the second part is not negative
        if (angleString[1] < 0):
            raise ValueError("Angle.setDegreesAndMinutes: Hey! The minutes is Negative.")
        
        
        convert_string = angleString[0] + (angleString[1] / 60)
         
        self.degrees = int (convert_string % 360)
        self.minutes = round (convert_string % 1,1) 
        
        return convert_string
#   ----------------------------------------------------- 
    def add(self,angle = None):
        if (angle == None):
            raise ValueError("Angle.add: Hey! The angle is Empty.")
         
        if (not(isinstance(angle,Angle))):
            raise ValueError ("Angle.add:Hey! That is not a Type of Angle Class")
#    ------------------------------------------------------------------
        total_degree = self.degrees + angle.degrees + self.minutes + angle.minutes
        
        self.degrees = int (total_degree % 360)
        self.minutes = round ( total_degree % 1, 1 )  
        
        return self.degrees + self.minutes
#   ----------------------------------------------------- 
    def subtract(self,angle = None):
        if (angle == None):
            raise ValueError("Angle.subtract: Hey! The angle is Empty.")
         
        if (not(isinstance(angle,Angle))):
            raise ValueError ("Angle.subtract:Hey! That is not Type of Angle Class")
#    ------------------------------------------------------------------
        total_degree = (self.degrees + self.minutes) - (angle.degrees  + angle.minutes) 
        
        self.degrees = int (total_degree % 360)
        self.minutes = round ( total_degree % 1, 1 )  
        
        return self.degrees + self.minutes
#   ----------------------------------------------------- 
    def compare(self, angle = None):
        if (angle == None):
            raise ValueError("Angle.compare: Hey! The angle is Empty.")
        if (not(isinstance(angle,Angle))):
            raise ValueError ("Angle.compare:Hey! That is not a Type of Angle Class")
        if (self.degrees == angle.degrees and self.minutes == angle.minutes ):
                return 0 
        currentangle = self.degrees + self.minutes
        parameterangle = angle.degrees + angle.minutes 
        if (currentangle > parameterangle):
            return 1
        else:
            return -1
#   ----------------------------------------------------- 
    def getString(self):
        String_Angle = str(int(self.degrees))+"d" + str(round ((self.minutes * 60), 1 ))  
        return String_Angle
#   ----------------------------------------------------- 
    def getDegrees(self):
        return round (self.degrees + self.minutes , 1 ) 
        
                                            
