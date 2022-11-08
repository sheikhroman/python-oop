class User:
    # history = []
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.from_des = from_des
        self.to = to
        self.departure = departure
        self.seat = ["Empty" for i in range(20)]

class HoluCompany:
    total_bus = 5
    total_bus_lst = []

    def install(self):
        bus_no = int(input("Enter Bus No : "))
        flag = 1
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                print("BUS already installed")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus To Destination : ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,
                               bus_departure, bus_from, bus_to)

            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus successfully installed\n")


class BusCounter(HoluCompany):
    yser_list = [] #user database
    bus_seat = 20
    def revervation(self):
        bus_no = int(input('Enter bus number: '))
        for bus in self.total_bus:
            if bus_no == bus['ccoach']:
                passanger = input('Enter your name: ')
                seat_no = int(input('Enter your seat number: '))
                if seat_no - 1 > self.bus_seat:
                    print('Only 20 seats are avaibale')
                elif bus['seat'][seat_no] != 'Empty':
                    print('Seat already booked')
                else:
                    bus['seat'][seat_no - 1] = passanger
            
            else:
                print('No bus avaibale')
                break
     
        for bus in self.total_bus_lst:
            print(bus['seat'])
            


company = HoluCompany()
company.install()
# 35 minutes done
b = BusCounter()
b.revervation()