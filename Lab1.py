#Comments
#value of x is 1
x=1
if x>0:
    print("There are two comments") #value is string 
#---------------------
#multi line statement
print("statement 1")
print("statement 2")
#you can write it as
print('statement 3');print("statement 4")
#-----------------------
#indentation
y=1
if y>0:
    print("Thise statement has a single space indentation")
    print("Thise statement has a single t6ab indentation")
    print("Thise statement has a single tab+space indentation")
#-----------------------
#type casting
n="687"
print("value= ", n)
print("type = ", type(n))
# converting it to float
n = float(n)
print("new value = ", n)
print("new type = ", type(n))
#complex type
v = complex(1,6)
print(v)
print(type(v))
# type bool
c = True
print(type(c))
# string
s = "string"
print(s)
# escape sequence
print("\\backslash")
print("this is \n new line")
print("this is \t tab")
print("\'single qoute\'")
print("\"double qoute\"")
#string indices
st = "python"
print(st [0])
print(st [-4])
# creating lists
l1 = [5,6,9,2]
print(l1)
l2 = ['red','brown','lion']
print(l2)
l3 = ['red',57,6.98]
print(l3)
# list indeces
print(l1[0:2])
print(l1[:])