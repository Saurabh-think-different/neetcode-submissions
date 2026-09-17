from .ride_service import RideService
from models.bike import Bike

class BikeRide(RideService):
    def create_vehicle(self):
        return Bike()
