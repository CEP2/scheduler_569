# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:33:08 2016

Final project intended to be able to schedule courses for students given a list of classes.
Initial prioritization is by listing order.

@author: clifp
"""

#from courseClass import*
from courseClass import*

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
	return count

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
		if (courseList[index].isViable)
		index += 1 
		
		
	
	return -1

"""
Input
	Accepted Course List (State)
	Full Course List (Entire List)
Objective
	Take the course at the front of the list (if viable)
	Compare it to the accepted list.
		If it fits, add to accepted AND mark all remaining as viable/not
"""
def considerCourse(courseList=None, acceptedList=None):
	if (courseList == None or acceptedList == None):
		print("considerCourse():\tCourse or Accepted List is missing.")
		return
	
	return
	
	
	

def main():
	classesTextList = readClasses()
	print(classesTextList)
	
	courseList = list()		 	#General Course list
	acceptedList = list()		#Accepted courses
	#Add all courses to standard list in structure.
	for course in classesTextList:
		newCourse = Course(course)
		courseList.append(newCourse)
		
	
	#Begin considering courses.
	
		
	#TEST COMPARISONS
	if ( isCompatibleCourse (courseList[1], courseList[3]) ):
		print("CLEAR")
	print("\nCourse List\n" + BARRIER_TEXT)
	printCourseList(courseList)
	print(BARRIER_TEXT)
		
	
	
	
	
	
	return
	
	
main()
