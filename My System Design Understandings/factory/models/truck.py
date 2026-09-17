from .vehicle import Vehicle

class Truck(Vehicle):

    def validate(self):
        print("Validating truck")

    def assign_driver(self):
        print("Assigning Driver")

    def calculate_fare(self, distance):
        return distance* 20

    def start(self):
        print("Starting Truck")