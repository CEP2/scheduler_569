# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:36:50 2016

@author: clifp
"""

class Course(object):
	def __init__(self, classString = "NOCLASSINIT"):
		self.name 			= "NONAME"
		self.units 			= -1
		self.startTime 	= "00:00"
		self.endTime 		= "00:00"
		self.days 			= "MTWRF"
		self.viable 		= True
		self.parseClass(classString)
		
	def getName(self): 			return self.name
	def getUnits(self): 		return self.units
	def getStartTime(self): 	return self.startTime
	def getEndTime(self): 		return self.endTime
	def getDays(self): 			return self.days
	def isViable(self):		return self.viable
	
	
	
	
	def setName(self, inName = "NONAME"):
		self.name = inName
		return	
	#Input, string of HH:MM, uses class to get 
	def setStartTime(self, inTime = "00:00"):
		self.startTime = classTime(inTime)
		return
	def setEndTime(self, inTime="00:00"):
		self.endTime = classTime(inTime)
		return
	#Input: Char, or int of Units
	def setUnits(self, unitCount = "-1"):
		self.units = int(unitCount)
		return
	#Input: String of letters, to set (i.e. MWF)
	def setDays(self, inDays = "MTWRF"):
		self.days = inDays
		return
	def setViable(self, boolIn):
		self.viable = boolIn
		return
		
		
	#Expected Format: Name Units Days Start End	
	def parseClass(self, classString = "NOCLASSPARSE"):
		classLine = classString.split()		#Separate by whitespace
		self.setName(classLine[0])
		self.setUnits(classLine[1])
		self.setDays(classLine[2])
		self.setStartTime(classLine[3])
		self.setEndTime(classLine[4])
		return
		
	def printCourse(self):
		print(self.name,end='\t')
		print(str(self.units),end='\t')
		print(self.days,end='\t')
		self.startTime.printClassTime()
		self.endTime.printClassTime()
		print()
		
		
		
#End Course Class
#================================================
	
#Easy creation of time.	
class classTime(object):
	def __init__(self, stringTime = "00:00"):
		inTime = stringTime.split(':')
		self.hour = int(inTime[0])
		self.minute = int(inTime[1])
		return
	
	def getHour(self): return self.hour
	def getMinute(self): return self.minute
		
	def printClassTime(self):
		if (self.hour < 10):
			strHour = "0"+str(self.hour)
		else:
			strHour = str(self.hour)
		if (self.minute < 10):
			strMinute = "0"+str(self.minute)
		else:
			strMinute = str(self.minute)
		print("{}:{}".format(strHour, strMinute), end='\t')
#End Time Class
#================================================	

def isCompatibleCourse(courseA=None, courseB=None):
	if (isCompatibleDay(courseA, courseB) == False):
		if (isCompatibleTime(courseA,courseB) == False):
			return False
	return True
#End isCompatibleCourse
#================================================

def isCompatibleDay(courseA=None, courseB=None):
	answer = True
	#Check for present classes
	if (courseA == None):
		print("NO FIRST COURSE")
		answer = False
	if (courseB == None):
		print ("NO SECOND COURSE")
		answer = False
	if (answer == False):
		return answer
		
	daysA = courseA.getDays()
	daysB = courseB.getDays()
	
	for day in daysA:
		if (day in daysB):
			return False
	return True

#End isCompatibleDay
#================================================	
	
"""
Compares the two courses to see if they are overlapping
False = overlapping
True = compatible
"""
def isCompatibleTime(courseA=None, courseB=None):
	answer = True
	#Check for present classes
	if (courseA == None):
		print("NO FIRST COURSE")
		answer = False
	if (courseB == None):
		print ("NO SECOND COURSE")
		answer = False
	if (answer == False):
		return			
			
	#Pull times into organized array.	
	timeA = [courseA.getStartTime(), courseA.getEndTime]	#Course 1
	timeB = [courseB.getStartTime(), courseB.getEndTime]	#Course 2
	
	#Avoid assumption that course A starts earlier.
	#Swap B/A if Hour is earlier, if equal check minute
	startHourDiff = timeB[0].getHour() - timeA[0].getHour()
	if ( startHourDiff < 0):
		#Perform a swap if class B starts earlier based on Hour.
		temp = timeA
		timeA = timeB
		timeB = temp
	#If the hour is equal, check for minutes being less. 
	elif ( (timeB[0].getHour() - timeA[0].getHour()) == 0):
		startMinDiff = timeB[0].getMinute() - timeA[0].getMinute()
		#If both values are 0, then they are the same start time.
		if (startMinDiff == 0):
			return False
		#If they don't start at the same time, swap minutes.
		if (startMinDiff < 0):
			temp = timeA
			timeA = timeB
			timeB = temp
	#Don't swap otherwise.
	
	#Compare startA / endA vs startA/startB
	hourDuration = timeA[0].getHour() - timeA[1].getHour()	 #Duration of classA
	hourNext = timeB[0].getHour() - timeA[0].getHour() #Duration between start of Class A/B
	#If the next class is sooner in hours than the end of the course...
	if (hourNext > hourDuration):
		return True
	#If the classes start in the same hour...
	elif (hourNext == hourDuration):
		#Check minute comparison.
		minDuration = timeA[0].getMinute() - timeA[1].getMinute()
		minNext = timeB[0].getMinute() - timeA[0].getMinute()
		#If next class is later than the end time of the first class...
		if (minNext > minDuration):
			return True
		else:
			return False
	#Catch for decision not being made. 
	else: 
		print ("function:\tisCompatibleTime reached end of decision tree.")
		return False
#END isCompatibleTime
#=================================================================
		
	
		
	
