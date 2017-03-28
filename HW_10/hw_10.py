# homework 10
# -*- coding: utf-8 -*-

import sys
import transport

an_26 = transport.Plan("Aviation kerosene", "Yelov & Blue", "440 km/h")
honda_cbr250 = transport.TwoWheeled("Bezin A-92", "Green", "214 km/h")
zaz_968 = transport.Plan("Voter", "Invisble", "PULYA")
volvo_cx90 = transport.Car("Diesel", "grey", "190 km/h")

print(honda_cbr250.feature())
print(honda_cbr250.fly())

# print(volvo_cx90.feature())
# print(volvo_cx90.fly())

print("Color of ZAZ-968 - ", zaz_968.color, "Speed of ZAZ-968 like as", zaz_968.speed)
print(zaz_968.feature())
print(zaz_968.fly())

print("___________________\n")

# task #6.1 Iterator for FILE


class FinderDataFile(object):
    def __init__(self, filename):
        self.data = open(filename, 'r', encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.data.readline()
        if line != '':
            return line.rstrip('\n')
        raise StopIteration

kobzar = FinderDataFile('shevchenko.txt')
[print(row) for row in kobzar]
print("___________________\n")

# Task #6.2 Iterator for LIST
# Task 6.2 Variant 1


# class FinderDataList(object):
#     def __init__(self, listname):
#         self.data = listname
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             element = self.data[self.count]
#             self.count += 1
#             return element
#         except IndexError:
#             raise StopIteration

# Task 6.2 Variant 2


# class FinderDataList(object):
#     def __init__(self, listname):
#         self.data = listname
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.count <= len(self.data):
#             try:
#                 element = self.data[self.count]
#                 self.count += 1
#                 return element
#             except IndexError:
#                 raise StopIteration

# Task 6.2 Variant 3


class FinderDataList(object):
    def __init__(self, listname):
        self.data = listname

    def __iter__(self):
        return self

    def __next__(self):
        [print(element) for element in self.data]
        raise StopIteration

list_os = FinderDataList(['Windows', 'Linux', 'Mac.', 'OpenSolaris', 'Plan 9'])
[print(os) for os in list_os]
print("___________________\n")

# Task 6.3 iterator for dict


class FinderDataDict(object):
    def __init__(self, dictdata):
        self.data = dictdata

    def __iter__(self):
        return self

    def __next__(self):
        [print(self.data.get(key)) for key in self.data.keys()]
        raise StopIteration


dict_os = FinderDataDict({'Apple Inc.': 'Macintosh',
                          'Google': 'Android',
                          'Microsoft': 'Windows mobile',
                          'Canonical Ltd.': 'Ubuntu'})

[print(os) for os in dict_os]
print("___________________\n")

# Task 7 Generator

result_list = [i for i in range(0, 100, 3) if i > 0]
print(result_list)
print("___________________\n")

# Task 8 List Comprehension

result_list2 = [i for i in range(100) if i > 0 and i % 3 == 0]
print(result_list2)
