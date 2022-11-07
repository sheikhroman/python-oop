# abstraction class

class Book:
    def __init__(self, name):
        self.name = name
    def read(self):
        raise NotImplementedError

    def exercise(self):
        pass

class Physics (Book):
    def __init__(self, name):
        super().__init__(name)

topon = Physics('Hero Alom')
# topon.read()
topon.exercise()