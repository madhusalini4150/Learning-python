#Write a Python program that takes item name, price, and quantity as input, calculates tax (5%), and prints the total amount.
item=input("enter item name:")
price=float(input("enter price:"))
quantity=int((input("enter quantity:")))
subtotal=price*quantity
tax=subtotal*0.05
total=subtotal+tax
print("subtotal:",subtotal)
print("tax:",tax)
print("total:",total)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a Python program to calculate age by taking birth year and current year as input./calculate current age.
year=int(input("enter your birth year:"))
current_year=int(input("enter current year:"))
age=current_year-year
print(f"you are approximately {age} years old.")
#or
import datetime
year=int(input("enter birth year:"))
current_year=datetime.date.today().year
age=current_year-year
print(age)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Currency Converter
#Write a Python program to convert an amount in USD to another currency using a fixed exchange rate.
exchange_rate=84.5#set it to a fixed number like 84.50
amount_usd=float(input("enter amount in usd:"))
convert_amount=exchange_rate*amount_usd
print(f"{amount_usd} USD is equal to {convert_amount} in Loacal Currency")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Multiplication Table
#Create a program that prints the multiplication table for a number entered by the user.
number=int(input("Enter number:"))
print("The Multiplication Table for given number:")
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
#------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3.2: The Summation
# Calculate the sum of all numbers from 1 to 100
total=0
for i in range(1,101):
    total+=i
print("The sum of all numbers from 1 to 100 is:",total)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Password Retry
# Create a loop that allows 3 attempts to enter a password
password="secret"
attempts=3
while attempts>0:
    user_password=input("Enter Password:")
    if user_password==password:
        print("Access Granted!!")
        break
    else:
        attempts-=1
        print("wrong password,attempts left:",attempts)
if attempts==0:
    print("Locked Out!!")