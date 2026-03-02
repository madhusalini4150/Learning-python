#printing patterns-
#print a solid square star pattern for a given number n
n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#--------------------------------------------------------------------------------------
#printing right angle triangle:   
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()
#----------------------------------------------------------------------------------------
#printing above pattern in reverse order(reverse right angle triangle)
print("pattern reversing")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
     #or
n=int(input("enter n:"))
for i in range(n):
    for j in range(i,n):
        print('*',end=" ")
    print()
#------------------------------------------------------------------------------------------------
#printing numbers pattern
for i in range(rows):
    for j in range(i+1):
        print(i,end=" ")
    print(" ")
#-------------------------------------------------------------------------------------------------
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()
    


       
