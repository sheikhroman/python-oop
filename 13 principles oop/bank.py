# Incaptulation

class Account:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.__balance = initial_balance

    def deposit(self, amount):
        print(f'adding {amount} to your account')
        self._account_number = 165
        self.__balance += amount

    def withdraw(self, amount):
        print(f'withdrawing {amount} from your account')
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school):
        self.school = school
        super().__init__(holder, initial_balance)

    def get_balance(self):
        return self.__balance

Alom = StudentAccount('Alom', 50000, 'IUB')
# print(Alom.balance)
print(Alom.holder)
Alom.deposit(20000)
Alom.deposit(35000)
Alom.deposit(15000)
# print(Alom.get_balance())
# Alom.balance = 0
# print(Alom.balance)
Alom._account_number = 123
print(Alom._account_number)