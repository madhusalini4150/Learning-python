#FUNCTIONS
#A function is a reusble block of code or programming statements designed to perform a certain task.A function helps avoiding code repetition.
#To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.
#Creating a Function-
def my_function():
    print("Hello from a function")
my_function() #To call a function, write its name followed by parentheses
#You can call the same function multiple times
def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()
#Return Values-
#return is used inside a fuction to send a value back to the place where the function was called.when a function reaches a retuen statement,it stops executing and sends the result back
def get_greeting():
    return "Hello!!"
message=get_greeting()
print(message)
#you can use the returned value directly
def get_greeting():
    return "hii"
print(get_greeting())#if a function doesn't have a return statement,it returns None by default.
#Pass Statement-
#Function definitions cannot be empty.if you need to create a function placeholder without any code,use the pass statement:
def function():
    pass            #The pass statement is often used when developing, allowing you to define the structure first and implement details later.


#Parameters-Parameters are variables written inside the function definition,they act as placeholders.
#Arguments-Arguements are actual values passed to the function when calling it.
def greet(name): #name is parameter
    print('hello',name)
greet("Riya") #Riya is parameter

def add(a,b): #here a,b is parameters
    return a+b
result=add(10,20) #here 10,20 is arguments
print(result)

#Number of Arguments-By default,a function must be called with the correct number of arguments.if your function expects 2 arguments,you must call it with exactly 2 arguments.
def my_function(fname,lname):
    print(fname,lname)
my_function("Emil","Refsnes") #if you try to call the function with the wrong number of arguments,you will get an error.

#Default Parameter Values-we can assign default values to parameters.If the function is called without an argument,it uses the default value
def my_fun(name="friend"): #friend is a default value
    print("Hello",name)
my_fun("Emil")
my_fun()  #in this line it prints friend
my_fun("Robert")
my_fun("Linus")
 
def greet(name,country="India"):
    print(name,country)
greet("Max")
greet("Max","USA")
 
def greetings(name="Peter"):
    message=name+',welcome to python for Everyone!'
    return message
print()

#Keyword Arguments(kwargs)-we can send arguments with the key=value syntax
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function(animal="dog",name="Buddy")
#this way,with keyword arguments,the order of the arguments does not matter.
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function(name="Buddy",animal="dog")

#Positional Arguments-when you call a function with arguments without using keywords,they are called positional arguments.Positional arguments must be in the correct order.
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function("dog","Buddy")
#the order matters with positional arguments
def my_function(animal,name):
    print("I have a",animal)
    print("My",animal+"'s name is",name)
my_function("Buddy","dog")
def animal(*name):
    print("i have a pet",name[1])
    print("i have a pet",name[0])
animal("dog","cat","cow")
#Mixing positional and keyword Arguments-you can mix positional and keyword arguments in a functional call.However, positional arguments must come before keyword arguments.
def new_function(animal,name,age):
    print("I have a", age, "year old", animal, "named", name)
new_function("dog", name="Buddy",age=5)
new_function("cat",name="mini",age=3)

#Passing Different Data Types-You can send any data type as an argument to a function(string,number,list,dictionary,etc.)
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits=["apple","banana","cherry"]
my_function(my_fruits)

#Positional-Only Arguments:you can specify that a function can have only positional arguments.To specify positional-only arguments,add ",/" after the parameters
def my_function(name,/):
    print("Hello",name)
my_function("Emil")
#without the ",/" you are actually allowed to use keyword arguments even if the function expects positional arguments
def my_function(name):
    print("Hello",name)
my_function(name="Emil") #with ",/" you will get an error if you try to usse keyword arguments

#Keyword-Only Arguments:To specify that a function can have only keyword arguments,add "*," before the parameters:
def my_function(*,name):
    print("Hello",name)
my_function(name="Emil")
#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments
def my_function(name):
    print("Hello",name)
my_function("emil") #With *,, you will get an error if you try to use positional arguments

#Combining Positional-Only and Keyword-Only:parameters before / are positional-only, and parameters after * are keyword-only
def my_function(a,b,/,*,c,d):
    return a+b+c+d
result=my_function(4,6,c=50,d=10)
print(result)

