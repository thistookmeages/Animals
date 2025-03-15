class Animal:
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
        print(self.name)
    
    def sleep(self):
        print('zzzZZZzzz', self.breed)

    def live(self):
        self.sleep()
        self.eat()
        self.sleep()    