print("hello wrld")

# commment 

#This is a comment

# veriable 
a=1 
b=2
print (a+b)

# Python allows you to assign values to multiple variables in one line:
fname ,lname= "sudip","khanal"
print(fname)
print(lname)
# global veriables
# Variables that are created outside of a function are known as  global variables.

a="good morning"

def greeting():
    print ("Hello " + a)

greeting()

# local veriable example
#global veriable
a="good morning"

def greeting():
    #local veriable
    
    a="good night"
    print ("Hello " + a)
    global b 
    b= "hey"

greeting()
print(a)
print(b)


# data Type

num=6
print(type(num))
num1=9979.8349794
print(type(num1))
a='apple'
print(type(a))
b=1j
print(type(b))

# type conversion
t1=int(num1)
print(t1)

t2=float(num)
print(type(t2))
a=int(num1)

# list 

l1=[1,2,3,4,5,6,7,8,1,3,5,67]
print(type((l1)))
print(l1[2])
# list are mutable so we can modify or change the item 
l1[2]=20
print(l1)
l1.remove(1)
print(l1)
print(l1.count(5))
print(l1.index(8))
print(l1.sort())
print(l1[3:6])
print(l1[:5])
print(l1[2:])
# the append method add item the end 
l1.append(50)
print(l1)
# The insert() method inserts an item at the specified index:
l1.insert(0,20)
print(l1)

# Remove the item from list using pop()
l1.pop()
print(l1)
#loop through list

l2 = ["apple", "banana", "cherry"]
for x in l2:
  print(x)

for x in range(len(l2)):
  print(x)

#   List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# [expression iterable condition]
l3 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in l3 if "e" in x]

print(newlist)
# copy the entire list
l4=l3.copy()
print(l4)

# Use the extend() method to add list2 at the end of list1:
l1.extend(l2)
print(l1)
# tuples
tuple1 = ("apple", "banana", "cherry","orange")
print (type(tuple1))
print(tuple1)

# Convert the tuple into a list
tuple2 = ("banana", "cherry","orange")
l5=list(tuple2)
print(type(tuple2))



