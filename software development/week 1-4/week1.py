print("Hello, world")

print("""hello world,
      this is a multiline string""")

a= """this is a multi line string
          for a variable"""
print(a)



# string functions

# input function
name= input("whatis your name?")
print("hello",name) 

# lenghth function
text= "Hello brother, How are you doing?" 
print(len(text))

# count function
print(text.count("h"))   
# here it will count, how many h are there in text.

# upper function
print(text.upper())

# lower finction
print(text.lower())

# join function
fruits=("banana","apple","orange")
mixed= "".join(fruits)
print(mixed)


# operations

# addition
x=5
y=34
print(x+y)

# substration
a=16
b=9
print(a-b)

# multiplication
print(x*y)
print(x*y*a)

# division
print(x/y)


# f-string - formatted string and it uses curly braces
Name= "Varinderjit singh"
age= 20

print(f"hello, i am {Name}, and i am {age} years old.")
# don't forget little f infront, otherwise it will not work.
# this is self input
# now, we ask user to input 

namE=(input("what is your name?"))
Age=(input("what is your age?"))

print(f"hello, i am {namE},and i am {Age} years old.")

# string concatenation - old method of formatting strings
print("my name is " + namE + "and i am " + Age + "years old")

# math inside the formatted string
price= 700
discount= 100

print(f"the final price is ${price - discount}")


# if elif else statement

q=20
w=45
if q>w:
    print("q is greater than w")
elif q==w:
    print("q is equal to w")
else:
    print("q is smaller than w") 



z=78
if z>=90:
    print("you got A grade")
elif z>=80:
    print("you got B grade")
elif z>=70:
    print("you got C grade")
else:
    print("you failed")                       