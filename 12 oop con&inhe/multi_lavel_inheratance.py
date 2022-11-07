class Vehicle:
    def __init__(self, name, license, price):
        self.name = name
        self.license = license
        self.price = price
    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self, name, license, price, seat, ticket_price):
        self.seat = seat
        self.availeable_seats = seat
        self.ticket_price = ticket_price
        print('Bus init called')
        super().__init__(name, license, price)


    def sell_Tticket(self, customer_name, quantity, amount):
        self.availeable_seats -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)
        return 'No ticket'

class ACBus(Bus):
    def __init__(self):
        print('AC BUS')

class MiniBus(Bus):
    def __init__(self):
        print('This is mini BUS')
        super().__init__('Mini Bus', 'DHK125', 1200000, 15, 1200)
        
class Ticket:
    def __init__(self, owner):
        self.owner = owner

mini = MiniBus()
print(mini.name)
print(mini.seat)
print(mini.availeable_seats)