class Cat():
    # class-level annotations (optional in most cases)
    name: None
    age: None
    isHappy: None


    # constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name
        self.age = age
        self._isHappy = isHappy

    def sound(self):
        print("Meow!")

    def display(self):
        print("\n======  Cat  ======")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Happy: ", self._isHappy)


    # getter method
    def get_isHappy(self):
        return self._isHappy
    
    # setter method
    def set_isHappy(self, new_happy):
        self._isHappy = new_happy


# inheritance
# child class

class DomesticCat(Cat):
    owner: None

    def __init__(self, owner, name, age, isHappy = True):
        super().__init__(name, age, isHappy)  # super is used to inherit the initial values that are in the parent class.
        self.owner = owner

    def display(self):
        super().display()
        print("Owner: ", self.owner)


# child class
class WildCat(Cat):
    def sound(self):
        print("Hiss!")