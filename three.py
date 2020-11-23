class Person:
	def __init__(self, name, address):
		self.name = name
		self.address = address
		
	def Person(name, address):
		pass
		
	def getName(self):
		return self.name
		
	def getAddress(self):
		return self.address

	def setAddress(address):
		self.address = address
		
	def toString(func):
		return "{}({})".format(self.name, self.address)
		

class Student(Person):
	def __init__(self, name, address, courses = {}, grades = {}, numCourses = 0):
		super().__init__(name, address)
		self.numCourses = numCourses
		self.courses = courses
		self.grades = grades
		
	def Student(name, address):
		pass
		
	def toString():
		return "Student: {}({})".format(name, address)
		
	def addCourseGrade(self, course, grade):
		pass
		
	def printGrades(self):
		print(self.grades)
		
	def getAverageGrade():
		return 100.0
		
	
	
		
class Teacher(Person):
	def __init__(self, name, address, courses = {}, numCourses = 0):
		super().__init__(name, address)
		self.numCourses = numCourses
		self.courses = courses
		self.grades = grades
		
	def Teacher(name, address):
		pass
		
	def toString():
		return "Teacher: {}({})".format(self.name, self.address)
		
	def addCourse(self, course):
		if course in self.courses:
			return True
		else:
			return False
		
	def removeCourse(self, course):
		if course in self.courses:
			return False
		else:
			return True
		
	def getAverageGrade():
		return 100.0
	
	
		
	