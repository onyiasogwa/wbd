'''
Started creation on Oct 25, 2016

@author: Rosemary
'''
import unittest
import os
import Navigation.prod.Fix as Fix

class Test(unittest.TestCase):
  
     

# --------------constructor-----------------------
# happy path
    def test100_010_ShouldConstructFix(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)
        
    def test100_020_ShouldConstructFix(self):
        self.assertIsInstance(Fix.Fix("hi"), Fix.Fix)
        
# sad path
    def test100_910_ShouldnotConstructFix(self):
        with self.assertRaises(ValueError):
            Fix.Fix(None)
    def test100_920_ShouldnotConstructFix(self):
        test_var = 0 ; 
        with self.assertRaises(ValueError):
            Fix.Fix(test_var)
    def test100_930_ShouldnotConstructFix(self):
        test_var = "" ; 
        with self.assertRaises(ValueError):
            Fix.Fix(test_var)
            
# -----------setSightingFile-------------------------
# happy path
    def test200_010_ReturnAbsoluteFilePath(self):
        F = Fix.Fix()
        s = os.path.abspath("hi.xml")
        s = s.replace( "\\","\\\\" )
        self.assertEqual(F.setSightingFile("hi.xml"),s)
# sad path
    def test200_910_NoFileExist(self):
        F = Fix.Fix()
        test_var = "bye.xml" ; 
        with self.assertRaises(ValueError):
            F.setSightingFile(test_var)
    def test200_920_PassIntegerAsFile(self):
        F = Fix.Fix()
        test_var = 1; 
        with self.assertRaises(ValueError):
            F.setSightingFile(test_var)
    def test200_930_PassNone(self):
        F = Fix.Fix()
        with self.assertRaises(ValueError):
            F.setSightingFile()
    def test200_940_passFilewithlengthlessthanone(self):
        F = Fix.Fix()
        test_var = ""; 
        with self.assertRaises(ValueError):
            F.setSightingFile(test_var)
    def test200_950_PassfileWithNoExtention(self):
        F = Fix.Fix()
        test_var = "hi"; 
        with self.assertRaises(ValueError):
            F.setSightingFile(test_var)
    def test200_960_PassfileWithdifferentExtention(self):
        F = Fix.Fix()
        test_var = "hi.txt"; 
        with self.assertRaises(ValueError):
            F.setSightingFile(test_var)
            
# -----------setAriesFile-------------------------
# happy path
    def test300_010_ReturnAbsoluteFilePath(self):
        F = Fix.Fix()
        s = os.path.abspath("aries.txt")
        s = s.replace( "\\","\\\\" )
        self.assertEqual(F.setAriesFile("aries.txt"),s)
    
# sad path
    def test300_910_NoFileExist(self):
        F = Fix.Fix()
        test_var = "bye.txt" ; 
        with self.assertRaises(ValueError):
            F.setAriesFile(test_var)
    def test300_920_PassIntegerAsFile(self):
        F = Fix.Fix()
        test_var = 1; 
        with self.assertRaises(ValueError):
            F.setAriesFile(test_var)
    def test300_930_PassNone(self):
        F = Fix.Fix()
        with self.assertRaises(ValueError):
            F.setAriesFile()
    def test300_940_passFilewithlengthlessthanone(self):
        F = Fix.Fix()
        test_var = ""; 
        with self.assertRaises(ValueError):
            F.setAriesFile(test_var)
    def test300_950_PassfileWithNoExtention(self):
        F = Fix.Fix()
        test_var = "hi"; 
        with self.assertRaises(ValueError):
            F.setAriesFile(test_var)
    def test300_960_PassfileWithdifferentExtention(self):
        F = Fix.Fix()
        test_var = "hi.txt"; 
        with self.assertRaises(ValueError):
            F.setAriesFile(test_var)
            
# -----------setStarFile-------------------------
# happy path
    def test400_010_ReturnAbsoluteFilePath(self):
        F = Fix.Fix()
        s = os.path.abspath("stars.txt")
        s = s.replace( "\\","\\\\" )
        self.assertEqual(F.setStarFile("stars.txt"),s)
# sad path
    def test400_910_NoFileExist(self):
        F = Fix.Fix()
        test_var = "bye.txt" ; 
        with self.assertRaises(ValueError):
            F.setStarFile(test_var)
    def test400_920_PassIntegerAsFile(self):
        F = Fix.Fix()
        test_var = 1; 
        with self.assertRaises(ValueError):
            F.setStarFile(test_var)
    def test400_930_PassNone(self):
        F = Fix.Fix()
        with self.assertRaises(ValueError):
            F.setStarFile()
    def test400_940_passFilewithlengthlessthanone(self):
        F = Fix.Fix()
        test_var = ""; 
        with self.assertRaises(ValueError):
            F.setStarFile(test_var)
    def test400_950_PassfileWithNoExtention(self):
        F = Fix.Fix()
        test_var = "hi"; 
        with self.assertRaises(ValueError):
            F.setStarFile(test_var)
    def test400_960_PassfileWithdifferentExtention(self):
        F = Fix.Fix()
        test_var = "hi.txt"; 
        with self.assertRaises(ValueError):
            F.setStarFile(test_var)
            
# ---------------------setSightingsFile-----------------------
# happy path
    def test500_010_correct(self):
        F = Fix.Fix()
        F.setSightingFile("hi.xml")
        self.assertEqual(F.getSightings(),('0d0.0','0d0.0'))

    def test500_020_Sortsamedate(self):
        F = Fix.Fix("samedatelog.txt")
        F.setSightingFile("sortsamedate.xml")
        self.assertEqual(F.getSightings(),('0d0.0','0d0.0'))

    def test500_030_Sortsamedateandtime(self):
        F = Fix.Fix("samedateandtimelog.txt")
        F.setSightingFile("sortsamedateandtime.xml")
        self.assertEqual(F.getSightings(),('0d0.0','0d0.0'))



# sad path
    def test500_910_notsetupsetsighting(self):
        F = Fix.Fix()
        with self.assertRaises(ValueError):
            F.getSightings()
            
    def test500_920_altitudeLessThanrange(self):
        F = Fix.Fix()
        F.setSightingFile("altitudelessthan1.xml")
        with self.assertRaises(ValueError):
            F.getSightings()

    def test500_930_missbody(self):
        F = Fix.Fix()
        F.setSightingFile("missBody.xml")
        with self.assertRaises(ValueError):
            F.getSightings()
         
    def test500_940_missdate(self):
        F = Fix.Fix()
        F.setSightingFile("missDate.xml")
        with self.assertRaises(ValueError):
            F.getSightings()         

    def test300_950_misstime(self):
        F = Fix.Fix()
        F.setSightingFile("missTime.xml")
        with self.assertRaises(ValueError):
            F.getSightings()           
    
    def test500_960_missObservation(self):
        F = Fix.Fix()
        F.setSightingFile("missobservation.xml")
        with self.assertRaises(ValueError):
            F.getSightings()

    def test500_970_Observationhavedegreemorethan90(self):
        F = Fix.Fix()
        F.setSightingFile("obgreatthan90.xml")
        with self.assertRaises(ValueError):
            F.getSightings()        


    def test500_980_Observationhavedegreelessthan0(self):
        F = Fix.Fix()
        F.setSightingFile("oblessthan0ford.xml")
        with self.assertRaises(ValueError):
            F.getSightings()   
            

    def test500_990_Observationhaveminutelessthan0(self):
        F = Fix.Fix()
        F.setSightingFile("oblessthan0form.xml")
        with self.assertRaises(ValueError):
            F.getSightings()    
            
    def test500_991_Observationhaveminutegreatthan60(self):
        F = Fix.Fix()
        F.setSightingFile("obgreatthan60.xml")
        with self.assertRaises(ValueError):
            F.getSightings()      
            
    def test500_992_HeightLessthan0(self):
        F = Fix.Fix()
        F.setSightingFile("heightlessthan0.xml")
        with self.assertRaises(ValueError):
            F.getSightings()      
            
    def test500_993_TemperatureMoreThan120(self):
        F = Fix.Fix()
        F.setSightingFile("tempmprethan120.xml")
        with self.assertRaises(ValueError):
            F.getSightings() 
            
    def test500_994_TemperatureLessthan_20(self):
        F = Fix.Fix()
        F.setSightingFile("templessthan-20.xml")
        with self.assertRaises(ValueError):
            F.getSightings()    
            
            
    def test500_995_PressureLessthan100(self):
        F = Fix.Fix()
        F.setSightingFile("preslessthan100.xml")
        with self.assertRaises(ValueError):
            F.getSightings()        
            
    def test500_995_Pressuremorethan1100(self):
        F = Fix.Fix()
        F.setSightingFile("presmorethan1100.xml")
        with self.assertRaises(ValueError):
            F.getSightings()   
            
    def test500_996_HorizonwithdifferentName(self):
        F = Fix.Fix()
        F.setSightingFile("horisdifferentname.xml")
        with self.assertRaises(ValueError):
            F.getSightings()   