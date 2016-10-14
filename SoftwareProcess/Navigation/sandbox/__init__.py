import Navigation.prod.Angle as Angle

angle1 = Angle.Angle()
angle2 = Angle.Angle()
angle3 = Angle.Angle()
angle4 = Angle.Angle()

#say:
angle1Degrees = angle1.setDegreesAndMinutes("46d0.0")   
print('angle1Degrees : ' , angle1Degrees)

#say:
angle2Degrees = angle2.setDegrees(degrees=-156.5)        
print("angle2Degrees : " , angle2Degrees)

try:
    invalidAngle = angle2.setDegreesAndMinutes("none")
    #"none" seems to be the same as "" or "0"

except ValueError as raisedException:
    diagnosticString = raisedException.args[0]
    print (diagnosticString)
    
#The exception should be raised!
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
angle1String = angle1.getString()   #angle1String should be "45d0.0"
print ("angle1String : ", angle1String)