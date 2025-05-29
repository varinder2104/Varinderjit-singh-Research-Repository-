# if else exercise

print("Welcome to our calculator")

v=int(input("enter the first number:"))
c=int(input("enter the second number:"))

sign=input("select - or + or / or *")

if sign== "+":
    sum= v+c
elif sign== "*":
    sum=v*c
elif sign== "/":
    sum=v/c        
else:
    sum= v-c

print(f" The total is {sum}")        