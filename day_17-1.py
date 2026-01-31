#IF STATEMENT:
# An "if statement" is written by using the if keyword.
#The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
a=210
b=34
if a>b:
    print("a is greater")
#You can have multiple statements inside an if block. All statements must be indented at the same level.
age=20
if age>18:
    print("you are an adult")
    print("you can vote")
    print("you have full legal rights")
#using variables in conditions-Boolean variables can be used directly in if statements without comparison operators.
color=True
if color:
    print("pink")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#IF ELSE STATEMENT:
#If condition is true the first block will be executed, if not the else condition will run.
a=45
b=41
if a>b:
    print("a is bigger")
else:
    print("b is bigger")
# The else statement must come last. You cannot have an elif after an else.
#-----------------------------------------------------------------------------------------------------------------------------------------
#ELIF STATEMENT:
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition",The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
a=34
b=35
if a>b:
    print("a is bigger")
elif a<b:
    print("b is bigger")
#ou can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true
marks=80
if marks>=70:
    print("B grade")
elif marks>=80:
    print("A grade")
elif marks>=90:
    print("A+ grade")
elif marks>=60:
    print("just pass")
else:
    print("Fail")
#Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
#When to Use Elif-Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
day=4
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thrusday")
elif day==5:
    print("Friday")
elif day==6:
    print("Satuarday")
elif day==7:
    print("Sunday")
#----------------------------------------------------------------------------------------------------------
#Shorthand if-If you have only one statement to execute, you can put it on the same line as the if statement.
a=3
b=8
if a!=b: print("True")
#This is a compact way to write an if statement. It executes print statement if the condition is true.
#---------------------------------------------------------------------------------------------------------------------
#Shorthand if else-If you have one statement for if and one for else, you can put them on the same line using a conditional expression
a="divya"
b="madhu"
print("same name") if a==b else print("No")
#This is called a conditional expression (sometimes known as a "ternary operator").
#You can also use a one-line if/else to choose a value and assign it to a variable:
a=10
b=20
bigger=a if a >b else b
print("bigger is:",bigger)
#Multiple Conditions on One Line
#You can chain conditional expressions, but keep it short so it stays readable:
#one-line if-elif-else (ternary operator)
a=330
b=330
print("A") if a>b else print("=") if a==b else print("B")
#or
if a>b:
    print("A")
elif a==b:
    print("=")
else:
    print("B")
#-----------------------------------------------------------------------------------------------------------------------------------
#Practical Examples-Ternary operators are particularly useful for simple assignments and return statements.
#Finding the maximum of two numbers:
x=23
y=56
max=x if x>y else y
print("max value is:",max)
#Setting a default value:
username=""
display_name=username if username else "Guest"
print("Welcome,",display_name)
#---------------------------------------------------------------------------------------------------------------------------------------
#Logical Operators-Logical operators are used to combine conditional statements. Python has three logical operators
#and-The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
a=400
b=33
c=340
if a>b and a>c:
    print("a is bigger")
#or-The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
if a>b or a==c:
    print("a is big")
#not-The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
if not a==b:
    print("a is not eual to b")
#Combining Multiple Operators-You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or
age=25
num=34
if (age>18 or age<18) and (num<40 or num>40):
    print("Conditions are true")
#More Examples-
#User authentication check:
username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
#Range checking with logical operators:
score = 85
if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
#----------------------------------------------------------------------------------------------------
#Nested if Statements-You can have if statements inside if statements. This is called nested if statements
x=30
if x>20:
    print("above 20,")
    if x>40:
        print("and also above 30")
    else:
        print("but not above 40")
#In this example, the inner if statement only runs if the outer condition (x > 20) is true.
#Checking multiple conditions with nesting:
age=23
has_license=True
if age>=18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#-----------------------------------------------------------------------------------------------------------------------------------
