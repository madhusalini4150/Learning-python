#Create a list of 5 mobile prices.Print the list,Print the first and last price
prices=[12000,30000,14000,50000,20000]
print(prices)
first_price=prices[0]
print(first_price)
last_price=len(prices)-1
last_price=prices[last_price]
print(last_price)
#A list contains student marks:marks = [45, 78, 62, 90, 55],Find total marks,Find average marks
list1=[45,78,62,90,55]
total=sum(list1)
avg=total/len(list1)
print(total)
print(avg)
#Create a list of city names.Check whether "Hyderabad" is present in the list
cities=["banglore","chennai","hyderabad","mumbai","delhi"]
if "hyderabad" in cities:
  print("yes")
else:
  print("no")
  #Given a list:nums = [10, 20, 30, 40, 50],Change the value 30 to 35
list2=[10,20,30,40,50]
print(list2)
list2[2]=35
print(list2)
#or
index=list2.index(40)
list2[index]=45
print(list2)
#Given:fruits = ["apple", "banana", "mango"],Add "orange" at the end,Add "grapes" at index 1
fruits=["apple","banana","mango"]
fruits.append("orange")
print(fruits)
fruits.insert(1,"grapes")
print(fruits)
#Given:numbers = [1, 2, 3],Add all elements of [4, 5, 6] using a list method
numbers=[1,2,3]
numbers.extend([4,5,6])
print(numbers)
#Given:items = ["pen", "pencil", "eraser", "scale"],Remove "eraser",Remove the last item
items=["pen","pencil","eraser","scale"]
items.remove("eraser")
print(items)
items.pop()#by default it removes last element
print(items)
items.pop(len(items)-1)
print(items)
#Given:values = [5, 2, 9, 1, 7],Sort the list,Reverse the list
values=[5,2,9,1,7]
print(values)
values.sort()
print(values)
values.sort(reverse=True)
print(values)
values.reverse()
print(values)
#Print all elements in this list using a for loop:
languages = ["Python", "Java", "C", "JavaScript"]
for i in languages:
  print(i)
  #Print only even numbers from this list:
nums = [10, 15, 20, 25, 30, 35]
for num in nums:
  if num%2==0:
     print(num)
#Count how many elements are greater than 50:
scores = [45, 67, 89, 32, 56, 90, 48]
count=0
for i in scores:
    if i>50:
      count+=1
print(count)
#Find the largest number in a list without using max()
largest=scores[0]
for num in scores:
  if num>largest:
    largest=num
print(largest)