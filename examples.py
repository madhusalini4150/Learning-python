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
