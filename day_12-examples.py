#Create a tuple with 5 different data types and print it.
mytuple=("lion",True,78,3.45,[1,2,3])
print(mytuple)
#Create a tuple with only one element. What mistake should you avoid?
mytuple=("lion",)
print(mytuple)
#Convert a list [10, 20, 30] into a tuple.
mylist=[10,20,30]
print(mylist)
mytuple=tuple(mylist)
print(mytuple)
#Given t = (5, 10, 15, 20, 25),Print the first element,Print the last element,Print the middle element
t=(5,10,15,20,25)
first_ele=t[0]
last_ele=t[-1]
middle_ele=t[len(t)//2]
print(first_ele,last_ele,middle_ele)
#Access elements from index 1 to 3 using slicing.
print(t[1:4])
#Print every alternate element from a tuple.
print(t[0::2])
#Given t = (1, 2, 3),Add element 4 to the tuple.
t=(1,2,3)
t1=(4,)
T=t+t1
print(T)
#or
T=t+(4,)
print(T)
#Remove element 20 from tuple (10, 20, 30, 40).
tup=(10,20,30,40)
lst=list(tup)
lst.remove(20)
tup=tuple(lst)
print(tup)
#Replace element 100 with 500 in tuple (50, 100, 150).
tup=(50,100,150)
mylist=list(tup)
mylist[mylist.index(100)]=500
tup=tuple(mylist)
print(tup)
#Unpack tuple (10, 20, 30) into three variables and print them.
mytuple=(10,20,30)
x,y,z=mytuple
print(x,y,z)
#Unpack only the first two values from (1, 2, 3, 4, 5) using *.
mytuple=(1,2,3,4,5)
a,b,*c=mytuple
print(a,b,*c)
#Print all elements of a tuple using a for loop.
for i in mytuple:
  print(i)
#Print all elements of a tuple using a for loop.
for i in mytuple:
  print(i)
#Print tuple elements along with their index.
for x in range(len(mytuple)):
  print(x,mytuple[x])
#or
for index,value in enumerate(mytuple):
  print(index,value)
#Count how many times 5 appears in (5, 1, 5, 2, 5, 3) using a loop.
tup=(5,1,5,2,5,3)
print(tup.count(5))
#or
count=0
for x in tup:
  if x==5:
    count+=1
print(count)
#Join two tuples (1, 2, 3) and (4, 5, 6).
tup1=(1,2,3)
tup2=(4,5,6)
TUP=tup1+tup2
print(TUP)
#Repeat a tuple (10, 20) three times.
tup=(10,20)
print(tup*3)
#Join multiple tuples stored in a list.
tuple_list=[(1,2),(3,4),(5,6)]
res=()
for i in tuple_list:
  res=res+i
print(res)
#Find the index of element 50 in (10, 20, 50, 40).
tupl=(10,20,50,40)
print(tupl.index(50))
#What happens if you try to find the index of an element not present?
t=(10,20,30)
if 50 in t:
  print(t.index[50])
else:
  print("Element not found")