#BOOLEAN DATA TYPE
#Booleans represent one of two values: True or False
#In programming you often need to know if an expression is True or False
#>When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10>2)
print(2<1)
print(10==3)
#The bool() function allows you to evaluate any value, and give you True or False in return
#Almost any value is evaluated to True if it has some sort of content
#Any string is True, except empty strings
#Any number is True, except 0
#Any list, tuple, set, and dictionary are True, except empty ones
print(bool("hello"))
print(bool(15))
print(bool(["apple","cherry","kiwi"]))
#n fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
print(bool(False))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(""))
print(bool(None))
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
a=200
print(isinstance(a,int))
print(isinstance(a,float))
#functions can return a boolean value
def myfun():
    return True
print(myfun())
#-------------
def myfun():
    return False
print(myfun())
#===================================================================================================
#____OPERATORS____
#operators are used to perform operations on variables and values
#in the below example,we use the + operator to add together two values
print(10+8)
#Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables:
sum1=12+5
sum2=sum1+10
sum3=sum2-10
print(sum1)
print(sum2)
print(sum3)
#====ARITHMETIC OPERATORS====
#Arithmetic operators are used with numeric values to perform common mathematical operations:
#"+","-","*","/","%","//","**"
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#division-
#Python has two division operators:
#>/ - Division (returns a float)
#>// - Floor division (returns an integer),It rounds DOWN to the nearest integer
x = 12
y = 5
print(x / y)
#----------
x = 12
y = 5
print(x // y)
#====ASSIGNMENT OPERATORS====
#"=","-=","+=","/=","%=","//=","**=","&=",.....
x=5
print(x)
#--------
x+=3
print(x)
#--------
x-=3
print(x)
#-----------
#The Walrus Operator
#Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
numbers=[1,2,4,4,6,7]
#normal way:
count=len(numbers)
if count>3:
    print(f"List has {count} elements")
#using walrus operator(:=)
if(count := len(numbers))>3:# t assigns a value and checks a condition at the same time.
    print(f"List has {count} elements")
#====COMPARISON OPERATORS====
#"==","!=",">","<",">=","<="
x=3
y=2
print(x==y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x!=y)
#chaining comparison operators-Python allows you to chain comparison operators:
num=4
print(1<x<10)
print(1<x and x<10)
#====LOGICAL OPERATORS
#"and","or","not"
#and-Returns True if both statements are true
print(1>3 and 3<4 )
print(10>4 and 2<4)
#or-Returns True if one of the statements is true
print(1>3 or 3<4 )
print(10>4 or 2<4)
#not-Reverse the result, returns False if the result is true
print(not(1>3 and 3<4))
print(not(10>4 and 2<4))
#====IDENTITY OPERATORS
#"is","is not"
#is-Returns True if both variables are the same object
x="hello"
y="hello"
z="hi"
print("x is y:",x is y)
print("x is z:",x is z)
#is not-Returns True if both variables are not the same object
print("x is not y:",x is not y)
print("x is not z:",x is not z)
#----------------------------------
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)
#Difference Between is and ==
#>is - Checks if both variables point to the same object in memory
#>== - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
#MEMBERSHIP OPERATORS
#"in","not in"
#in-Returns True if a sequence with the specified value is present in the object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
#not in-Returns True if a sequence with the specified value is not present in the object
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
#Membership in Strings
#The membership operators also work with strings:
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)
#====BITWISE OPERATORS====
#Bitwise operators are used to compare (binary) numbers:
#"&","|","^","~","<<",">>"
#&(AND)-A bit is 1 only if both bits are 1
a = 5      # 0101
b = 3      # 0011
print(a & b)
#|(or)-A bit is 1 if at least one bit is 1
print(a|b)
''' 0101
| 0011
------
  0111 → 7'''
#^(Bitwise XOR (Exclusive OR))-A bit is 1 only if bits are different
print(5 ^ 3)
'''0101
^ 0011
------
  0110 → 6'''
#~(bitwise not(complement)-Flips all bits (1 → 0, 0 → 1)
print(~5)
'''~x = -(x + 1)
~5 = -(5 + 1) = -6'''
#<<(Left Shift)-Shifts bits to the left, adds 0s on the right,Each shift multiplies by 2
print(5 << 1)
'''5 = 0101
<< 1
= 1010 → 10''' #another example
print(5 << 2)   # 5 × 2²
#>>(right shift)-Shifts bits to the right,Each shift divides by 2
print(10 >> 1)
'''10 = 1010
>> 1
= 0101 → 5'''
print(10 >> 2)   # 10 ÷ 2²
#Left shift	Multiply by 2ⁿ
#Right shift Divide by 2ⁿ