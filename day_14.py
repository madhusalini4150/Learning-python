#SETS-
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#---------------------------------------------------------------------------------
myset={"apple","orange","banana"}
print(myset)
myset=set(("apple","banana","kiwi"))
print(myset)
#creating an empty set
set1=set()
print(set1)
# Creating a Set with the use of a List
#Sets are unordered, so you cannot be sure in which order the items will appear.
set1=set(["a","b","c"])
print(set1)
# Creating a Set with the use of a tuple
tup=(1,2,3)
print(set(tup))
#---------------------------------------------------------------------------------------------
#Duplicates not allowed
myset={"apple","banana","apple"}
print(myset)
#The values True and 1 are considered the same value in sets, and are treated as duplicates
myset1={"apple",True,1,2}
print(myset1)
#The values False and 0 are considered the same value in sets, and are treated as duplicates
myset2={"banana",False,0,1}
print(myset2)
#----------------------------------------------------------------------------------------------------
#Get the length of a set
#To determine how many items a set has, use the len() function.
myset3={"riya",18,"pink","water"}
print(myset3)
print(len(myset3))
print(type(myset3))
#------------------------------------------------------------------------------------
#Access Items-
#You cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset={"divya","madhu","sridivya","madhusalini"}
for i in thisset:
    print(i)
print("madhu" in thisset)
print("sri" in thisset)
print("sri" not in thisset)
#------------------------------------------------------------------------------------------------
#Add Set Items-
#Once a set is created, you cannot change its items, but you can add new items
#>To add one item to a set use the add() method
myset={"pink","blue","yellow","black"}
myset.add("white")
print(myset)
#Add Sets-
thisset={"purple","orange","green"}
myset.update(thisset)
print(myset)
#Add any iterable-The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
mylist=[1,2,3,4,5]
myset.update(mylist)
print(myset)
#-----------------------------------------------------------------------------------------------------------------
#Remove Set Items-
#To remove an item in a set, use the remove(), or the discard() method.
myset.remove("blue")
print(myset)
#If the item to remove does not exist, remove() will raise an error
myset.discard("yellow")
#If the item to remove does not exist, discard() will NOT raise an error.
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.The return value of the pop() method is the removed item
x=myset.pop()
print(x)#removed item
print(myset)#the set after removal
#Clear-The clear() method empties the set:
myset.clear()
print(myset)
#del-The del keyword will delete the set completely:
#del myset
#print(myset)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Loop Sets-
#>Loop items-You can loop through the set items by using a for loop:
clrs={"yellow","blue","pink","white"}
for i in clrs:
    print(i)
#-----------------------------------------------------------------------------------------------------------------------------
