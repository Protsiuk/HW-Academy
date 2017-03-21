# homework 9

class Animal(object):

    def __init__(self, weight, is_big, speed):
        self.weight = weight
        self.is_big = is_big
        self.speed = speed

    def impuls_power(self):
        return int(self.weight.split()[0])*int(self.speed.split()[0]), "kg*m/s"

class CatFamily(Animal):
    def voice(self):
        return "This is animal - growls"

class DogFamily(Animal):
    def voice(self):
        return "This is animal - barks"

Cat = CatFamily("10 kg", "small", "30 km/h")
Dog = DogFamily("30 kg", "middle", "30 km/h")
Tiger = CatFamily("170 kg", "big", "80 km/h")
Wolf = DogFamily("80 kg", "big", "65 km/h")
Fox = DogFamily("10 kg", "small", "50 km/h")
Hare = Animal("6 kg", "small", "40 km/h")

print("Dog weight-", Dog.weight)
print("Tiger power -",Tiger.impuls_power())
print("Hare speed -", Hare.speed)

