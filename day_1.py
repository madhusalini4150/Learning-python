#First program
print("Hello,World!")
#taking input from the user
name=input("enter name:")
print("hello",name)
#taking multiple inputs in single line
cups,glasses=input("enter count:").split()
print("number of cups:",cups)
print("number of glasses:",glasses)
#---------------------------
print(3+4)#addition 
print(3-4)#subtrction
print(3*4)#multiplication
print(3/4)#division
print(3//4)#floor division
print(3%4)#modulo division
print(3**4)#exponential
#determine the type of objects
print(type(10))
print(type(3.14))
print(type(1+3j))
print(type('python'))
print(type([1,3.5,5.666666]))
print(type({'name':'siri'}))
print(type({1,3333.4,55.66666}))
print(type((2,4.5,6.888888)))
# declaring multiple variables in single line
a,b,c="orange","mango","watermelon"
print(a)
print(b)
print(c)
#print in single line
print(a,b,c)
#declaring multiple variables which are having the same value
l=m=n="india"
print(l)
print(m)
print(n)
#var that created outside of a function
#global var can be used in inside and outside 
#local var are cretaed inside the function
x="awesome"
def myfun():
    print(x)
myfun()
#--------------------------
a="watermelon"
def fun():
    a="mango"
    print(a)
fun()
print(a) 
#-----------------------------
def my():
    global x
    x="future"
my()
print(x)
#-----------------------------
x="lily"
def fun():
    global x
    x="rose"
fun()
print(x)
#--------------------------
#some built in functions
#print(),len(),type(),int(),float(),pow(),list(),sum(),min(),max(),str(),input(),dict(),help(),map(),set(),tuple(),eval(),.....so on
#examples
print("hello")
print(len('hello'))
print(type(11))
print(int('10'))
print(type(10))
print(str(10))
print(type(str(10)))
print(float(55))
help('keywords')
print(input("enter name:"))
print(min(11,2,3333))
print(max(11,2,3333))
print(sum([11,3,2]))
print(min([1,3,4]))
print(max([3,2,1]))
print(sum({1,2,3}))
print(sum((1,2,3)))
# checking python version
import sys
print(sys.version)
#getting list of keywords
import keywords
print(keyword.kwlist)
