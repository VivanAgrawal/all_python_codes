
#The Python Match Statement
#Instead of writing many if..else statements, you can use the match statement.

#The match statement selects one of many code blocks to be executed

'''Syntax:
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block'''

#The match expression is evaluated once.
#The value of the expression is compared with the values of each case.
#If there is a match, the associated block of code is executed.
#The example below uses the weekday number to print the weekday name
#eg1:
day = 4
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
    print("Saturday")
  case 7:
    print("Sunday")
    
#eg2:
temp = int(input("Enter temperature in °C: "))

match temp:
    case t if t > 40:
        print("🔥 Very Hot")
    case t if 30 <= t <= 40:
        print("☀ Hot")
    case t if 20 <= t < 30:
        print("🌤 Warm")
    case t if 10 <= t < 20:
        print("🌥 Cool")
    case _:
        print("❄ Very Cold")
      
#eg3:
marks = int(input("Enter marks (0-100): "))
match marks:
    case m if m >= 90:
        print("Grade: A")
    case m if m >= 75:
        print("Grade: B")
    case m if m >= 60:
        print("Grade: C")
    case m if m >= 40:
        print("Grade: D")
    case m if m < 40:
        print("Grade: F")
    case _:
        print("Invalid input")