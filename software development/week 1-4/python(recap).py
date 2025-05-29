# using operators


# current_mood="Happy"
# previous_mood="sad"
# upgrade_mood=input("Do you want to upgrade your mood? (yes/no)").lower()
# if upgrade_mood =="yes":
#     current_mood+=" and exicted"
#     print(f"Today, I am feeling {current_mood}.")

# else:
#     print(f"Today, I am feeling {current_mood}.")
#     print(f"yesterday, I was feeling {previous_mood}.")
#     print("I hope you have a good day.")






# guessing game 




# import random
# print("Play a game to win a prize.")

# print("Guess the secret the number from 1 to 5 to get a price.")
# random_guess= random.randint(1,5)
# print(random_guess)
# secret_number=4
# if random_guess>secret_number:
#         print("your number is higher, please try again.")
# elif random_guess<secret_number:
#      print("your number is lower, please try again.")
# else:
#      print("WOW!!!   , you WON!")








# fizzbuzz
# if any number is divisible by 3 it is fizz
# if anr number is divisible by 5 it is buzz
# if it is divisible by both 3 and 5 it is fizzbuzz




# for i in range(1,30):
#     if i%3 == 0 and i%5 ==0:
#         print("FIZZBUZZ")
#     elif i%3 ==0:
#         print("FIZZ")
#     elif i%5 ==0:
#         print("BUZZ")
#     else:
#          print("not a fizzbuzz number: ",i)








#if-elif-else exercise
# basic aritmatic calculator




# number_1=float(input("enter the first number: "))
# number_2=float(input("enter the second number: "))
# operation=input("enter the operation (+,-,*,/): ")

# if operation=="+":
#     result = number_1 + number_2
#     print(f"the sum of {number_1} and {number_2} is : {result}")
# elif operation=="-":
#     result = number_1 - number_2
#     print(f"the difference between {number_1} and {number_2} is : {result}")
# elif operation=="*":
#     result = number_1 * number_2
#     print(f"the product of {number_1} and {number_2} is : {result}")
# elif operation=="/":
#     if number_2 != 0:
#         result = number_1 / number_2
#         print(f"the quotient of {number_1} and {number_2} is : {result}")
#     else:
#         print("Error: cannot be divided by zero.")
# else:
#     print("Invalid operation. Please enter one of the following: +, -, *, / ")







# add a new contact to the list or phonebook




# contacts=[]
# name= input("Enter the name: ")
# phone_number= input("Enter the phone number: ")
# email= input("Enter the email: ")

# contact_info= f"name: {name}, phone number: {phone_number}, email: {email}"
# contacts.append(contact_info)

# # append is used to put the value of list in the array
# # here, the new contact is added into the array(contacts)

# print("\n Updated contact list: ")
# for contact in contacts:

# # and we use for loop here because it will print everything in array with the new inputs.
    
#     print(contact)







# brand name generator


# def generate_brand_name():
#     print("Welcome to the Brand name generator! ")
#     city= input("which city did you grow up in?\n")
#     pet= input("what is the name of your pet?\n")

#     brand_name=f"{city.capitalize()} {pet.capitalize()}"
#     return brand_name
# brand_name= generate_brand_name()
# print(f"Your brand name could be: {brand_name}")






# to do a countdown program


# import time
# def countdown(my_time):
#     for sec in range(my_time, 0, -1):
#         seconds= sec % 60
#         minutes= (sec // 60) % 60
#         print(f"00: {minutes:02}:{seconds:02}")
#         time.sleep(1)
#     print("Time's up!")
# countdown(60)







# exercise ticket price


def gig_ticket_price_calculator(age, is_student=False):
    if is_student and age >5:
        return 15.00
    elif age <=5:
        return 0.00
    elif age <= 28 or age >= 65:
        return 20.00
    else:
        return 30.00
    
user_age = int(input("Enter your age: "))
user_is_student= input("Are you a student? (yes/no)").lower()=="yes"
ticket_price= gig_ticket_price_calculator(user_age, user_is_student)
print(f"Gig ticket price for age {user_age} is ${ticket_price:.2f}")