#python loops
i=0 
while i<5:
    i+=1
    print(i)
#priniting patter
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()
#printing above pattern in reverse order
print("pattern reversing")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#printing numbers patter 
for i in range(rows):
    for j in range(i+1):
        print(i,end=" ")
    print(" ")


       
