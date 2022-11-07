from abc import ABC, abstractmethod
# abstract base class

class Animal(ABC):
    def __init__(self):
        self.__name__ = 'Monkey'
    @abstractmethod
    def eat(self):
        print('eat beriany')

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        print('Moving around zoo')

class Monkey(Animal):
    def sing(self):
        print('Monkey is singing.....')

    @property
    def name(self):
        return self.__name__
    
    @name.setter
    def name(self,value):
        self.__name__ = value

    def eat(self):
        print('eating banana')
        # super().eat()

    def move(self):
        # print('Moving in trees')
        super().move()

class Tiger(Animal):
    def eat(self):
        pass
    def move(self):
        pass
    


layka = Monkey()
print(layka)
layka.eat()
layka.move()
layka.name = 'Marse'
print(layka.name)