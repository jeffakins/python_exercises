# Python Control Structures Exercises
#1. Conditional Basics
# a. prompt the user for a day of the week, 
#    print out whether the day is Monday or not

print("What day of the week is it? ")
day_of_week = input()
if day_of_week == "monday" or day_of_week == "Monday":
    print("It's a Monday :(")
else:
    print("It's not a Monday :)")

# b. prompt the user for a day of the week, 
#    print out whether the day is a weekday or a weekend

weekend_days = ["saturday", "Saturday", "sunday", "Sunday"]

print("What day of the week is it? ")
day_of_week = input()
for day in weekend_days:
    if day == day_of_week:
        print("Yay, it's the weekend!!")
print("The day of the week is", day_of_week)
    

# c. create variables and make up values for
#       - the number of hours worked in one week
weekly_work_hours = 40
#       - the hourly rate
hourly_rate = pay / pay_period_hours
#       - how much the week's paycheck will be
weekly_paycheck = hourly_rate * weekly_work_hours
#       - write the python code that calculates the weekly paycheck. 
weekly_paycheck = hourly_rate * weekly_work_hours
#         You get paid time and a half if you work more than 40 hours
if weekly_work_hours > 40:
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    return overtime_pay


# 2. Loop Basics
#   a. While Loop
#   - Create an integer variable i with a value of 5.
i = 5
#   - Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    i += 1
#   - Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1


#   - Create a while loop that will count by 2's starting with 0 and ending at 100. 
#     Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
#   - Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5
#   - Create a while loop that starts at 2, 
#     and displays the number squared on each line while the number is less than 1,000,000. 
i = 2
while i <= 100000:
    print(i)
    i = i ** 2

#   - From 100 subtract by 5 until 0
i = 100
while i >= 0:
    print(i)
    i -= 5



# b. For Loops

# - 1. Write some code that prompts the user for a number, 
#   then shows a multiplication table up through 10 for that number.
print("Enter a number to show its multiplication table")
number = int(input())
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# - 2. Output number of number
for i in range(1, 10):
    number = str(i)
    print(number * i)


# c. break and continue

# - 1. Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting 
# the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.
print("Enter an odd integer between 1 and 50")
number = input()
if number.isdigit() == True and int(number) % 2 != 0 and int(number) > 0 and int(number) < 50:
    for i in range (1, 50):
        if i % 2 != 0:
            if int(number) == i:
                print("Yikes, skip number", number)
                continue
            print("Here is an odd number:", i)
else:
    print("That is not an odd number between 1 and 50")


# d. The input function can be used to prompt for input and use that input in your python code. 
#    Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#    (Hints: first make sure that the value the user entered is a valid number, also note that 
#    the input function returns a string, so you'll need to convert this to a numeric type.)

print("Enter a positive integer")
number = input()
i = 0 # to initialize i
if number.isdigit() == True and int(number) > 0: # to check that the input is a pos number
    print("I will count to your number...")
    while i <= int(number):
        print(i)
        i += 1
else:
    print("That is not a positive integer")

# e. Write a program that prompts the user for a positive integer. 
#    Next write a loop that prints out the numbers from the number the user entered down to 1.

print("Enter a positive integer")
number = input()
i = int(number) # to initialize i
if number.isdigit() == True and int(number) > 0: # to check that the input is a pos number
    print("I will count from your number to 1...")
    while i > 0:
        print(i)
        i -= 1
else:
    print("That is not a positive integer")


# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# Write a program that prints the numbers from 1 to 100.

i = 1
while i <= 100:
    print(i)
    i += 1

# For multiples of three print "Fizz" instead of the number

i = 1
while i <= 100:
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1

# For the multiples of five print "Buzz"

i = 1
while i <= 100:
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# For numbers which are multiples of both three and five print "FizzBuzz"

i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i += 1


# 4. Display a table of powers.

#    Prompt the user to enter an integer.
#    Display a table of squares and cubes from 1 to the value entered.
#    Ask if the user wants to continue.
#    Assume that the user will enter valid data.
#    Only continue if the user agrees to.

print("Enter a number to be sqaured and cubed")
number = input()
def square(x):
    return x * x
def cube(x):
    return x * x * x

print("Here is your table")
print("number", "squared", "cubed")
for i in range(1, number):
    print(number, square(number), cube(number))