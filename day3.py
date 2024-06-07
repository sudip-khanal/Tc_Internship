#class method
class Student:
    grade = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return {"Name": self.name, "Age": self.age, "Grade": self.grade}

    @classmethod
    def update_grade(cls, grade):
        cls.grade = grade

# Example usage
student1 = Student("sudip", 10)
student2 = Student("samir", 12)
# student2.grade=9
print(student1.get_data())  
print(student2.get_data())  

Student.update_grade(6)

print(student1.get_data()) 
print(student2.get_data()) 

#static method

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

print(MathOperations.add(5, 3))        
print(MathOperations.subtract(10, 4))  


# amother example

from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	@staticmethod
	def isAdult(age):
		return age >= 18

person1 = Person('sudip', 23)
person2 = Person.fromBirthYear('amit', 2000)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(18))


#decoraters
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout) 
greet(whisper) 

#another example

def decorators_example(func):
    def greeting():
        print("Good Morning")
        func()
        print("Good Afternoon")
    return greeting

@decorators_example
def hello():
    print("Hello........")

hello()

# list Comprehensions


list_using_comp = [var**2 for var in range(1, 10)]

print( list_using_comp)


# Dictionary Comprehensions
input_list = [1,2,3,4,5,6,7]

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print(dict_using_comp)


# Set Comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print(set_using_comp)

# lambda function
x = lambda a, b : a * b
print(x(5, 6))


list1=[20,3,90,44,54,32,43,65,44,55,70,90]

even=list(filter(lambda x:x%2==0,list1))
print(even)


from abc import ABC,abstractmethod

class Machine(ABC):
      @abstractmethod
      def processing():
            pass

class Computer(Machine):
    def processing(self):
            print('Running')  

    def programmer(self):
          print('solve problem')

c1= Computer()
c1.processing()
c1.programmer()