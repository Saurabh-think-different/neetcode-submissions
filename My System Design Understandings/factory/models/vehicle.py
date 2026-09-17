from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def assign_driver(self):
        pass

    @abstractmethod
    def calculate_fare(self, distance):
        pass

    @abstractmethod
    def start(self):
        pass
