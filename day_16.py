#DICTIONARIES-
#Dictionary items are ordered, changeable, and do not allow duplicates.Dictionary items are presented in key:value pairs, and can be referred to by using the key name
mydict={
    "name":"joy",
    "age":22,
    "role":"actor",
    "color":"black"
}
print(mydict)
print(mydict["name"])
#duplicates are not allowed-Dictionaries cannot have two items with the same key:
mydict1={
    "name":"lily",
    "age":21,
    "role":"model",
    "role":"actor",
    }
print(mydict1)#it prints last occurance of role key
#dictionary length-
print(len(mydict))
print(len(mydict1))
#The values in dictionary items can be of any data type:
print(type(mydict))
#dict() constructor-It is also possible to use the dict() constructor to make a dictionary.
mydict2=dict(name="nick",age=23,country="japan")
print(mydict2)
#------------------------------------------------------------------------------------------------------------------------------------
#>Accessing dictionay items-
#you can access the items of a dictionay by reffering to its key name,inside square brackets
a=mydict1["name"]
print(a)
#>there is also a method called get() that will give you the same result
b=mydict1.get("name")
print(b)
#>the keys() method will return a list of all keys in the dictionay
c=mydict1.keys()
print(c)
#>The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car={ 
    "brand":"ford",
    "model":"mustang",
    "year":"1964"
}
print(car.keys())#before the change
print(car)
car["color"]="white"
print(car.keys())
print(car)
#>get values-the values() method will return a list of all the values in the dictionary
print(car.values())
#>the list of the values is a view of the dictionary,meaning that any changes done to the dictionary will be reflected in the views list
car["year"]=2020
print(car.values())
print(car)
#>the items() method will return each item in a dictionary,as tuples in a list
print(car.items())
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car["color"]="red"
print(car.items())
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Check if Key Exists-To determine if a specified key is present in a dictionary use the in keyword:
if "color" in car:
    print("yes")
#-------------------------------------------------------------------------------------------------------------------------------------
#Change Values-You can change the value of a specific item by referring to its key name:
car["brand"]="bmw"
print(car)
#the update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.
car.update({"year":2024})
print(car)
#--------------------------------------------------------------------------------------------------------------------------------------
#Adding items-Adding an item to the dictionary is done by using a new index key and assigning a value to it:
car["owner"]="paul"
print(car)
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
car.update({"num":7})
print(car)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#remove items-There are several methods to remove items from a dictionary:
#pop()-The pop() method removes the item with the specified key name:
car.pop("num")
print(car)
#popitem()-The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car.popitem()
print(car)
#del-The del keyword removes the item with the specified key name:
del car["year"]
print(car)
#the del keyword can also delete the dictionary completely
#clear()-The clear() method empties the dictionary:
car.clear()
print()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#loop through a dictionary-You can loop through a dictionary by using a for loop.When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
for i in mydict:
    print(i)
#Print all values in the dictionary, one by one:
for x in mydict1:
    print(mydict1[x])
#You can also use the values() method to return values of a dictionary:
for x in mydict.values():
    print(x)
#You can use the keys() method to return the keys of a dictionary:
for x in mydict1.keys():
    print(x)
#Loop through both keys and values, by using the items() method:
for l,m in mydict.items():
    print(l,m)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Copy a dictionary-
thisdict=mydict.copy()
print(thisdict)
#Another way to make a copy is to use the built-in function dict().
thisdict=dict(mydict)
print(thisdict)
