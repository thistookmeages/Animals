from animal import Animal

class Doggo(Animal):
    def __init__(self, breed: str, colour: str, name: str, age: int, loudness: float):
        super().__init__(breed, colour, name, age) 

        self.loudness = loudness
    
    def woof(self):
        print(self.name, 'says "woof" with loudness', self.loudness, '(in decibels)')

    