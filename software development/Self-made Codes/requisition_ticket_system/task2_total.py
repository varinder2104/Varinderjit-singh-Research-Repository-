"""
In this program, we will get the order from the staff about what they need to have and also of the item and last we will total
the amount of all items for the billing and we will use the while loop.

Author = Varinderjit singh
"""


def requisitions_total():
    #this function will just ask about the items and their price that the user wants and give us the total amount at end.
    option = []
    total_cost = 0

    while True: # we use while loop to get all the items that user wants until they say done.
        item = input("Enter Item/addons you want buy (e.g. Coffee, Tea, Paper, Pen) or 'Done' to finish: ")
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price for '{item}': $ "))
            option.append((item, price))# we use append to store value in the the empty array.
            total_cost += price
            # accumulating the total amount.
        except ValueError:
            print("Invalid price, Please enter a numeric value.")
    
    return option, total_cost