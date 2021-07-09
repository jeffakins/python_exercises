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
#       - the hourly rate
#       - how much the week's paycheck will be
#       - write the python code that calculates the weekly paycheck. 
#         You get paid time and a half if you work more than 40 hours