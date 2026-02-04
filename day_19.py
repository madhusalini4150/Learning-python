#For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
colors=["blue","white","pink","yellow"]
for i in colors:
    print(i)
#The for loop does not require an indexing variable to set beforehand.
#-----------------------------------------------------------------------------------------------------------------------------------
#Looping Through a String- strings are iterable objects, they contain a sequence of characters
for x in "paris":
    print(x)
#Looping through a Tuple-
nums=(1,2,3,4,5)
for x in nums:
    print(x)
#Looping through a dictionary-For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
child={
    "name":"tom",
    "age":11,
    "weight":34
}
for key in child:
    print(key)
for key,values in child.items():
    print(key,values)# this way we get both keys and values printed out
#Looping through a set-
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#for loop with condition-
numbers=[10,20,30,40,50,60]
for num in numbers:
    if num>40:
        print(num)
#------------------------------------------------------------------------------------------------------------------------------------------------
#Break Statement-With the break statement we can stop the loop before it has looped through all the items:
fruits=["apple","cherry","banana","mango","kiwi","guava"]
for i in fruits:
    print(i)
    if i=="mango":
        break
#Exit the loop when x is "banana", but this time the break comes before the print:
for i in fruits:
    if i=="mango":
        break
    print(i)
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Continue Statement-With the continue statement we can stop the current iteration of the loop, and continue with the next:
for i in fruits:
    if i=="banana":
        continue
    print(i)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#range() function-To loop through a set of code a specified number of times, we can use the range() function,The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(10): #Note that range(6) is not the values of 0 to 10, but the values 0 to 9.
    print(x)
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
for x in range(2,6): #range(2, 6), which means values from 2 to 6 (but not including 6)
    print(x)
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2,20,4):
    print(x)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Iterating by Index of Sequences
#We can also use the index of elements in the sequence to iterate. The key idea is to first calculate the length of the list and then iterate over the sequence within the range of this length.
mylist=["name","age","color","weight","height"]
for i in range(len(mylist)):
    print(mylist[i])
#The range(len(list)) generates indices from 0 to the length of the list minus 1.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Else in for loop:The else keyword in a for loop specifies a block of code to be executed when the loop is finished
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for i in range(10):
    print(i)
else:
    print("loop ended")
#The else block will NOT be executed if the loop is stopped by a break statement.
for i in range(6):
    if i==3:
        break
    print(i)
else:
    print("loop ended")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pass statement-for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in [1,2,3]:
    pass
