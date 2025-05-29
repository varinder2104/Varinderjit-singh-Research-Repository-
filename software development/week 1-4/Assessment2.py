# 1
# to calculate the person's age

name=(input("what is your name= ")) 
age=int(input("what is your year of birth= "))
presentyear=int(input("what is the current year= "))
currentage=presentyear-age

print(f"Hello {name}, you are now {currentage} years old. Wow!!!")



# 2
a=42
b=3.14
c="Hello, World!"
d=[1,2,3]
e=(1,2,3)
f={"name":"John","age":30}

# 2a type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# 2b convert
print(str(b))

#2c exponential
import math
exponential_b = math.exp(b)
print(exponential_b)

# 2d modulus
print(a % b)

# 2e operators
a += 5
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 7
print(a)

# 2f upper case
print(c.upper())

#  2g concatenate
x=str(a)
y=str(b)
result=x+y
print(f"result is {result}")