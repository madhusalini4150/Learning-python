#finding euclidean distance
a,b=2,3
c,d=10,8
dis=((a-c)**2+(b-d)**2)**0.5
print("euclidian distance:",dis)

   #OR
import math
a,b=2,3
c,d=10,8
dis=math.sqrt((a-c)**2+(b-d)**2)
print("euclidian distance:",dis)

   #OR
print(((2-10)**2+(3-8)**2)**0.5)
#------------------------------------
#determining type of variables
first_name="divya"
last_name="setty"
full_name="sridivya"
country="india"
city="eluru"
age=19
year=2006
is_married="no"
is_true=True
x,y,z=1,2,3
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(x,y,z)
#--------------------------
#checking length of two strings equal or not
first_name="divya"
last_name="setty"
full_name="sridivya"
print(len(first_name))
print(len(last_name))
print(len(first_name)==len(last_name))
#---------------------------
#calculating area and circumstence of circle
area_of_circle=3.14*radius**2
print(area_of_circle)
circum_of_circle=2*3.14*radius
print(circum_of_circle)
radius1=int(input("enter radius:"))
area=3.14*radius1**2
print("area of circle:",area)



