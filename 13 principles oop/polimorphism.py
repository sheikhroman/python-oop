# print(2+8)
# print('hello'+'bondhu')
# print([34,56]+[44,11])


# overriding
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print('Animal making sound')

class Cat(Animal):
    def __init__(Self, name):
        super().__init__(name)
    
    def make_sound(self):
        print('Mew mew')

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def make_sound(self):
        print('bhau bhau')

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print('ney ney ')


don = Cat('don')
# don.make_sound()

hitlar = Dog('hitlar')
# hitlar.make_sound()

ghora = Horse('ghora')
# ghora.make_sound()

marse = Dog('marse')

animals = [don, hitlar, ghora, marse]
for animal in animals:
    animal.make_sound()