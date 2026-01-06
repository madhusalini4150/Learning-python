#DATA TYPES
'''Text Type->str
Numeric Types->int, float, complex
Sequence Types->list, tuple, range
Mapping Type->dict
Set Types->set, frozenset
Boolean Type->bool
Binary Types->bytes, bytearray, memoryview
None Type->	NoneType'''
#int,float,complex
x=1#int()
y=2.8#float()
z=1+10j#complex()
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#-------------------------int
x=1
y=2345678987654
z=-9876543
print(x,y,z)
#taking integer as user input
number=int(input("enter number:"))
print(number)
#-------------------------float
x=1.9876
y=-198765.0987
z=1.0
print(x,y,z)
x=34e7
y=-87.1e0
print(x,y)
#taking float as user input()
number=float(input("enter number:"))
print(number)
#--------------------------complex
x=6j
y=3+7j
z=-9j
print(x,y,z)
num=complex(3,4)
num1=complex(2)
num2=complex()
print(num)
print(num1)
print(num2)
#taking float as user input()
number=complex(input("enter number:"))
print(number)
#another method
x1=float(input("enter real part:"))
x2=float(input("enter imaginary part:"))
X=complex(x1,x2)
print(X)
#-------------------------type convesion
a=1
b=2.98
c=1+8j
x=float(a)
y=int(b)
z=complex(a)
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
#--------------------------random numbers
import random
print(random.randrange(1,100))
#---------------------------random alphabets
import random
import string
print(random.choice(string.ascii_letters))
print(random.choice(string.ascii_lowercase))
#prints random words in specific range
import random
import string
word=''.join(random.choice(string.ascii_lowercase) for i in range(5))
print(word)
#random word for a specific word list
import random
words=['java','python','c++','c']
print(random.choice(words))
print(random.sample(words,1))
#random alphabet inside a specific sentence
import random
a="i love india"
print(random.choice(a))
#-----------------------------------------------------------------
#TYPE CONVERSION-converting objects from one data type to another data type
x=int(1)#int to int
y=int(2.7)#float to int
z=int("1")#str to int
print(x,y,z)
a=float(8)#int to float
b=float(2.5)#float to float
#c=float('m') Give error,float could not convert str to float
print(a,b)
l=str("m")#str to str
m=str(2)#int to str
n=str(3.5)#float to str
print(l,m,n)

