import random
def calculate_ticket_price(category):
    if category == "VIP" or "vip":
        return 50.00
    elif category == "Regular" or "regular" or "REGULAR":
        return 30.00
    elif category == "Member" or "member" or "MEMBER":
        return 20.00
    elif category == "Student" or "student" or "STUDENT":
        return 15.00
    elif category == "Child" or "child" or "CHILD":
        return 00.00
    else:
        return None # Invalid category

def generate_random_seat_number():
    return random.randint(1,100)

def buy_ticket(name, category):
    ticket_price = calculate_ticket_price(category)
    if ticket_price is None:
        print("Invalid category. Please choose VIP, Regular, Member, Student, Child")
        return
    seat_number = generate_random_seat_number()

    print("\n----------------Event Ticket-----------------")
    print(f"\nName: {name}")
    print(f"Category: {category}")
    print(f"Ticket price: ${ticket_price}")
    print(f"Seat number: {seat_number}\n")
    print("-"*45)
    print("Thank you for your purchase!")
    print("Enjoy the event\n")

name= input("Enter your name: ")
category= input("Enter your ticket category (VIP, Regular, Member, Student, Child): ")
buy_ticket(name, category)