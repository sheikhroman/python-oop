class Item:
    all = []
    def __init__(self, itemName, itemPrice) -> None:
        self.__itemName=itemName
        self.__itemPrice=itemPrice
        self.all.append(self)
    
    def __repr__(self) -> str:
        return f'Item({self.itemName}, {self.itemPrice})'

item1 =Item('Bowl', 150)
item2 =Item('Plate', 100)

# item1.discount = 10
# item1.offer = '60%'
# Item.all.append(item1)
# print(Item.all)
# print(item1.__dict__)
# print(item2.__dict__)
# print(item1.all)

item1.__discount = 10
# print(item1.__itemName)
print(item1, __dict__)