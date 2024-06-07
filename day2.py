# tuples
tuple1=("apple","banana","ball")
# Slicing
print(tuple1[:2])
print(tuple1[2:])

a="helloWorld"
# string  slicing
print (a[2:6])
print (a[2:6:2])

# concatination
tuple2=(1,4,5,673,)
tuple3=tuple1+tuple2
print(tuple3)

#some basic function of tuple
print(tuple3.count(1))
print(max(tuple2))
print(min(tuple2))
print(sum(tuple2))

# enumerate=> The enumerate function in Python is a built-in function
# that adds a counter to an iterable and returns it as an enumerate object
for i,v in  enumerate(tuple3):
    print(i,v)

# zip=> Returns an iterator of tuples, where the i-th tuple 
# contains the i-th element from each of the argument sequences or iterables.


t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
zipped = zip(t1, t2)
print(zipped)
print(list(zipped)) 


#Dictionaries

dic1={'name':'ram','age':25,'num':9078494,'address':'Ktm','salary':123.2222}
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())
dic1.update({'gender':'male'})
print(dic1)
dic1.pop('num')
print(dic1)
# loop through dictonary
for x in dic1:
    print(dic1[x])
for i in dic1.keys():
    print(i)

for a,b in dic1.items():
    print(a,b)


# sets
set1 = {1, 2, 3,'apple',20,40,80}
print(set1)
set2 = {2, 3, 4,6,7,9}
print(set2)
set2.add("ball")
print(set2)

diff=set1.difference(set2)
print(diff)

intersection= set1.intersection(set2)
print(intersection)

union= set2.union(set1)
print(union)
# join
set3= set1|set2
print(set3)

#loop
# while loop

a=0
while a< 10:
    print(a)
    a+=2

# for loop

for i in range(1,10,1):
    print (i)

# Break/Continue statement
print('break')
i =1
while i < 10:
    print(i)
    if i%2==0:
        break
    i+=1

print('continue')
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  
    print(i)

# for loop with else
print("for loop with else")
for x in range(6):
  print(x)
else:
  print("finished!")

# if else statement
# print('if else statement')
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# if b > a:
#   print("second number is greater than first number")
# elif a == b:
#   print("first number and second number are equal")
# else:
#   print("first number is greater than second number")

# function
print('function')

def greeting():
    a='good morning'
    print("hello" + a)

greeting()
greeting()


def my_function(fname,lname):
  print("hello " + fname +' '+ lname)


my_function("sudip","khanal")
my_function("john","doe")

#Keyword Arguments
def fruits(a, b, p):
    print('We have', a+ ',', b+ ' and', p+ ' at our store.')

fruits('apple', 'banana', 'pineapple')

# positional argument
def nameAge(name, age):
	print("Hi, I am", name)
	print("My age is ", age)

print("Case-1:")
nameAge("Prince", 20)
print("\n Case-2:")
nameAge(20, "Prince")



# Arbitrary Arguments

def Person(*args):
    print(args)

Person('sudip', 'Male', 23, 'ktm', 9375821987)

#classes and objects
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

p1 = Person("John", "Doe")
p2=Person("sudip","khanal")

print(p1.fname)
print(p1.lname)
print(p2.fname)
print(p2.lname)

# inheritance
#  Multilevel Inheritance
class Grandparent():
   def grandparent_method(self):
        print(" Grandparent class")

class Parent(Grandparent):
    def parent_method(self):
        print(" Parent class")

class Child(Parent):
    def child_method(self):
        print(" Child class")

c1=Child()
c1.parent_method()
c1.grandparent_method()
c1.child_method()
p1=Parent()
p1.grandparent_method()
p1.parent_method()

# multiple inheritance

class Coordinator():
    name="xyz"
    def coordinator_method(self):
        print('Coordinator class')

class Teacher():
    teacher_name='abc'
    def teacher_method(self):
        print('Teacher class')

class Student(Coordinator,Teacher):
    def student_method(self):
        print('Student class')

s1=Student()
print(s1.name)
s1.teacher_method()
print(s1.teacher_name)

# Hierarchical  Inheritance
class Parent:
    def parent_method(self):
        print("This is a method in the Parent class")

class Child1(Parent):
    def child1_method(self):
        print("This is a method in Child1")

class Child2(Parent):
    def child2_method(self):
        print("This is a method in Child2")

c1=Child1()
c1.parent_method()

# hybrid inheritance
print("hybrid inheritance")
class Main:
    def Main_method(self):
        print("This is a method in the Main class")

class Parent1(Main):
    def parent1_method(self):
        print("This is a method in Parent1")

class Parent2(Main):
    def parent2_method(self):
        print("This is a method in Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is a method in the Child class")

# Example usage
c = Child()
c.Main_method()      
c.parent1_method()    
c.parent2_method()   
c.child_method()     


# Iterators
print('Iterators')
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

str = "banana"
iter1 = iter(str)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

class DemoItertor():
    def __init__(self) :
        self.a=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a<=10:
            val=self.a
            self.a+=1
            return val
        else:
            raise StopIteration

obj1=DemoItertor()
for i in obj1:
    print(i)

        
# Duck typing in Python emphasizes an object's
# behavior over its explicit type, allowing for more flexible and reusable code.
class Duck:  
   def swim(self):  
         print("I'm a duck, and I can swim.")  
   
class Sparrow:  
     def swim(self):  
         print("I'm a sparrow, and I can swim.")  
   
class Crocodile:  
     def swim_walk(self):  
         print("I'm a Crocodile, and I can swim, but not quack.")  
   
# The duck_testing function takes an animal object and calls its swim method.
# This function assumes that any object passed to it will have a swim method.
def duck_testing(animal):  
     animal.swim()   
       
duck_testing(Duck())  
duck_testing(Sparrow())  
# duck_testing(Crocodile())  

# operator overloading
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 7)
p2 = Point(2, 3)

print(p1+p2)

# Polymorphism in Class Methods
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("jerry", 3)
dog1 = Dog("jojo", 4)

cat1.make_sound()
cat1.info()
dog1.make_sound()
dog1.info()

# method overriding
class Cow ():
     def __init__(self, name):
        self.name = name

     def intro(self):
        print(f"I am a cow. My name is {self.name}.")

     def color(self):
         print("Red")

class Buffalo (Cow):

    def intro(self):
        print(f"I am a buffalo. My name is {self.name}.")

    def color(self):
         print("Black")

c1=Cow("milky")
b1=Buffalo("jack")
c1.intro()
c1.color()
b1.intro()
b1.color()


# working of try() 
def divide(x, y):
	try:
		result = x / y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

divide(3, 0)

# another example
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        print("The error is: ",e)

divide(3,0)

# Program to depict else clause with try-except

# Function which returns a/b
def demo(a , b):
	try:
		c = ((a+b) // (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

demo(2.0, 3.0)
demo(3.0,3.0)

# JSON in Python
import json
x =  '{ "name":"sudip", "age":23, "city":"Ktm"}'

# parse x:
y = json.loads(x)

print(y)

# Convert from Python to JSON:

dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
jsonn = json.dumps(x)

print(jsonn)


# Python String Formatting
txt = f"example of string formating"
print(txt)

name = "john"
txt = f"My name is {name} "
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)