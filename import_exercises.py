# Import Exercises

# 1. Import and test 3 of the functions from your functions exercise file. 
#    Import each function in a different way:

#    a. Run an interactive python session and import the module. 
#       Call the is_vowel function using the . syntax.

from function_exercises import is_vowel

print(is_vowel("a"))

#    b. Create a file named import_exericses.py. 
#       Within this file, use from to import the calculate_tip function directly. 
#       Call this function with values you choose and print the result.

from function_exercises import get_letter_grade

print(get_letter_grade(99))

#    c. Create a jupyter notebook named import_exercises.ipynb. 
#       Use from to import the get_letter_grade function and give it an alias. 
#       Test this function in your notebook.

# ** Complete **




# 2. Read about and use the itertools module from the python 
#    standard library to help you solve the following problems:

#       a. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product
print(list(product('ABC', [1, 2, 3])))
len(list(product('ABC', [1, 2, 3])))

#       b. How many different combinations are there of 2 letters from "abcd"?

from itertools import combinations
print(list(combinations('ABCD', 2)))
len(list(combinations('ABCD', 2)))

#       c. How many different permutations are there of 2 letters from "abcd"?

from itertools import permutations
print(list(permutations('ABCD', 2)))
len(list(permutations('ABCD', 2)))


# 3. Save this file as profiles.json inside of your exercises directory 
#    (right click -> save file as...). 
#    Use the load function from the json module to open this file.

import json # Initialization

profiles = list(json.load(open('profiles.json'))) 

#   a. Total number of users
print("Number of users:")
print(len(profiles)) # Total number of users is 19

#   b. Number of active users
def number_active_users():
    i = 0
    for profile in profiles:
        if profile["isActive"] == True:
            i += 1
    return i

print("Number of active users:")
print(number_active_users()) # Number of active users: 9

#   c. Number of inactive users

def number_inactive_users():
    i = 0
    for profile in profiles:
        if profile["isActive"] == False:
            i += 1
    return i

print("Number of inactive users:")
print(number_inactive_users()) # Number of inactive users: 10

#   d. Grand total of balances for all users

def sum_balances():
    total = 0 # initialize total
    for profile in profiles:
        # print("User balance:", profile["balance"]) # Used to check balances if needed
        temp_balance = profile["balance"] # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "") # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "") #Removes $ from the string
        total += float(remove_dollar_sign_balance) # Adds all balances in list
    return total

print("Total balances for all users:")
print("$", sum_balances()) # Result: $ 52667.02

#   e. Average balance per user

def avg_balance():
    i = 0
    total = 0 # initialize total
    for profile in profiles:
        # print("User balance:", profile["balance"]) # Used to check balances if needed
        temp_balance = profile["balance"] # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "") # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "") #Removes $ from the string
        total += float(remove_dollar_sign_balance) # Adds all balances in list
        i += 1 # 19 balances
    #print("len(profiles:", len(profiles)) # Test to see if lenth == i
    #print("Total:", total) # Test for total
    #print("i:", i ) # Test for i
    return round(total / i, 2)

print("Average balance for all users:")
print("$", avg_balance()) # Result: $ 2771.95


#   f. User with the lowest balance

def lowest_balance():
    lowest_balance = float("inf")
    for profile in profiles:
        temp_balance = profile["balance"] # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "") # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "") #Removes $ from the string
        numeric_balance = float(remove_dollar_sign_balance) # transforms the balance into float type
        if numeric_balance < lowest_balance:
            lowest_balance = numeric_balance
    return round(lowest_balance, 2)

print("Lowest balance:")
print("$", lowest_balance())

#   g. User with the highest balance

def highest_balance():
    highest_balance = float("-inf")
    for profile in profiles:
        temp_balance = profile["balance"] # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "") # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "") #Removes $ from the string
        numeric_balance = float(remove_dollar_sign_balance) # transforms the balance into float type
        if numeric_balance > highest_balance:
            highest_balance = numeric_balance
    return round(highest_balance, 2)

print("Highest balance:")
print("$", highest_balance())

#   h. Most common favorite fruit

def favorite_fruit():
    highest_fruit = ""
    highest_count = 0
    for profile in profiles:
        fruit_counter = profile["favoriteFruit"]
        fruit_count = 0
        for compare in profiles:
            if fruit_counter == compare["favoriteFruit"]:
                fruit_count += 1
        if fruit_count > highest_count:
            highest_count = fruit_count
            highest_fruit = fruit_counter
    return highest_fruit

print("Most common favorite fruit")
print(favorite_fruit())

#   i. Least most common favorite fruit

def least_favorite_fruit():
    highest_fruit = ""
    highest_count = 0
    for profile in profiles:
        fruit_counter = profile["favoriteFruit"]
        fruit_count = 0
        for compare in profiles:
            if fruit_counter == compare["favoriteFruit"]:
                fruit_count += 1
        if fruit_count > highest_count:
            highest_count = fruit_count
            highest_fruit = fruit_counter
    return highest_fruit

print("Most common favorite fruit")
print(least_favorite_fruit())

#   j. Total number of unread messages for all users

def total_unread_messages():
    for profile in profiles:
        greeting = profile["greeting"]
        num_messages = ""
        for number in greeting:
            if number.isdigit:
                num_messages.append(number)
        