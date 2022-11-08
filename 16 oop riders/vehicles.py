from abc import ABC, abstractmethod

class vehicle:
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 40
    }
    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self. rate =  rate
        self.driver = driver
        self.status = 'available'
        self.license_plate = license_plate
        self.speed = self.speed[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finished(self):
        pass

class Car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, rate, license_plate, driver)
    
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate, 'started')
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')

class Bike(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, rate, license_plate, driver)
    
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate, 'started')
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')

class Cng(vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, rate, license_plate, driver)
    
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.license_plate, 'started')
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip')