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
# print(is_two(2))
# print(is_two("2"))
# print(is_two(4))

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
# print("Input a vowel") 
# letter = input()
# if is_vowel(letter) == True:
#     print("That is a vowel")
# else:
#     print("Not a vowel")



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
# print("Input a letter") 
# letter = input()
# if is_consonant(letter) == True:
#     print("That is a consonant")
# else:
#     print("Not a consonant")


# 4. Define a function that accepts a string that is a word. 
#    The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_first_letter(word):
    """Function that capitalies the first letter of a word if it's a consonant"""
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return word

# Testing that the above function works
# print("Type a word")
# word = input()
# print("Your word:")
# print(cap_first_letter(word))


# 5. Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) 
#    and the bill total, and return the amount to tip.

def calculate_tip(bill_total, tip_percentage):
    """A function to calculate a tip"""
    return round(float(bill_total) * float(tip_percentage), 2)

# Testing that the above funtion works
# print("To calculate tip amount first,")
# print("enter your bill total:")
# bill_total = input()
# print("Now enter tip percentage in decimal form:")
# tip_percentage = input()
# print("Tip amount:")
# print("$", calculate_tip(bill_total, tip_percentage))


# 6. Define a function named apply_discount. 
#    It should accept a original price, and a discount percentage, 
#    and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    """A function that will apply a discount to the price of an item"""
    discount = float(original_price) * float(discount_percent)
    discount_price = float(original_price) - discount
    return round(discount_price, 2)

# Testing that the above funtion works
# print("To calculate the price of your item after applying a discount first,")
# print("enter the price of your item:")
# original_price = input()
# print("Now enter the discount percentage in decimal form:")
# discount_percent = input()
# print("Discounted price:")
# print("$", apply_discount(original_price, discount_percent))



# 7. Define a function named handle_commas. 
#    It should accept a string that is a number that contains commas 
#    in it as input, and return a number as output. 

def handle_commas(number):
    num_no_comma = number.replace(",", "")
    return float(num_no_comma)

# Testing the above function
# print(handle_commas("3,254"))
# print(handle_commas("3,254,123,456"))



# 8. Define a function named get_letter_grade. 
#    It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(numeric_grade):
    numeric_grade = int(numeric_grade)
    if numeric_grade >= 0 and numeric_grade <= 59:
        return "F"
    elif numeric_grade >= 60 and numeric_grade <= 69:
        return "D"
    elif numeric_grade >= 70 and numeric_grade <= 79:
        return "C"
    elif numeric_grade >= 80 and numeric_grade <= 89:
        return "B"
    elif numeric_grade >= 90 and numeric_grade <= 100:
        return "A"
    else:
        return "Not valid"


# Test above
# print(get_letter_grade(55))
# print(get_letter_grade(85))
# print(get_letter_grade(95))
# print(get_letter_grade(155))



# 9. Define a function named remove_vowels
#    that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    word = word.replace("a", "")
    word = word.replace("e", "")
    word = word.replace("i", "")
    word = word.replace("o", "")
    word = word.replace("u", "")
    return word

# Test above
# print(remove_vowels("This is a test"))
# print(remove_vowels("Yo aeiou ya"))
# print(remove_vowels("Let's try this one more time"))


# 10. Define a function named normalize_name. 
#     It should accept a string and return a valid python identifier, that is:
#       - anything that is not a valid python identifier should be removed
#       - leading and trailing whitespace should be removed
#       - everything should be lowercase
#       - spaces should be replaced with underscores

def normalize_name(input_str):
    norm_str = ""
    for char in input_str:
        if char.isdigit() or char.isalpha() or char == "_" or char == " ":
            norm_str += char 
    norm_str = norm_str.strip()
    norm_str = norm_str.replace(" ", "_")
    norm_str = norm_str.lower()
    return norm_str

# Test 10. 
#normalize_name("1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@")



# 11. Write a function named cumulative_sum that accepts a list of numbers 
#     and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(list_to_sum):
    i = 0
    list_summed = []
    for number in list_to_sum:
        number += number
        list_summed[i] = number
        i += 1
    return list_summed

#       - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
print(cumulative_sum([1, 1, 1]))
#       - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]