# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:33:08 2016

Final project intended to be able to schedule courses for students given a list of classes.
Initial prioritization is by listing order.

@author: clifp
"""

#from courseClass import*
from courseClass import*
import sys

BARRIER_TEXT = "===================="
"""
Opens file for reading.

"""
def readClasses(filename="classes.txt"):
	file = open(filename, "r")
	courseList = list()
	for courseLine in file:
		courseLine = (courseLine.upper())	
		courseList.append(courseLine)
	return courseList
	
def printCourseList(courseList=None):
	if (courseList==None):
		print("No course list to print.")
		return
	for listing in courseList:
		listing.printCourse()
	
def countViable(courseList=None):
	if courseList == None:
		print ("countViable:\t No list present.")
		return -1
	count = 0
	for listing in courseList:
		if (listing.isViable()):
			count+=1
	return count

def sumCourseUnits(acceptedList=None):
	if (acceptedList==None):
		print("sumCourseUnits:\tNo list available.")
		return
	sumUnits = 0
	for listing in acceptedList:
		sumUnits += listing.getUnits()
	return sumUnits

"""
	Input
		Current Course List
	Output
		Index of next viable course.
"""
def findNextViableCourse(courseList=None):
	if(courseList==None):
		print("findNextViableCourse():\t Course List is missing.")
		return
	#Sort through list to find first viable course
	index = 0
	listLen = len(courseList)
	while index < listLen:
		if (courseList[index].isViable()):
			return index
		index += 1 
	return -1

"""
Input
	Accepted Course List (State)
	Full Course List (Entire List)
	OPTIONAL courseIndex - location to start on courseList.
Objective
	Take the course at the front of the list (if viable)
	Compare it to the accepted list.
		If it fits, add to accepted AND mark all remaining as viable/not
"""
def considerCourse(courseList=None, acceptedList=None, courseIndex=None):
	if (courseList == None or acceptedList == None):
		print("considerCourse():\tCourse or Accepted List is missing.")
		return
	if (len(acceptedList) == 0):
		index = 0
	else:
		index = findNextViableCourse(courseList)
	
	#Accept first found 
	acceptedCourse = courseList[index]
	acceptedCourse.setViable(False)	
	acceptedList.append(acceptedCourse)	
	
	for listing in courseList[index+1:]:
		courseBool = (listing.getName(), listing.isViable()) #DEBUG - VISIBILITY
		if (listing.isViable() == False):
			continue
		listing.setViable(isCompatibleCourse(acceptedCourse, listing))
		courseBool = (listing.getName(), listing.isViable())
	return

def findCourses(courseList=None, acceptedList=None):
	if (courseList == None or acceptedList == None):
		print("findCourses():\tCourse or Accepted List is missing.")
		return
	viableCount = countViable(courseList)
	while viableCount > 0: 
		considerCourse(courseList, acceptedList)
		viableCount = countViable(courseList)
	
	return

		
		
def main():
	if len(sys.argv)	== 2:
		classesTextList = readClasses(sys.argv[1])	
	else:
		classesTextList = readClasses()
	#print(classesTextList)
	
	courseList = list()		 	#General Course list
	acceptedList = list()		#Accepted courses
	#Add all courses to standard list in structure.
	for course in classesTextList:
		newCourse = Course(course)
		courseList.append(newCourse)
		
	print("\nCourse List\n" + BARRIER_TEXT)
	printCourseList(courseList)
	print(BARRIER_TEXT)
		
	#Begin considering courses.
	findCourses(courseList, acceptedList)
	
	print("\nACCEPTED COURSES\n" + BARRIER_TEXT)
	print("Total Units:\t{}".format(sumCourseUnits(acceptedList)))
	printCourseList(acceptedList)
	print(BARRIER_TEXT)	
	#TEST COMPARISONS
	#if ( isCompatibleCourse (courseList[1], courseList[3]) ):
		#print("CLEAR")

		
	
	
	
	
	
	return
	
	
main()
