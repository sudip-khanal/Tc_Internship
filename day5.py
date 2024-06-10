
# context manager

class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()

# loading a file 
with FileManager('test1.txt', 'w') as f:
	f.write('Hello!!!!')


class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()

# loading a file 
with FileManager('test2.txt', 'r+') as f:
	f.write('This is test file 2 with read and wright permission')




#threading

import threading

def print_cube(num):
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done!")

# Meta class
# A metaclass is a class that allows for 
# other classes to be instantiated as objects of the metaclass.

# Metaclasses allow for code not only to manipulate data, but to manipulate classes.
# Often this change happens when an object of the class is instantiated. 
# Using metaclasses also helps to abstract our code, making it more readable 
# and helping to reduce the amount of code written by avoiding repetition in code.

class ExampleMetaClass(type):
	# def __init__(self,name,gender ):
	# 	self.name=name
	# 	self.gender=gender
	pass

class SubClass(metaclass=ExampleMetaClass):
    pass
 

subclass_object = SubClass()

print(f"subclass_object's class is {subclass_object.__class__}/n")
print(f"SubClass's class is {subclass_object.__class__.__class__}/n")
print(f"ExampleMetaClass's class is {subclass_object.__class__.__class__.__class__}")

print(dir())
