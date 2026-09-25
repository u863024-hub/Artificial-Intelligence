#A PROGRAM  to find numbers which are divisible by 7 and multiple of 5 between 1500 and 2700
num=[]
for i in range (1500,2701):
    if i%7==0 and i%5==0:
        num.append(i)
print("Num=", num)
#program for converting temp to and from celcius,ferhanite
C=60
F=45
c=(F-32)*5/9
f=C*9/5 + 32
print("Temp in Celcius=",c)
print("Temp nin Farhenheite=",f)
# prograwm to guess a num between 1-9
n = 6
while True:
    guess = int(input("Guess a number between 1 to 9: "))
    if n == guess:
        print("Well guessed")
        break    
# program to print pattern using nested for loop
'''*
   **
   ***
   ****
   *****
   ****
   ***
   **
   *'''
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()
# program to accept a word from user and reverse it
word = input("Enter a word to reverse : ")
print("Reverse word is : ", "".join(reversed(word)))
# program to count even and odd numbers
number = (1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in number:
    if i%2==0:
        even = even + 1
    else:
        odd = odd + 1
print("Number of Evens: ",even)
print("Number of Odds: ",odd)
# program that prints each item and its type from list
list = [1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]
for i in list:
    print(i,type(i))
# program to print num 0-6 except 3,6 using continue statement
a = (0,1,2,3,4,5,6)
for i in a:
    if i==3 or i==6:
        continue
    print(i)
# program to print fibonacci series btween 0-50
b=0
c=1
while b<=50:
    print(b,end=",")
    sum = b + c
    b = c
    c = sum
# program to iterate num 1-50 if num multiple of 3 print fizz,if of 5 print buzz,if both print fizzbuzz
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        continue
# program that accept column and rows ,generates two dimensional array ,the element vaue in i-th row and j-th column should be i*J
row = int(input("Enter rows: "))
column = int(input("Enter column: "))
for i in range(row):
    for j in range(column):
        print(i*j,end="")
    print()
#program that accepts sequence of lines(blank line to terminate) as input and prints line as output(all characters in lower case)
while True:
    line = input("Enter a line:")
    if line=="":
        break
    print(line.lower())
# program that accept a sequence of comma seperated 4 digit binary number as input and print the number that are divisible by 5 in a comma seperated sequence
binary = input("Enter 4 digit binary Numbers: ").split(",")
result = []
for i in binary:
    if len(i)==4 and all(x in "01" for x in i):
        decimal = int(i,2)
        if decimal%5==0:
            result.append(i)
    else:
        continue
print("Results are: ",result)
#program that accepts a string and calculates number of digits and letters
text = input("Enter a string:")
l=0
d=0
for i in text:
    if i.isalpha():
        l=l+1
    elif i.isdigit():
        d=d+1
    else:
        continue
print("Number of Letter: ",l)
print("Number of Digit: ",d)
#program to check password validation enter by user,at least 1 letter between [a-z],1 between [A-Z],1 between [0-9],1 character from [$#@], min length 6 max length 16
password = input("Enter a password: ")
lower = 0
upper = 0
digit = 0
special = 0

if len(password)>=6 and len(password)<=16:
    for i in password:
        if i.islower():
            lower = lower + 1
        elif i.isupper():
            upper = upper + 1
        elif i.isdigit():
            digit = digit + 1
        elif i in "$#@":
            special = special + 1
        else:
            print("Invalid Password")
            break
else:
        print("Invalid length")
if lower>=1 and upper>=1 and digit>=1 and special>=1:
    print("Valid password")
else:
    print("Enter a strong password")