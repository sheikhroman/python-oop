# Inheritance

# Base class -> all Common attr & method
class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    def re_sale(self):
        print('Ready to sell again')

class Laptop(Device):
    def __init__(self, brand, price, color, disc_size) :
        super().__init__(brand, price, color)
        self.disc_size = disc_size

    def run(self):
        print('Running the laptop')

    def __repr__(self) -> str:
        return f'Laptop {self.brand} : {self.price} : {self.color}'

    def purchase(self, money, discount):
        if money < (self.price - self.price * discount/100):
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price


class Phone:
    def __init__(self, brand, price, color, camera, sim_num):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num
    
    def is_dual_sim(self):
        return self.sim_num > 1

    def __repr__(self) -> str:
        return f'Phone {self.brand} : {self.price} : {self.color}'

class Watch:
    def __init__(self, brand, price, color, watch_type):
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_degital (self):
        return self.watch_type == 'degital'


class Manager:
    def __init__(self, name, salary, experience, designation):
        pass

    def withdraw_salary(self):
        pass

    def day_total_sales(self):
        pass
    
    def handle_customer_complain(self):
        pass


class SalesPerson:
    def __init__(self, name, salary, experience, designation, comision):
        pass
    
    def withdraw_salary(self):
        pass

    def handle_customer(self):
        pass

lenovo = Laptop('Lenovo', 42000, 'Black', '500GB')
print(lenovo)
Dell = Laptop('Dell', 50000, 'Silver', '500GB')
print(Dell)
Samsung = Phone('Samsung', 1000000, 'Z-Black', '50mp', 2)
print(Samsung)
Pixel = Phone('Pixel', 90000, 'Gold', '64mp', 2)
print(Pixel)
Dell.re_sale()