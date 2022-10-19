class Phone:
    manufacter = 'china'
    def __init__(self,brand,price,color):
        self.brand = brand 
        self.price = price
        self.color = color

def send_sms(self,number,text):
    sms = f'sending: {text} to {number}'
    return sms

my_phone = Phone('Oppo', 13000, 'Pink')
print(my_phone.brand,my_phone.manufacter)
her_phone = Phone('iPhone', 90000,'Z-black')
print(her_phone.brand,her_phone.manufacter)