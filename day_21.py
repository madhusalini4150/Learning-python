#printing patterns
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
#printing numbers pattern
for i in range(rows):
    for j in range(i+1):
        print(i,end=" ")
    print(" ")
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()


       
