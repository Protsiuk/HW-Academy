# homework 10
# Class main


class Transport:
    def __init__(self, fuel, color, speed):
        self.fuel = fuel
        self.color = color
        self.speed = speed

    def fly(classobj):
        try:
            return classobj._fly()
        except AttributeError:
            return "This is a transport can't be flying"


# Children class - TwoWheeled


class TwoWheeled(Transport):
    __weight = 100

    def feature(self):
        return "This is a transport has two wheeles, and has carrying capacity (ton)-" + str(self._carrying_capacity())

    def _carrying_capacity(self):
        return self.__weight/1000

# Children class - Car


class Car(Transport):
    __weight = 2300

    def feature(self):
        return "This is a transport has four or more wheeles, and has carrying capacity (ton)-" + \
               str(self._carrying_capacity())

    def _carrying_capacity(self):
        return self.__weight/1000


# Children class - Plan


class Plan(Transport):
    __weight = 3000

    def _fly(self):
        return "It is can be flying"

    def feature(self):
        return "This is a transport has two wings, and has carrying capacity (ton)-" + str(self._carrying_capacity())

    def _carrying_capacity(self):
        return self.__weight/1000
