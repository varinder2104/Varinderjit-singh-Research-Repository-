# exercise 

basket = ["banana","strawberry","kiwi"]
price=3
text="welcome to the grocery store, everything is of {} dollars."

print(text.format(price))

quantity=3
discountcode=500

myorder="i want {} differnt items under discount code of {} for {} dollars."
print(myorder.format(quantity,discountcode,price))

total= price* quantity

print(f"total price: {total}")
print(f"your item to delivery:{basket}")