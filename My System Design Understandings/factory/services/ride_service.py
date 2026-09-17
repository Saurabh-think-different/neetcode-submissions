from abc import ABC, abstractmethod

class RideService:

    def start_ride(self, distance):

        vehicle = self.create_vehicle()

        vehicle.validate()
        vehicle.assign_driver()

        fare = vehicle.calculate_fare(distance)
        vehicle.start()

        print(f"The price of the fare is: {fare}")

    @abstractmethod
    def create_vehicle(self):
        pass