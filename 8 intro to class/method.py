class Phone:
    color='Black',
    features=['camera','water proof','type-c']

    def call(self):
        print('ring ring ring')
    def send_sms(self, number, text):
        sms= f'sending sms: {text} to: {number}'
        return sms

my_phone =Phone()
my_phone.call()
sms = my_phone.send_sms('012457846','I never miss you')
print(sms)