from .ride_service import RideService
from models.car import Car

class CarRide(RideService):
    def create_vehicle(self):
        return Car()