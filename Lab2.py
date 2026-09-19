# while loop
count = 0
while (count<3):
    count=count+1
    print("hello geek")
#single statement while block
alpha = -1
while(alpha>0):print("Hello Geeks")
#for loop
#ex 1
print("Loop Iterations")
l=["geeks","for","geeks"]
for i in l:
    print(i)
#Ex 2
print("\nTuple Iterations")
t =("geeks","for","geeks")
for i in t:
    print(i)
#Ex 3
print("\n String Iterations")
s = "Geeks"
for i in s:
    print(i)
# iterating by index of sequence
list = ["geeks","for","geeks"]
for index in range(len(list)):
    print (list[index])
# control statemenents in loop
# continue statement
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print("Current Letter: ",letter)
# break statement
for l in "geeksforgeeks":
    if l == 'e' or l == 's':
        break
    print("letter= ",l)
# Functions
def my_function():
    print("Hello from function")
my_function()
# by giving parameters
def fun(fname):
    print(fname +" Reference")
fun("Email")
fun("Name")
# default parameter value
def fin(country="Norway"):
    print("My country is "+ country)
fin()
fin("Pakistan")
fin("Italy")
# list as parameter
def frutty(food):
    for x in food:
        print(x)
fruit = ["apple","banana","pear","orange"]
frutty(fruit)
# retun statement
def add(v):
    return 6 + v
print(add(67))
print(add(46))
# keyword arguments
def child(child3,child2,child1):
    print("My youngest child is: " +child3)
child(child1="EMAIL",child2="LUIS",child3="LINUS")
# Python object and classes
class MyClass:
    g=5
    j=4
p1=MyClass() 
print(p1.g)
p2=MyClass()
print(p2.j)
print(p2.g + p2.j)
print(p2.j - p1.g)
# use function to assign values to object properties
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
p3= Person("Umair",22)
print(p3.name)
print(p3.age)