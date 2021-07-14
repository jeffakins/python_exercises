# Import Exercises

# 1. Import and test 3 of the functions from your functions exercise file. 
#    Import each function in a different way:

#    a. Run an interactive python session and import the module. 
#       Call the is_vowel function using the . syntax.

from function_exercises import is_vowel

print(is_vowel("a"))                                # Returned True

#    b. Create a file named import_exericses.py. 
#       Within this file, use from to import the calculate_tip function directly. 
#       Call this function with values you choose and print the result.

from function_exercises import get_letter_grade

print(get_letter_grade(99))                         # Returned A

#    c. Create a jupyter notebook named import_exercises.ipynb. 
#       Use from to import the get_letter_grade function and give it an alias. 
#       Test this function in your notebook.

# ** Complete **




# 2. Read about and use the itertools module from the python 
#    standard library to help you solve the following problems:

#       a. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product
print(list(product('ABC', [1, 2, 3])))
len(list(product('ABC', [1, 2, 3])))                # 9 combinations

#       b. How many different combinations are there of 2 letters from "abcd"?

from itertools import combinations
print(list(combinations('ABCD', 2)))
len(list(combinations('ABCD', 2)))                  # 6 combinations

#       c. How many different permutations are there of 2 letters from "abcd"?

from itertools import permutations
print(list(permutations('ABCD', 2)))
len(list(permutations('ABCD', 2)))                  # 12 permutations


# 3. Save this file as profiles.json inside of your exercises directory 
#    (right click -> save file as...). 
#    Use the load function from the json module to open this file.

import json # Initialization

profiles = list(json.load(open('profiles.json')))   # Storing the json file into a list variable

#   a. Total number of users
print("Number of users:")
print(len(profiles))                                # Total number of users is 19

#   b. Number of active users
def number_active_users():
    i = 0
    for profile in profiles:
        if profile["isActive"] == True:
            i += 1
    return i

print("Number of active users:")
print(number_active_users())                        # Number of active users: 9

#   c. Number of inactive users

def number_inactive_users():
    i = 0
    for profile in profiles:
        if profile["isActive"] == False:
            i += 1
    return i

print("Number of inactive users:")
print(number_inactive_users())                      # Number of inactive users: 10

#   d. Grand total of balances for all users

def sum_balances():
    total = 0 # initialize total
    for profile in profiles:
        temp_balance = profile["balance"]                                   # Created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "")                # Removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "")  # Removes $ from the string
        total += float(remove_dollar_sign_balance)                          # Adds all balances in list
    return total

print("Total balances for all users:")
print("$", sum_balances())                                                  # Result: $ 52667.02

#   e. Average balance per user

def avg_balance():
    i = 0
    total = 0 # initialize total
    for profile in profiles:
        # print("User balance:", profile["balance"])                        # Used to check balances if needed
        temp_balance = profile["balance"]                                   # Created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "")                # Removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "")  # Removes $ from the string
        total += float(remove_dollar_sign_balance)                          # Adds all balances in list
        i += 1                                                              # 19 balances
    return round(total / i, 2)                                              

print("Average balance for all users:")
print("$", avg_balance())                                                   # Result: $ 2771.95


#   f. User with the lowest balance

def lowest_balance():
    lowest_balance = float("inf")
    for profile in profiles:
        temp_balance = profile["balance"]                                   # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "")                # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "")  #Removes $ from the string
        numeric_balance = float(remove_dollar_sign_balance)                 # transforms the balance into float type
        if numeric_balance < lowest_balance:
            lowest_balance = numeric_balance
    return round(lowest_balance, 2)

print("Lowest balance:")
print("$", lowest_balance())

#   g. User with the highest balance

def highest_balance():
    highest_balance = float("-inf")
    for profile in profiles:
        temp_balance = profile["balance"]                                   # created a variable to modify and keep things straight in my head
        remove_comma_balance = temp_balance.replace(",", "")                # removes commas from the string
        remove_dollar_sign_balance = remove_comma_balance.replace("$", "")  #Removes $ from the string
        numeric_balance = float(remove_dollar_sign_balance)                 # transforms the balance into float type
        if numeric_balance > highest_balance:
            highest_balance = numeric_balance
    return round(highest_balance, 2)

print("Highest balance:")
print("$", highest_balance())

#   h. Most common favorite fruit

def favorite_fruit():
    highest_fruit = ""                                      # Initializing str variable
    highest_count = 0                                       # Initializing int variable
    for profile in profiles:                                # Iterating through the list
        fruit_comparer = profile["favoriteFruit"]            # Variable to compare the below nested loop
        fruit_count = 0                                     # Initializing int variable
        for compare in profiles:                            # Nested loop to compare and count like fruit
            if fruit_comparer == compare["favoriteFruit"]:   # compare variables
                fruit_count += 1                            # Count like fruit
        if fruit_count > highest_count:                     # if statement to compare total amounts of fruits
            highest_count = fruit_count                     # Stores number of fruit
            highest_fruit = fruit_comparer                  # Stores name of fruit
    return highest_fruit                                    # Returns name of most common fruit

print("Most common favorite fruit")
print(favorite_fruit())                                     # Strawberry is the most common favorite fruit

#   i. Least most common favorite fruit

def least_favorite_fruit():
    least_fruit = ""                                        # Initializing str variable
    least_count = 1000000                                   # Initializing int variable
    for profile in profiles:                                # Loop through the list
        fruit_comparer = profile["favoriteFruit"]           # Stores fruit from each item in list to a variable
        fruit_count = 0                                     # Initializing counter before entering nested loop
        for compare in profiles:                            # Nested loop to count similar fruits
            if fruit_comparer == compare["favoriteFruit"]:  # Comparing fruit names
                fruit_count += 1                            # Counting similar names
        if fruit_count < least_count:                       # Comparing totals
            least_count = fruit_count                       # Storing the lesser amount of fruits
            least_fruit = fruit_comparer                    # Storing name of lesser amount of fruits
    return least_fruit                                      # Returns least common fruit

print("Least common favorite fruit")
print(least_favorite_fruit())                               # Apple is the least common favorite fruit

#   j. Total number of unread messages for all users

def total_unread_messages():
    total_messages = 0                          # Initialize variabe
    for profile in profiles:                    # Iterate through the list
        # print(total_messages)                 # Used to print each iteration
        greeting = profile["greeting"]          
        num_messages = ""                       # Initialiing variable
        for number in greeting:                 # Iterate through the string
            if number.isdigit():                # Check for numbers within the string
                num_messages += number          # Adding numbers to a new variable
        total_messages += int(num_messages)     # Converting string numbers to int and summing
    return total_messages                       # Output total

print("Total number of unread messages:")
print(total_unread_messages())                  # Total: 210 unread messages