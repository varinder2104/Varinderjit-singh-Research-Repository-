class Car():
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"\nThe {self.color} {self.model} is driving")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped")


# create instances of the car class
car1 = Car("Green", "\033[0;32m""Mini Cooper""\033[0m")
car2 = Car("Black", "\033[0;36m""Aston Martin""\033[0m")

# call methods on the instances

car1.drive()
car1.stop()

car2.drive()
car2.stop()