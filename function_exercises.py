# Function Exercises

# 1. Define a function named is_two. 
#    It should accept one input and return True if the passed 
#    input is either the number or the string 2, False otherwise.

def is_two(number):
    if number == 2 or number == "2":
        return True
    else:
        return False

# Testing the function:
print(is_two(2))
print(is_two("2"))
print(is_two(4))

# 2. Define a function named is_vowel. 
#    It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter): # Function to check if a letter is a vowel
    """Frunction that will return True if the passed string is a vowel"""
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        if letter.lower() == vowel:
            return True
    return False

# User input. Will check if the input is a vowel using the above function.
print("Input a vowel") 
letter = input()
if is_vowel(letter) == True:
    print("That is a vowel")
else:
    print("Not a vowel")



# 3. Define a function named is_consonant. 
#    It should return True if the passed string is a consonant, False otherwise. 
#    Use your is_vowel function to accomplish this.

def is_consonant(letter): 
    """Function that will return True if the passed string is a consonant"""
    if is_vowel(letter) == False:
        return True
    else:
        return False

# User input. Will check if the input is a consonant using the above function.
print("Input a letter") 
letter = input()
if is_consonant(letter) == True:
    print("That is a consonant")
else:
    print("Not a consonant")


# 4. Define a function that accepts a string that is a word. 
#    The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_first_letter(word):
    """Function that capitalies the first letter of a word if it's a consonant"""
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return word

# Testing that the above function works
print("Type a word")
word = input()
print("Your word:")
print(cap_first_letter(word))


# 5. Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) 
#    and the bill total, and return the amount to tip.

def calculate_tip(bill_total, tip_percentage):
    """A function to calculate a tip"""
    return round(float(bill_total) * float(tip_percentage), 2)

# Testing that the above funtion works
print("To calculate tip amount first,")
print("enter your bill total:")
bill_total = input()
print("Now enter tip percentage in decimal form:")
tip_percentage = input()
print("Tip amount:")
print("$", calculate_tip(bill_total, tip_percentage))