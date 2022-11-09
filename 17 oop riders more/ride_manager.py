class RideManager:
    def __init__(self) -> None:
        print('Ride manager activated')
        self.__income = 0
        self.__trip_history = []
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            vehicles= self.__available_cars
        elif vehicle_type == 'bike':
            vehicles = self.__available_bikes
        else:
            vehicles = self.__available_cng 
        
        if len(vehicles) == 0:
            print(f'Sorry no {vehicle_type} is available.')
            return False
        for vehicle in vehicles:
            # print('potential', rider.location, car.driver.location)
            if abs(rider.location - vehicle.driver.location) < 10:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print('You do not have enough money for this trip.', fare, rider.balance)
                    return False
                if vehicle.status == 'available':
                    trip_info = f'Match {vehicle_type} for {rider.name} for fare: {fare} with {vehicle.driver.name} started: {rider.location} to: {destination}'
                    print(trip_info)
                    self.__trip_history.append(trip_info)
                    vehicles.remove(vehicle)
                    rider.start_a_trip(fare, trip_info)
                    vehicle.driver.start_a_trip(rider.location, destination, fare*0.8, trip_info)
                    self.__income += fare * 0.2
                    
                    return True
                    
            # print('looping done')

pubar = RideManager()