# method overloading
def add(num1, num2, num3 =0):
    return num1 + num2 +num3
# print(add(12,13))
# print(add(12,13,50))

def add2(*args, **Kwargs):
    pass

# operator overloading
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def __eq__(self, __o: object) -> bool:
        return self.__balance == __o.__balance

    def __add__(self, other):
        return self.__balance + other.__balance

my_account = Account('Sakib Al Hasan', 50000)
her_account = Account('Shishir vabi', 90000)
result = my_account + her_account
print(result)