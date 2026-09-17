from .ride_service import RideService
from models.truck import Truck

class TruckRide(RideService):
    def create_vehicle(self):
        return Truck()
