#TUPLE-Tuples are used to store multiple items in a single variable
#A tuple is a collection which is ordered and unchangeable.
#-----------------------------------------------------------------------------------
#>Creating a tuple--
mytuple=("books","pen","pencil","eraser","scale")
print(mytuple)
#empty tuple:
empty_tuple=()
print(empty_tuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Allow duplicates-
mytuple1=("books","pen","pencil","eraser","scale","pen")
print(mytuple1)
#>Creating a tuple with mixed datatypes:
mytuple2=("jennie",21,[1,2,3],True)
print(mytuple2)
#>Creating a tuple with nested tuples:
mytuple3=(("hi",
            "hello"))
print(mytuple3)
#or
tup1=("apple","mango")
tup2=("cherry","kiwi")
tup3=(tup1,tup2)
print(tup3)
#>Creating a tuple with repetition:
tup4=("food",)*4
print(tup4)
#>Creating a tuple with the use of loop:
tupl=("kiwi")
for i in tupl:
    print(i)
tupl=("japan")
n=1
for i in range(int(n)):
    tupl=(tupl,)
    print(tupl)
#------------------------------------------------------------------------------
#Tuple length-
#To determine how many items a tuple has, use the len() function
print(len(mytuple))
print(len(mytuple1))
#------------------------------------------------------------------------------
#Create a tuple with one item-
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
tuple1=("banana",)
print(tuple1)
print(type(tuple1))
tuple2=("banana")
print(tuple2)
print(type(tuple2))
#---------------------------------------------------------------------------------
#The tuple() Constructor-
#It is also possible to use the tuple() constructor to make a tuple.
tuple3=tuple(("apple"))
print(tuple3)
#-----------------------------------------------------------------------------------
#>Access Tuple Items-
#You can access tuple items by referring to the index number, inside square brackets:
print(mytuple[1])
#negative indexing-
print(mytuple[-3])
print(mytuple[-1])
#>Range of Indexes-
#You can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new tuple with the specified items
print(mytuple[1:4])#the search will start at index 1(included) and end at index 4(not included)
print(mytuple[:3])#By leaving out the start value, the range will start at the first item
print(mytuple[2:])#By leaving out the end value, the range will go on to the end of the tuple
#Range of Negative Indexes-
print(mytuple)
print(mytuple[-3:-1])#returns the items from index -3(included) to index -1 (excluded)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Check if item exists-
#To determine if a specified item is present in a tuple use the in keyword
print(mytuple)
if "sharpner" in mytuple:
    print("yes")
else:
    print("no")
#-----------------------------------------------------------------------------------------
#Update tuples-Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.But there are some workarounds
#>Change Tuple Values-You can convert the tuple into a list, change the list, and convert the list back into a tuple
print(mytuple)
mylist=list(mytuple)
print(mylist)
mylist[1]="sharpner"
print(mylist)
newtuple=tuple(mylist)
print(newtuple)
#>Add Items-there are other ways to add items to a tuple.
#1.Convert into a list:
mylist.append("marker")
newtuple=tuple(mylist)
print(newtuple)
# Add tuple to a tuple:You are allowed to add tuples to tuples
print(newtuple)
tp=("sketch",)#When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple
newtuple+=tp
print(newtuple)
#>Remove Items-
#1.Convert the tuple into a list
print(newtuple)
lst=list(newtuple)
lst.remove("sketch")
modtuple=tuple(lst)
print(modtuple)
#Or you can delete the tuple completely
#del newtuple
#print(newtuple) #this will raise an error because the tuple no longer exists
#--------------------------------------------------------------------------------------------------------------------------------------------

