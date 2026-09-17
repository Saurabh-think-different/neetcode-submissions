from factories.ride_factory import RideFactory


def main():

    ride_type = "truck"
    distance = 10

    ride = RideFactory.create_ride(ride_type)

    ride.start_ride(distance)


if __name__ == "__main__":
    main()