# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:36:50 2016

@author: clifp
"""

class Course():
	def __init__(self):
		self.name
		self.units
		self.startTime
		self.endTime
		self.days
		
	def getName(self): 			return self.name
	def getUnits(self): 		return self.units
	def getStartTime(self): 	return self.startTime
	def getEndTime(self): 		return self.endTime
	def getDays(self): 			return self.days
	
	#Input, string of HH:MM
	def setStartTime(self, inTime):
		self.startTime = classTime(inTime)
		return
	
#Easy creation of time.	
class classTime():
	def __init__(self, stringTime = "00:00"):
		inTime = stringTime.split(':')
		self.hour = int(inTime[0])
		self.minute = int(inTime[1])
		return
	
#End Course Class
#================================================