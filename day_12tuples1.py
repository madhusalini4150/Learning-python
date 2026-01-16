#Unpack Tuples-
#>When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits=("apple","banana","cherry","guava","kiwi")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
print(fruits)
x,y,z,u,v=fruits
print(x,y,z,u,v)
#The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
#>Using Asterisk*-If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a lis
print(fruits)
x,y,*rem=fruits
print(x,y,*rem)
print(x,y,rem)
print(x)
print(y)
print(rem)
print(type(fruits))
*a,b,c=fruits
print(a)
print(b)
print(c)
l,*m,n=fruits
print(l,m,n)
#---------------------------------------------------------------------------
#Loop Through a Tuple-
#>You can loop through the tuple items by using a for loop
thistuple=("insta","utube","snap","fb")
for x in thistuple:
    print(x)
#>Loop Through The index Numbers
#You can also loop through the tuple items by referring to their index number.Use the range() and len() functions to create a suitable iterable.
for i in range(len(thistuple)):
    print(thistuple[i])
#You can loop through the tuple items by using a while loop.
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1
#------------------------------------------------------------------------------------------------------------------------------------
#>Join Two Tuple/Concatenation of Tuples:
#To join two or more tuples you can use the + operator,Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined. 
fruits=("apple","mango","kiwi","grape")
vegee=("tomato","onion","potato")
f_and_v=fruits+vegee
print(f_and_v)
#>Multiply Tuples:If you want to multiply the content of a tuple a given number of times, you can use the * operator
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
mytuple=fruits*3
print(mytuple)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Count()-The count() method returns the number of times a specified value appears in the tuple.
print(mytuple.count("apple"))
#Index()-The index() method finds the first occurrence of the specified value.The index() method raises an exception if the value is not found.
print(mytuple.index("kiwi"))
#----------------------------------------------------------------------------------------------------------------------------------------------------
#Slcing of tuple:
print(vegee[1:])
print(vegee[::-1])#reverse the tuple


