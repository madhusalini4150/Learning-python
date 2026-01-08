#Take two strings and join them with a space in between
str1=input("enter first string:")
str2=input("enter second string")
print(" ".join([str1,str2]))
 #OR
result=str1+" "+str2
print(result)
#Concatenate your first name and last name and print the full name.
first_name=input("enter your first name:")
last_name=input("enter your second name:")
full_name=first_name+" "+last_name
print(full_name)
#Print the string "Python" 5 times using an operator
print("python "*5)
#Join a string and a number (hint: type conversion required)
text=input('enter string:')
num=int(input("enter number:"))
print(f"{text}} {num}")
#Format the value of price = 49.5678 to 2 decimal places
price=49.5678
print("{:.2f}".format(price))
print(f"{price:.2f}")
#Given text = "Programming",Print first 5 characters,Print last 3 characters
text1="Programming"
print(text[0:5])
print(text[-3:])
#Reverse the string "Python" using slicing
text2="python"
print(text[::-1])
#Print every second character from "Computer"
text3="computer"
print(text3[0::2])
#Convert "python programming" into:Uppercase,Title case
text4="Python programming"
print(text4.upper())
print(text4.title())
#Remove extra spaces from " Hello World "
text5=" Hello World "
print(text5.strip(" "))
#or
print(text5.replace(" ",""))
#Replace "Java" with "Python" in the string "I like Java"
text6="I like Java"
print(text6.replace("Java","Python"))
#Count how many times 'a' occurs in "banana"
txt="banana"
print(txt.count("a"))
#Check whether "Python123" contains only letters.
#Check whether "12345" contains only digits
print("python123".isalpha())
print("12345".isdigit())
#Split the string "Python is very easy" into a list.
print("Python is very easy".split(" "))
#Join the list ["Learn", "Python", "Now"] into a single string with spaces
txt=["Learn", "Python", "Now"]
print(" ".join(txt))
#Input a string and check whether it starts with "Py"
print(input('enter string:').startswith("py"))
