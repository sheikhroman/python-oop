import hashlib
from brta import BRTA
import random
from vehicles import Bike, Car, Cng
from ride_manager import pubar
import threading


class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object):
        print(f'user: {email} already exists.')
        super().__init__(*args)

license_authority = BRTA()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exists = False
        with open('user.txt', 'r') as file:
            if email in file.read():  
                already_exists = True
                # raise UserAlreadyExists(email) 
            file.close()
        if already_exists == False:
            with open('user.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
            file.close()
        # print(self.name, 'user created')

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
        self.__trip_history = []
        self.location = location
        self.balance = balance
        
    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location

    def request_trip(self, destination):
        psss

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, fare, trip_info):
        self.balance -= fare
        self.__trip_history.append(trip_info)

class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license  = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            # print('Sorry you failed... Try again')
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            # new_vehicle = None
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = Cng(vehicle_type, license_plate, rate, self)
                pubar.add_a_vehicle(vehicle_type, self.vehicle)
            
        else:
            # print('You are not a valid driver')
            pass


    def start_a_trip(self, start, destination, fare, trip_info):
        print(f'A trip started for {self.name}')
        self.earning += fare
        self.location = destination
        # start a thread
        trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()
        self.vehicle.start_driving(start, destination)
        self.__trip_history.append(trip_info)
        

rider1 = Rider('rider1','rider1@gmail.com','rider1', random.randint(0,30), 5000)
rider2 = Rider('rider2','rider2@gmail.com','rider2', random.randint(0,30), 5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3', random.randint(0,30), 5000)

vehicle_typs = ['car','bike','cng']

for i in range(1, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'kikhobor{i}', random.randint(0,100), random.randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(random.choice(vehicle_typs),random.randint(10000, 99999), 10)

print(pubar.get_available_cars())
pubar.find_a_vehicle(rider1, random.choice(vehicle_typs), random.randint(1, 100))
pubar.find_a_vehicle(rider2, random.choice(vehicle_typs), random.randint(1, 100))
pubar.find_a_vehicle(rider3, random.choice(vehicle_typs), random.randint(1, 100))

print(rider1.get_trip_history())
print(pubar.total_income())