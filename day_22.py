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


