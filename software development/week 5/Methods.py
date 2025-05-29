class Person():

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.student = True
        self.pets = ["chico", "Barbie"]
        self.age_counter = age + 1

    # method 1: eat
    def eat(self):
        meal = input(f"What will {self.name} eat?")
        print(f"\nYum! {self.name} has eaten {meal}")


    # method 2: sleep
    def sleep(self):
        print("Good night")


    # method 3: work
    def work(self, employed):
        if employed == False:
            print(f"\nWork on ypour assessment {self.name}!")
        else:
            print(f"\n{self.name} will now go to work!")


# instances
Person_1 = Person("Lyle", "Female", 24)
Person_2 = Person("Varinder", "Male", 21)
Person_3 = Person("Ian", "Male", 20)

