from .vehicle import Vehicle

class Bike(Vehicle):

    def validate(self):
        print("Validating bike")

    def assign_driver(self):
        print("Assigning Driver")

    def calculate_fare(self, distance):
        return distance* 8

    def start(self):
        print("Starting Bike")