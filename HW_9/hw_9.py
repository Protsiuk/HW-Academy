# homework 9

class Animal(object):
    def __init__(self, weight, is_big, speed):
        self.weight = weight
        self.is_big = is_big
        self.speed = speed

    def impuls_power(self):
        power = int(self.weight.split()[0]) * int(self.speed.split()[0])
        return power, "kg*m/s"


class CatFamily(Animal):
    def voice(self):
        return "This is animal - growls"


class DogFamily(Animal):
    def voice(self):
        return "This is animal - barks"


class Rabbit(Animal):
    pass


cat = CatFamily("10 kg", "small", "30 km/h")
dog = DogFamily("30 kg", "middle", "30 km/h")
tiger = CatFamily("170 kg", "big", "80 km/h")
wolf = DogFamily("80 kg", "big", "65 km/h")
fox = DogFamily("10 kg", "small", "50 km/h")
hare = Rabbit("6 kg", "small", "40 km/h")


def request_voice(ClassOdj):
    try:
        return ClassOdj.voice()
    except AttributeError:
        return "This is animal has not voice!"

print(request_voice(fox))
print(request_voice(cat))
print(request_voice(hare))
