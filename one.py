class myObject:
	def __init__(self):
		pass
		
class X(myObject):
	def __init__(self):
		pass
		
class Y(myObject):
	def __init__(self):
		pass
		
class Z(myObject):
	def __init__(self):
		pass
		
class A(X, Y):
	def __init__(self):
		pass
		
class B(Y, Z):
	def __init__(self):
		pass
		
class M(A, B, Z):
	def __init__(self):
		pass