# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#

class Vehicle(): ## Base class 
    pass


class GroundVehicle(Vehicle): ### GroundVehicle Base
    pass

class Car(GroundVehicle): 
    pass

class Motorcycle(GroundVehicle): 
    pass


class FlightVehicle(Vehicle): ### FlightVehicle Base
    pass

class Airplane(FlightVehicle): 
    pass 

class Starship(FlightVehicle): 
    pass


