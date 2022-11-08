import hashlib
from brta import BRTA
import random
from vehicles import Bike, Car, Cng
from ride_manager import pubar

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('user.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, 'user created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('user.txt', 'r')as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    # print(line)
                    stored_password = line.split(' ')[1]
        file.close()
        hash_password = hashlib.md5(password.encode()).hexdigest()
        if hash_password == stored_password:
            print('Valid user')
        else:
            print('Invalid user')
        # print('password found', stored_password)


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance
        
    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location

    def request_trip(self, destination):
        psss

    def start_a_trip(self, fare):
        self.balance = fare

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license  = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            print('Sorry you failed... Try again')
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            # new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, new_vehicle)
            
        else:
            print('You are not a valid driver')


    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination

rider1 = Rider('rider1','rider1@gmail.com','hululo', random.randint(0,30), 5000)
# print(dir(rider1))
rider2 = Rider('rider1','rider2@gmail.com','hello', random.randint(0,30), 5000)
# print(dir(rider2))

driver1 = Driver('driver1', 'driver1@gmail.com', 'kikhobor', random.randint(0,30), 5463)
driver1.take_driving_test()
driver1.register_a_vehicle('car',1234, 10)
driver2 = Driver('driver2', 'driver1@gmail.com', 'valoaco', random.randint(0,30), 5463)
driver2.take_driving_test()
driver2.register_a_vehicle('car',1234, 10)

print(pubar.get_available_vehicle_cars())
pubar.find_a_vehicle(rider1, 'car', 90)