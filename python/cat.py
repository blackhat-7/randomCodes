class Cat:
    mood = 0
    hunger = 0
    energy = 0

    def __init__(self, mood=0, hunger=0, energy=0):
        self.mood = mood
        self.hunger = hunger
        self.energy = energy

    def meow(self):
        print("Meow!")

    def sleep(self):
        self.energy += 1
        self.hunger += 1
        print('Cat slept')

    def play(self):
        self.mood += 1
        self.energy -= 1
        self.meow()
        print('Cat played')

    def stats(self):
        print("mood:",self.mood)
        print("hunger:",self.hunger)
        print("energy:",self.energy)

Tom = Cat(mood=2, hunger=1, energy=3)
Tom.stats()
Tom.sleep()
Tom.stats()
Tom.play()
Tom.stats()
