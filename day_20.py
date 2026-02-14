#Nested Loops:
#Nested While loops-A nested while loop in Python is a while loop placed inside the body of another while loop
list1=[1,2,3]
list2=[4,5,6]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        print(list1[i],list2[j])
        j+=1
    print()
    i+=1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nested For loops-A nested for loop in Python is a for loop placed inside the body of another for loop
for x in range(3):
    for y in range(1,10):
        print(y,end=" ")
    print()
 

rows=int(input("Enter the no.of rows:"))
columns=int(input("Enter the no.of columns:"))
symbol=input("Enter a symbol to use:")
for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()


for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f"{x},{y},{z}")

        
colors=['red','blue','green']
sizes=['L','M','S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
