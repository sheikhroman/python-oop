class RideManager:
    def __init__(self):
        print('Ride Manager Activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cngs.append(vehicle)


    def get_available_vehicle_cars(self):
        return self.__available_cars

    def find_a_vehicle(self, rider, vehicle_type, destination):
        print('looking for a car')
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print('Sorry no cars available now')
                return False
            for car in self.__available_cars:
                print('paico', rider.location, car.driver.location)
                if abs(rider.location - car.driver.location)<10:
                    print('find a match')
                    return True
            print('looping done')

pubar = RideManager()
# 5.58