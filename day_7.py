#change a range of item values
mylist=[1,2,3,4,5,6]
print(mylist)
mylist[2:5]=[10,11,12]
print(mylist)
#---------------------------------------------------------------------------------
#ADDING ELEMENTS TO LIST
#>Inset()-The insert() method inserts an item at the specified index
mylist.insert(3,100)
print(mylist)
fruits=["apple","cherry","banana"]
fruits.insert(1,"kiwi")
print(fruits)
#>Append()-to add an item to the end of the list,use the append() method
fruits.append("orange")
print(fruits)
#>Extend()-Adds multiple elements to the end of the list
fruits.extend(["guava","blackberry","strawberry"])
print(fruits)
#or
fruits.extend(("guava","blackberry","strawberry"))
print(fruits)
#or
myfruits=["mango","papaya","kiwi"]
fruits.extend(myfruits)
print(fruits)
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
count=(59,76)
fruits.extend(count)
print(fruits)
#--------------------------------------------------------------------------------------------------------
#REMOVING LIST ITEMS
#>Remove()-The remove() method removes the "specified item"
fruits.remove("kiwi")
print(fruits)
#If there are more than one item with the specified value, the remove() method removes the first occurrence
#>Pop()-The pop() method removes the "specified index"
fruits.pop(2)
print(fruits)
#If you do not specify the index, the pop() method removes the last item
fruits.pop()
print(fruits)
#>Del()-The del keyword also removes the specified index:
del fruits[3]
print(fruits)
#it can also be used to delete items within index range
del fruits[3:6]
print(fruits)
#The del keyword can also delete the list completely
#del fruits-it delete fruits list completely, #this will cause an error because you have succsesfully deleted "fruits"
#>Clear()-The clear() method empties the list,The list still remains, but it has no content
fruits.clear()
print(fruits)
#-----------------------------------------------------------------------------------------------------------------------
#Copy a list-You can use the built-in List method copy() to copy a list
thislist=["apple","banana","cherry"]
print(thislist)
mylist=thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method list()
mylist=list(thislist)
print(mylist)
#You can also make a copy of a list by using the : (slice) operator
mylist=thislist[:]
print(mylist)
#-------------------------------------------------------------------------------------------------------------------------
#Join two lists
#There are several ways to join, or concatenate, two or more lists in Python,One of the easiest ways are by using the + operator
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)
#Another way to join two lists is by appending all the items from list2 into list1, one by one
for i in list2:
    list1.append(i)
print(list1)
#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1.extend(list2)
print(list1)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Count()-The count() method returns the number of elements with the specified value.
x=thislist.count("cherry")
print(x)
y=list1.count("a")
print(y)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#reverse()-The reverse() method reverses the sorting order of the elements
thislist.reverse()
print(thislist)
#------------------------------------------------------------------------------------------------------------------------------------------------
#sort()-List objects have a sort() method that will sort the list alphanumerically, ascending, by default
thislist=["python","java","c","c++"]
thislist.sort()
print(thislist)
#sort desecnding-To sort descending, use the keyword argument reverse = True:
thislist.sort(reverse=True)
print(thislist)
#Case insensensitive sort-By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
