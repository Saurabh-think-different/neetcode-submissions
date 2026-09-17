from services.car_ride import CarRide
from services.bike_ride import BikeRide
from services.truck_ride import TruckRide

class RideFactory:
    _rides = {
        "car": CarRide,
        "bike": BikeRide,
        "truck": TruckRide,
    }

    @classmethod
    def create_ride(cls, ride_type):

        ride_class = cls._rides.get(ride_type)

        if not ride_class:
            raise ValueError("Unknown ride type")

        return ride_class()
