class KitKat:
    breed: str
    colour: str
    name: str
    age: int


    def __init__(self, breed: str, colour: str, name: str, age: int):
        self.breed = breed
        self.colour = colour
        self.name = name
        self.age = age

    def eat(self):
        print ('eat')