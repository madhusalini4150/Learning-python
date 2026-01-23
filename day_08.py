#Loop through a list
#for loop-You can loop through the list items by using a "for" loop:
thislist=["apple","banana","cherry"]
for i in thislist:
    print(i)
#You can also loop through the list items by referring to their index number,Use the range() and len() functions to create a suitable iterable
for i in range(len(thislist)):
    print(thislist[i])
for i in range(len(thislist)-1):
    print(thislist[i])
#while loop-Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes,Remember to increase the index by 1 after each iteration
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
#Looping using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists,A short hand for loop that will print all items in a list
[print(i) for i in thislist]
[print(x) for x in ["abc","xyz"]]
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
#Example:Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits=["apple","mango","kiwi","guava","strawberry","orange","cherry","banana"]
newlist=[x for x in fruits if "a" in x]
print(newlist)
newlist1=[x for x in fruits if x!="apple"]
print(newlist1)
list=[x for x in range(10)]
print(list)
#Same example, but with a condition:
list1=[x for x in range(20) if x<13]
print(list1)
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
newlist=[x.upper() for x in fruits]
print(newlist)
#You can set the outcome to whatever you like:
newlist=["lemon" for x in fruits]
print(newlist)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#NESTED LISTS-A nested list is a list within another list, which is useful for representing matrices or tables. We can access nested elements by chaining indexes
matrix=[[1,2,3],
       [2,3,4],
       [5,7,9]]
print(matrix)
print(matrix[1][2])
