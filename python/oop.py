class Person:
    num_of_legs = 2
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def walk(self):
        print(self.name + ' is walking.')

shaunak = Person("Shaunak", 57, 175)
shilpi = Person("Shilpi", 62, 165)
print(shaunak.num_of_legs)
print(shilpi.num_of_legs)

shaunak.walk()
shilpi.walk()

name = input()
weight = input()
height = input()
person1 = Person(name, weight, height)
