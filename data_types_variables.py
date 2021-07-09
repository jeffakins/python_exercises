#You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

movies = ['little mermaid', 'brother bear', 'hercules']
rental_days = 3 + 5 + 1
rental_price = 3
total_cost = len(movies) * rental_days * rental_price
print("Total cost:", total_cost)

#Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

def google_weekly_pay(pay, hours): 
    return pay * hours
def Amazon_weekly_pay(pay, hours): 
    return pay * hours
def Facebook_weekly_pay(pay, hours): 
    return pay * hours
total_pay = google_weekly_pay(400, 6) + Amazon_weekly_pay(380, 4) + Facebook_weekly_pay(350, 10)
print("Total weekly pay:", total_pay)

#A student can be enrolled to a class only if the class is not full
# and the class schedule does not conflict with her current schedule.

def can_be_enrolled(class_openings, schedule_conflict):
     return class_openings and schedule_conflict
print(can_be_enrolled(True, True))

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

def can_prod_offer_be_applied(items, expired, premium):
    return items > 2 and expired == False or premium == True
can_prod_offer_be_applied(3, False, True)


#Create a variable that holds a boolean value for each of the following conditions:
username = 'codeup'
password = 'notastrongpassword'
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
def credentials(username, password):
    length_password = len(password) >= 5
    length_username = len(username) <= 20
    password_username_notequal = username != password
    whitespace_username = username != username.strip()
    whitespace_password = password != password.strip()
    results = length_password and length_username and password_username_notequal and not whitespace_password and not whitespace_username;
print("Does the username and password meet the criteria?", credentials(username, password))
