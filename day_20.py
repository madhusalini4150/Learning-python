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
row=int(input("enter your no.of rows:"))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



       
