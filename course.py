# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:36:50 2016

@author: clifp
"""

class Course():
	def __init__(self, classString = "NOCLASS"):
		self.name
		self.units
		self.startTime
		self.endTime
		self.days
		self.viable = True
		
	def getName(self): 			return self.name
	def getUnits(self): 		return self.units
	def getStartTime(self): 	return self.startTime
	def getEndTime(self): 		return self.endTime
	def getDays(self): 			return self.days
	
	def setName(self, inName = "NONAME"):
		self.name = inName
		return
	
	#Input, string of HH:MM, uses class to get 
	def setStartTime(self, inTime = "00:00"):
		self.startTime = classTime(inTime)
		return
	def setEndTime(self, inTime):
		self.endTime = classTime(inTime = "00:00")
		return
	#Input: Char, or int of Units
	def setUnits(self, unitCount = "-1"):
		self.units = int(unitCount)
		return
	#Input: String of letters, to set (i.e. MWF)
	def setDays(self, inDays = "MTWRF"):
		self.days = inDays
		return
#End Course Class
#================================================
	
#Easy creation of time.	
class classTime():
	def __init__(self, stringTime = "00:00"):
		inTime = stringTime.split(':')
		self.hour = int(inTime[0])
		self.minute = int(inTime[1])
		return
	
#End Time Class
#================================================	
	
	
"""
Compares the two courses to see if they are overlapping
"""
def isCompatibleTime(courseA=None, courseB=None):
	answer = True
	if (courseA == None):
		print("NO FIRST COURSE")
		answer = False
	if (courseB == None):
		print ("NO SECOND COURSE")
		answer = False
	if (answer == False):
		return
		
	timeA = [courseA.getStartTime(), courseA.getEndTime]
	timeB = [courseB.getStartTime(), courseB.getEndTime]
		
	difference = 
