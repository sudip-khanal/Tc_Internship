# Comprehenssion
# Given a list of numbers, remove all odd numbers from the list.
list1=[1,2,3,4,7,5,3,8,4,8,9,55,65,75,33,43]
result=[var for var in list1 if var%2==0]
print(result)

# Create a dictionary of squares of numbers from 1 to 10 using dictionary comprehenssion.

dic1={a:a for a in range(1,11)}
print(dic1)

# Create a dictionary of even numbers as keys and their squares as values using dictionary comprehenssion.

dic2={x:x**2 for x in range(1,20) if x%2==0}
print(dic2)

# Generate a set of squares of numbers from 1 to 10 using set comprehenssion.
   
set_comp = {z**2 for z in range(1,11)}
print(type(set_comp))
print(set_comp)

# Generate a set of tuples containing numbers and their squares using set comprehenssion.

set_comp2={(b,b**2) for b in range(1,10)}
print(type(set_comp2))
print(id(set_comp2))
print(set_comp2)

# Instance Method
# Define a Rectangle class with attribures width, height. Wrire a
#  instance methods to calculate area of the rectangle and perimeter of the rectangle.

class Rectangle():
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def Area(self):
        area= self.height * self.width
        return area
    
    def Perimeter(self):
        perimeter= 2*(self.height+self.width)
        return perimeter
    
rec1=Rectangle(10,5)
rec2=Rectangle(7,7)
print("Area:" ,rec1.Area())
print("Perimeter:" ,rec1.Perimeter())
print("Area:" ,rec2.Area())
print("Perimeter:" ,rec2.Perimeter())

# static method
# Create a class called StringOperations with a static method is_palindrome that takes a string as an argument and
#  returns True if the string is a palindrome, and False otherwise.

class StringOperations():
    @staticmethod
    def is_palindrome(str):
        for i in range(0, int(len(str)/2)):
            if str[i] != str[len(str)-i-1]:
                return False
        return True
    
print(StringOperations.is_palindrome("apple")) 
print(StringOperations.is_palindrome("rar"))        


#  Create a class called DateUtils with a static method format_date
#   that takes a date object and returns it as a string in the format YYYY-MM-DD.
from datetime import *

class DateUtils():

    @staticmethod
    def show_time():
        today = str(date.today())
        print(today)
        print(type(today))
DateUtils.show_time()

# lambda
# Write a Python program to filter a list of even integers using Lambda.

li1=[20,3,90,44,54,32,43,65,44,55,70,90,40,90,60,70,]

even=list(filter(lambda x:x%2==0,li1))
print(even)

# Write a Python program to filter a list of odd integers using Lambda.

li2=[20,3,90,44,54,32,43,65,44,55,70,90,40,90,60,70,]

odd=list(filter(lambda x:x%2!=0,li2))
print(odd)

# Write a Python program to square and 
# cube every number in a given list of integers using Lambda.

li3=[1,2,3,4,5,6,7,8,9]
square=list(map(lambda a:a*2,li3))
print(square)

cube=list(map(lambda a:a**3,li3))
print(cube)

# class method
# Create a class Counter with a class attribute count.
#  Add a class method increment that increments the count by 1. 
#   Add another class method reset that sets the count back to 0.


class Counter():
    count=0

    @classmethod
    def increment(cls):
        cls.count  += 1

    @classmethod
    def reset(cls):
        cls.count=0

print(Counter.count)

Counter.increment()
print(Counter.count)

Counter.reset()
print(Counter.count)

Counter.increment()
print(Counter.count)

# threading
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

# Create a class Date with attributes day, month, and year. Add a class 
# method today that returns a new instance of Date with the current date.

class Date():
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    @classmethod
    def today(cls):
        current_date = datetime.today()
        # print(type(current_date))
        return cls(current_date.day, current_date.month, current_date.year)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
print(Date.today())



# Decorator

# Create a decorator that modifies the return value of a function by doubling it.


def double_return(func):
    def inner(a,b):
        result = func(a,b)
        return result * 2
    return inner

@double_return
def add(a, b):
    return a + b

output=add(3, 5)
print(output)

    

# Write a Python program to create a decorator 
# function to measure the execution time of a function.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.3f} seconds to execute")
        return result
    return wrapper

# Example usage
@measure_time
def add(a,b):
    sum=a+b
    return sum

# Call the decorated function
result = add(500,900)
print("Result:", result)




