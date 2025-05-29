import winsound
from random import choice

class Cat():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def display_data(self):
        print("Cat: ", self.name)
        print("Age: ", self.age)
        print("Color: ", self.color)

    def display(self):
        if self.color == "Purple":
            print("""\033[0;35m
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
\033[0m""")
        elif self.color == "Blue":
            print("""\033[0;34m
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
\033[0m""")
        else:
            print("Invalid input")

        
    def sound(self):
        winsound.Beep(800,900)
        print("Meow!")

cat1 = Cat("cherry", "2", "Purple")
cat2 = Cat("Jiji", "3", "Blue")

cat1.display_data()
cat1.display()
cat1.sound()
cat2.display_data()
cat2.display()
cat2.sound()
cat1.display()
cat1.sound()