#magic methods
# print(dir())
# print(dir(int))

# num=10
# res = num.__add__(5) 
# print(res)


# class Employee:
#   def __new__(cls):
#     print ("__new__ magic method is called")
#     inst = object.__new__(cls)
#     return inst
#   def __init__(self):
#     print ("__init__ magic method is called")
    
    
# emp = Employee()




# Write a Python program that creates a generator function
# that yields cubes of numbers from 1 to n. Accept n from the user.

# def cube_genrator(n):
#     for i in range(1,n+1):
#         yield i**3
    
# n = int(input("Enter the number: "))

# cube=cube_genrator(n)
# for i in cube:
#     print(i)





# Write a Python program to implement a generator 
# that generates random numbers within a given range.

# import random

# def random_generator(start, end):
#     while True:
#         yield random.randint(start, end)

# random_numbers = random_generator(10, 15)
# for i in range(10):
#     print(next(random_numbers))

 

# Write a function process_data that takes any number of positional
# and keyword arguments, prints the sum of all positional arguments, and
# then prints all the keyword arguments.

# def process_data(*args ,**kwargs):
#     cal_sum = sum(args)
#     print("Sum of positional arguments:", cal_sum)

#     for a, b in kwargs.items():
#          print(f"{a}: {b}")

# process_data(1,2,3,a=2,b=3,c=5,d=7)



# Write a function calculate that takes any number of positional and 
# keyword arguments. If a keyword argument operation is provided, it 
# performs the specified operation (add, subtract, multiply, divide) on
# all the positional arguments. If no operation is provided, it should default to add.

def calculate(*args, **kwargs):
    operation = kwargs.get('operation','add')
    
    if not args:
        return None

    if operation == 'add':
        result = sum(args)
    
    elif operation=='sub':
        result=args[0]
        for num in args[1:]:
            result -= num

    elif operation=='mul':
        result = 1
        for num in args:
            result *= num
        
        pass
    elif operation=='div':
        result= args[0]
        for num in args[1:]:
            result /= num
        
  
    return result
    
        
print(calculate(1, 2, 3, 5))
print(calculate(1,2,3, operation ='mul'))
print(calculate (10,20,20,operation ='add'))
print(calculate (20,20,30,40,operation ='div'))
print(calculate (2,20,op ='sub'))
#print(operation='mul')


    

    # slicing


# a=['apple','ball','cat','dog', 'elephant','flag']
# print(a[0])
# print(a[-1])
# print(a[2:5])
# print(a[:3])
# print(a[3:])
# print(a[-5:-2])
# print(a[2:len(a)])
# print(a==a[:])
# print(a[:])
# print(a[1:6:2])
# print(a[::-1])


# creating metaclasse

# class Hello(type):
    
