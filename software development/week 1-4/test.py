s="dogs have masters. cats have staff."
print("1.", s[1:6])
print("2.", s[:2] * 3)
print("3.", s[-3])
print("4.", s[4]+s[1])
print("5.", s[-4:])


# multifunction:
# 1
def celsius_to_fahrenhiet(celsius):
    fahrenhiet= celsius*9/5+32
    return fahrenhiet

celsius =26
print(celsius_to_fahrenhiet(celsius))    


def fun_2(age):
    years=age+10
    print("3.",years)

def fun_1(years):
    print("4.",years)
    years=20

def main():      
    years=7
    fun_1(years)
    print("1.",years)
    fun_2(years)
    print("2.",years)

#here, age=years=7  so the value of age which will program put is 7.
 
main()


# 2

def function1():
    print("A")
    function2(3)
    print("B")

def function2(num):
    print("C")
    function4(num - 1, num - 2)
    print("D")

def function3(number):
    print("E", number)

# Here, we get number=3 because in funtion2 num=3 (preassinged), then in function4 num -1 (i.e. 3-1) and num -2 (i.e. 3-2), then we get num1 = 2, num2 = 1.
#  therefore, in function3 num1 + num2 (i.e. 2+1 = 3). thats why we get E 3 in output as num1 + num2 = number (in function3).


def function4(num1, num2):
    print("F")
    function3(num1 + num2)

def Main():
    print("G")
    function1()

Main()



# 


print("Welcome to wavelength to colour converter")

value_of_wavelength=int(input("Please enter an integer wavelength between 380 and 750= "))

print(f"Thank you, the wavelength that you entered in nonometres is {value_of_wavelength}")
def wavelength(value_of_wavelength):
    if 380<=value_of_wavelength <=449:
        colour="* Violet *"

    elif 450<=value_of_wavelength<=494:
        colour="* Blue *"

    elif 495<=value_of_wavelength<=569:
        colour="* Green *"

    elif 570<=value_of_wavelength<=589:
        colour="* Yellow *"

    elif 590<=value_of_wavelength<=619:
        colour="* Orange *"

    elif 620<=value_of_wavelength<=750:
        colour="* Red *"
    
    else:
        print("invalid input")
    return colour
wavelength(value_of_wavelength)
print(f"The colour is {wavelength(value_of_wavelength)}")