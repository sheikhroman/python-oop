""" class Item:
    def __init__(self, itemName, itemPrice) -> None:
        assert itemPrice>=0,f'error line 3, {itemPrice} is invalid'
        self.itemName=itemName
        self.itemPrice=itemPrice
   
item =Item('Plate', -90)
print(item.itemName, item.itemPrice) """

class Person:
    def __init__(self, name , phone, age) -> None:
        assert age > 13, f'Only greater then 13 is accepted'
        assert len(phone) == 11, f'Invalid phone number'
        self.name = name
        self.phone = phone
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name} {self.phone} {self.age}'

user = Person('Ronam', '01870549105', 14)
print(user)