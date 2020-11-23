class Circle:
	def __init__(self, radius = 1.0, color = "red"):
		self.radius = radius
		self.color = color
		
	def Circle(self):
		pass
		
	def Circle(self, radius):
		pass

	def Circle(self, radius, color):
		pass
		
	def getRadius(self):
		return self.radius
		
	def setRadius(self, radius):
		self.radius = radius
		
	def getColor(self):
		return self.color
		
	def setColor(self):
		self.color = color
	
	def toString(self):
		return "My radius is {} and my color is {}".format(self.radius, self.color)
		
	def getArea(self):
		return 3.14 * self.radius * self.radius
		

class Cylinder(Circle):
	def __init__(self, radius, color, height):
		super().__init__(radius, color)
		self.height = height
		
	def Cylinder(self):
		pass
		
	def Cylinder(self, height):
		pass

	def Cylinder(self, height, radius):
		pass
		
	def Cylinder(self, height, radius, color):
		pass
		
	def getHeight(self):
		return self.height
		
	def setHeight(self, height):
		self.height = height
		
	def toString(self):
		return "My radius is {}, my color is {}, and my height is {}".format(self.radius, self.color, self.height)
		
	def getVolume(self):
		return (self.height * (self.radius**2) * 3.14)