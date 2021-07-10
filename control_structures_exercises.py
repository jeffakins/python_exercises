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
