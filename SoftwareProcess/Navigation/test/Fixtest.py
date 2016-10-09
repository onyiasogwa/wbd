'''
Created on Oct 9, 2016

@author: owners
'''
import Navigation.prod.Fix as Fix


theFix = Fix.Fix()     
theFix.setSightingFile("sightings.xml")        
approximatePosition = theFix.getSightings()        
