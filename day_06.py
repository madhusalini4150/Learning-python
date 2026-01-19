#Python List
mylist=["apple","kiwi","cherry"]
print(mylist)
#creating s list:
#>using square brackets-
a=[1,2,3]
b=["apple","cherry"]
print(a,b)
#>using list() buitl-in function-
c=list((1,3,4))
print(a)
d=list("hello")
print(d)
#>creating list with repeated elemets
list1=[2]*5
list2=["hi"]*4
print(list1)
print(list2)
#we use len() function to find legth of the list
print(len(a))
print(len(b))
#A list can be empty or it may have different data type items.
empty_list1=list()
empty_list2=[]
lst=[1,2,"helo",3.45,10+6j,True]
print(empty_list1)
print(empty_list2)
print(lst)
print(len(empty_list1))
print(len(empty_list2))
#Accesing list elements-
#List items are indexed and you can access them by referring to the index number:
a=[10,20,30,40]
print(a[0])#poistive indexing
print(a[-1])#negative indexing
#unpacking list items-
list3=["item1","item2","item3","item4","item5"]
x,y,z,*rest=list3
print(x)
print(y)
print(z)
print(rest)
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *remaining = fruits 
print(first_fruit)     
print(second_fruit)   
print(third_fruit)     
print(remaining) 
#allow duplicate values-
list4=["apple","kiwi","banana","kiwi"] 
print(list4)   
#getting type
print(type(list4))
#slicing items from a list-
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
print(fruits[0:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[:-2])
print(fruits[::-1])
#modifying list-
#List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
fruits[0]="avocado"
fruits[3]="guava"
print(fruits)
print(fruits)
#chech if item exists-
#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

