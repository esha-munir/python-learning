
#This is how to import libraries
import keyword
n=keyword.kwlist
print(n)
print(len(n))
# this is how we can import math library
import math
r=math.factorial(4)
print(r)
#this is how we can open turtle screen in python
import turtle
Screen=turtle.Screen()
Screen.setup(600,600)
Screen.title("ESHA Munir")
turtle.done()

#this is how we can allocate space between variablesp
x=45
y=90
w=34
print(x,y,w,sep='     ')
print(x,y,w,sep='EM')



#Conditional statement 
e=int(input("Enter first num: "))
m=float(input("Enter second num: "))
if e>m:
    print("e is greater than m:")

elif m>e:
    print("e is less than m: ")

else:
    print("E and M are Equal:")


#For loop

E="Esha Munir"
for i in E:
    print("i am a beginner:")
    print("inspired by sir Mushahid hussain: ")

#concept of while loop

x=0
while x<10:
    print("I like to learn coding: ")
    x=x+1





