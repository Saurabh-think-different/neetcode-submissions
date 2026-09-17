
## Factory Design UML

In Python:
Abstract class → can have implemented methods + abstract methods. You can’t instantiate it.
Interface → Python doesn’t have a separate interface keyword. Usually represented using an ABC with only abstract methods.



``` mermaid
classDiagram
direction TB
    class Vehicle {
	    +validate()
	    +assign_driver()
	    +calculate_fare(distance)
	    +start()
    }

    class RideService {
	    +start_ride(distance)
	    +create_vehicle() Vehicle
    }

    class Car {
	    +validate()
	    +assign_driver()
	    +calculate_fare(distance)
	    +start()
    }

    class Bike {
	    +validate()
	    +assign_driver()
	    +calculate_fare(distance)
	    +start()
    }

    class Truck {
	    +validate()
	    +assign_driver()
	    +calculate_fare(distance)
	    +start()
    }

    class CarRide {
	    +create_vehicle() Vehicle
    }

    class BikeRide {
	    +create_vehicle() Vehicle
    }

    class TruckRide {
	    +create_vehicle() Vehicle
    }

	<<interface>> Vehicle
	<<abstract>> RideService

    Vehicle <|.. Car
    Vehicle <|.. Bike
    Vehicle <|.. Truck
    RideService <|-- CarRide
    RideService <|-- BikeRide
    RideService <|-- TruckRide
    RideService ..> Vehicle : uses
    CarRide ..> Car : creates
    BikeRide ..> Bike : creates
    TruckRide ..> Truck : create
``` 