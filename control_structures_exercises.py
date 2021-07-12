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



# For Loops

# - Write some code that prompts the user for a number, 
#   then shows a multiplication table up through 10 for that number.
print("Enter a number to show its multiplication table")
number = int(input())
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# - Output number of number
for i in range(1, 10):
    number = str(i)
    print(number * i)


# break and continue

# - Prompt the user for an odd number between 1 and 50. 
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
