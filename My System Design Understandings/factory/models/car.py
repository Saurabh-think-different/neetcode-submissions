from .vehicle import Vehicle

class Car(Vehicle):

    def validate(self):
        print("Validating car")

    def assign_driver(self):
        print("Assigning Driver")

    def calculate_fare(self, distance):
        return distance* 10

    def start(self):
        print("Starting Car")