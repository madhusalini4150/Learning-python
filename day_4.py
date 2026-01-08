#STRINGS
print("hey hello 'madhu'")
print('hey hello "divya" ')
print("it's ok")
#---------multiple line string assinging
a='''heyuikjhgfdcvb
iuyfvghjnbvgyu
iuytfghjk'''
print(a)
b="""hjiuyfghjuy
ytdfghjkjh
iytfvbj"""
print(b)
#----------------------------
a="hello world"
print(a[1])
print("hello"[3])
#------------------------
for i in "banana":
    print(i)
#----------------------
a="madhu divya"
print(len(a))
#====================check string
txt="The best things in life are free!"
print("free" in txt)
#--------------using if statement
txt="The best things in life are free!"
if "free" in txt:
    print("yes")
#----------------check not in
txt="The best things in life are free!"
print("expresive" not in txt)
#----------using if
txt="The best things in life are free!"
if "express" not in txt:
    print("yes")
#to concatenate,or combine to strings we can use + operator
a="hello"
b="world"
print(a+b)
print(a+" "+b)
print(a+"-"+b)
#ESCAPE CHARACTERS
# \"" or \''
print("we are \"indians\".")
print('we are \'indians\'.')
# if we want print we are "indians". there is another way without escape characters
print("we are 'indians'.") # or print('we are "indians".')
#---------------------------------------------------------
#\\
print("this will inser one \\ (backslsh)")
#---------------------------------------------------------
#\n-new line
print("japan\nindia")
#---------------------------------------------------------
#\r-carriage return
print("hello\rworld")
print("apple\rkiwi")
print("1234\rA")
#--------------------------------------------------------
#\t-tab
print("good\tmorning")
#---------------------------------------------------------
#\b-backspace(it erases one character)
print("hey  \bhow are you?")
#--------------------------------------------------------
#\f(form feed)-different environments treats it differently some show it as space,new line,page break
print("hello\fworld")
#---------------------------------------------------------
#more escape characters are there like \u-unicode escape sequence,\ooo-octsl value,\xhh-hex value
#Slicing
a="hello world"
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])
print(a[::2])
print(a[::-1])
#we can not combine strings and numbers by using '+' operator
'''age= 39
   txt="my name is jhon,I am "+age
   print(txt)
   -------it gives error'''
   #------------------------------------
#we comine strings and numbers by using f-strings or the format() method
#f-strings
age=36
txt=f"My name is jhon,I am {age}"
print(txt)
#----------------------------------------
#add a placeholder for the price variable
price=59
txt=f"the price is {price} dollars"
print(txt)
#----------------------------------------
#place holder can include a modifier to format the value
#   a modifier is included by adding a colon: followed by a legal formatting type
price=48
txt=f"the price is {price:.3f} dollars"
print(txt)
#----------------------------
colors="blue,pink,red"
txt=f"i have colors like {colors}"
print(txt)
#------------------------------------
#a place holder can contain python code like math operations
line=f"the price is {20*56} dollars"
print(line)
#-------------------------------
a = 10
b = 5
print(f"Sum is {a + b}")
print(f"Product is {a * b}")
#-------------------------------
price = 250
quantity = 4
print(f"Total amount = {price * quantity} rupees")
#---------------------------------
name=input("enter your name:")
print(f"hello {name}")
#----------------------------------
x = 10
y = 20
print(f"x={x}, y={y}")
#To modify strings we have some methods
#-------Upper()
a="Setty srdivya"
print(a.upper())
print("madhu".upper())
#--------lower()
print(a.lower())
#--------strip()=removes whitespaces from the strt and end
c='    hey how are you   '
print(c.strip())
b='*  hey how are you    *'
print(b.strip("*"))
print(b.lstrip("*"))
print(b.rstrip("*"))
#--------------------replace string
txt="balckpink"
print(txt.replace("pink"," and white"))
#------------------split string
txt="welocme to the derry"
print(txt.split())
print(txt.split(" "))
txt1="penny/wise"
print(txt1.split("/"))
txt2="it-st"
print(txt2.split("-"))
sen="   hi  "
print(sen.split())
list='a,,c,d'
print(list.split(","))
#STRING METHODS
#All string methods return new values. They do not change the original string.
#---------------------------------------------------------
#capitalize()-converts first chacracter to upper case
name="larA willIam"
print(name.capitalize())
#--------------------------------------------------------
#casefold()-converts string into lower case,it is similar to lower() but it is more better than lower() when comparison
print(name.casefold())
#---------------------------------------------------------
#center()-returns a centerd string
print(name.center(20))
print(name.center(20,"*"))
#----------------------------------------------------------
#count()-returns the no of times a specific value occurs in a string
print(name.count("l"))
print(name.count("l",4,9))#l-value,4-start,9-end
#-----------------------------------------------------------
#endswith()-returns true if the string ends with the specified value
print(name.endswith("m"))
print(name.endswith("w"))
#startswith()-Returns true if the string starts with the specified value
print(name.startswith("l"))
#-----------------------------------------------------------
#expandtabs()-sets the tab size of the string
txt1="hello\thi"
print(txt1.expandtabs(5))
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
#------------------------------------------------------------
#find()-Searches the string for a specified value and returns the position of where it was found,it returns -1 when the value not found
#searches from left to right
print(name.find("ll"))
print(name.find("a"))
#rfind()-searches from right to left,but gives index as given like left to right index
print(name.rfind("a"))
#------------------------------------------------------------
#formaat()-Formats specified values in a string
text="the price is {price:.2f} rupees"
print(text.format(price=48))
 #or
print("the price is {price:.2f} rupees".format(price=48))
text1="my name is {name} and age is {age}"
print(text1.format(name="madhu",age=19))
print("my name is {} and age is {}".format("madhu",19))
txt2 = "My name is {0}, I'm {1}".format("John",36)#0,1 are indexes if we give 0,2 it gives error i.e 0,1 matches jhon,36
print(txt2)
#--------------------------------------------------------------
#index-Searches the string for a specified value and returns the position of where it was found,first occurrence,it returns error if the value not found
print(name.index("a"))
print(name.index("l",0,4))
#rindex()-Searches the string for a specified value and returns the last position of where it was found
print(name.rindex("a"))
#--------------------------------------------------------------
#isalnum()-The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(name.isalnum())#it returs error becoz in 'LarA willIam' space is there,space is non alaphanumeric
#isalpha()-The isalpha() method returns True if all the characters are alphabet letters (a-z)
print(name.isalpha())#space is non alphabte letter
#isascii()-The isascii() method returns True if all the characters are ascii characters  
print(name.isascii())
#isdecimal()-The isdecimal() method returns True if all the characters are decimals (0-9)
print(name.isdecimal())
#isdigit()-Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print(name.isdigit())
#isidentifier()-Checks for a valid identifier - it checks if a string is a valid variable name
print(name.isidentifier())
#isnumeric()-Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)(-1,0.5 like this returns false)
print(name.isnumeric())
#islower()-Returns True if all characters in the string are lower case
print(name.islower())
#isupper()-Returns True if all characters in the string are upper case
print(name.isupper())
#isprintable()-Returns True if all characters in the string are printable,carriage return and form feed sre non printable
print(name.isprintable())
#isspace()-Returns True if all characters in the string are whitespaces
print(name.isspace())
#------------------------------------------------------------------------------------------------------------------------
#lower()-Converts a string into lower case
print(name.lower())
#upper()-Converts a string into upper case
print(name.upper())
#-----------------------------------------------------------------------------------------
#title()-Converts the first character of each word to upper case
print(name.title())
#istitle()-Returns True if the string follows the rules of a title
print(name.istitle())
#--------------------------------------------------------------------------------------
#replace()-Returns a string where a specified value is replaced with a specified value
print(name.replace("will","max"))
print(name.replace("l","h",2))
#-------------------------------------------------------------------------------------
#join()-Converts the elements of an iterable into a string
fruits=('apple','mango','kiwi')
print("$".join(fruits))
print("-".join(fruits))
#When using a dictionary as an iterable, the returned values are the keys, not the values.
mydict={"name":"jhon","age":23}
print("man".join(mydict))
#-------------------------------------------------------------------------------------
#strip()-The strip() method removes any leading, and trailing whitespaces.
#>Leading means at the beginning of the string, trailing means at the end.
#>You can specify which character(s) to remove, if not, any whitespaces will be removed.
text=".....,.,happy,.,."
print(text.strip(",."))
print(text.strip("."))
#rstrip()-Returns a right trim version of the string
print(text.rstrip(".,"))
#lstrip()-Returns a left trim version of the string
print(text.lstrip(".,"))
#------------------------------------------------------------------------------------------
#swapcase()-Swaps cases, lower case becomes upper case and vice versa
print(name.swapcase())
#-------------------------------------------------------------------------------------------
#The partition() -method searches for a specified string, and splits the string into a tuple containing three elements.
#>The first element contains the part before the specified string.
#>The second element contains the specified string.
#>The third element contains the part after the string
#>This method searches for the "first occurrence" of the specified string
print(name.partition("l"))
#rpartition()-The rpartition() method searches for the last occurrence of a specified string
print(name.rpartition("l"))
#----------------------------------------------------------------------------------------------
#split()-The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.
print(name.split(" "))
print(text.split("."))
#>When maxsplit is specified, the list will contain the specified number of elements plus one.
print(name.split("l",1))
#>rsplit()-The rsplit() method splits a string into a list, starting from the right.If no "max" is specified, this method will return the same as the split() method
print(name.rsplit(" "))
print(name.rsplit("l",1))