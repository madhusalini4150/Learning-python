#WHILE LOOP-With the while loop we can execute a set of statements as long as a condition is true.
i=1
while i<6:
    print(i)
    i+=1
#infinite while loop-Code given below uses a 'while' loop with the condition "True", which means that the loop will run infinitely until we break out of it using "break" keyword or some other logic.
'''while(True):
    print("hello")
    #It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition is always true and we have to forcefully terminate the compiler.'''
#Break statement-With the break statement we can stop the loop even if the while condition is true:
i=0
while i <6:
    print(i)
    if i == 3:
        break
    i+=1
#continue statement-With the continue statement we can stop the current iteration, and continue with the next:
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
#With the else statement we can run a block of code once when the condition no longer is true
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
#---------------------------------------------
i=1
n=int(input("enter number:"))
while i<=n:
    print(i,end="\n")
    i+=1
#-----------------------------------------------
#Fibnocci Series-
n=int(input("enter n:"))
a,b=0,1
print(a,end="\n")
while n>1:
    print(b,end="\n")
    a,b=b,a+b
    n-=1
#----------------------------------------------
#To find nth fibnocci number-
n=int(input("enter n:"))
a,b=0,1
while n>1:
    a,b=b,a+b
    n-=1
print(a)



