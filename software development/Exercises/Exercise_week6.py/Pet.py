class Pet():
    def __init__(self, species, name, age, sound):
        self.species = species
        self.name = name
        self.age = age
        self.sound = sound

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday '{self.name}', you are now {self.age} years old.")

    def display(self):
        print("\n========= Pet ==========")
        print("Species: ", self.species)
        print("Pet Name: ", self.name)
        print(f"Sound: '{self.sound}'")

if __name__ == "__main__":

    pet1 = Pet("Dog", "Tuffy", 6, "Woof!")
    pet1.display()
    pet1.birthday()

    pet2 = Pet("Cat", "Luna", 3, "Meow!")
    pet2.display()
    pet2.birthday()

    pet3 = Pet("Parrot", "Jack", 2, "Screech!")
    pet3.display()
    pet3.birthday()

    pet4 = Pet("Rabbit", "Bella", 3, "cluck!")
    pet4.display()
    pet4.birthday()