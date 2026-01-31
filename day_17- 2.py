#Pass Statement-if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a=23
b=45
if a>b:
    pass
  #having an empty if statement like this, would raise an error without the pass statement
#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
#pass with Multiple Conditions,You can use pass in any branch of an if-elif-else statement.
value=40
if value<0:
    print("negative value")
elif value==0:
    pass
else:
    print("Positive number")
#While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.
#-------------------------------------------------------------------------------------------------------------------------------------------
#Match Statement-The match statement is used to perform different actions based on different conditions.
#Instead of writing many if..else statements, you can use the match statement.The match statement selects one of many code blocks to be executed
day=4
match day:
    case 1:
       print("Monday")
    case 2:
       print("Tuesday")
    case 3:
       print("Wednesday")
    case 4:
       print("Thursday")
    case 5:
       print("Friday")
    case 6:
       print("Satuarday")
    case 7:
       print("Sunday")
#Default Value-Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
day=2
match day:
   case 6:
      print("Today is Satuarday")
   case 7:
      print("Today is Sunday")
   case _:
      print("Looking forward to the Weekend")
#The value _ will always match, so it is important to place it as the last case to make it behave as a default case
#Combine Values-Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day=7
match day:
  case 1|2|3|4|5:
     print("Today is a weekday")
  case 6|7:
     print("i love weekend")
#You can add if statements in the case evaluation as an extra condition-check:
month=5
day=4
match day:
   case 1|2|3|4|5 if month==4:
      print("A weekend in april")
   case 1|2|3|4|5 if month==5:
      print("A weekend in may")
   case _:
      print("No match")
