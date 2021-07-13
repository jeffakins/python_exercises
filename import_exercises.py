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

from itertools import combinations
print(list(combinations('ABC123', 6)))

#       b. How many different combinations are there of 2 letters from "abcd"?

from itertools import combinations
print(list(combinations('ABCD', 2)))

#       c. How many different permutations are there of 2 letters from "abcd"?

from itertools import permutations
print(list(permutations('ABCD', 2)))
print(list(permutations('ABCD', 2)))



# 3. Save this file as profiles.json inside of your exercises directory 
#    (right click -> save file as...). 
#    Use the load function from the json module to open this file.

import json

profiles = list(json.load(open('profiles.json'))) 
#print(profiles[0])

#   Total number of users
print(len(profiles)) # Total number of users is 19

#   Number of active users
for profile in profiles:
    if profile