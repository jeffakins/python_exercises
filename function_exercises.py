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

def is_vowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in vowels:
        if letter.lower() == vowels:
            return True
        else:
            return False

print("Input a vowel")
letter = input()
if is_vowel() == True:
    print("That is a vowel")
else:
    print("Not a vowel")
