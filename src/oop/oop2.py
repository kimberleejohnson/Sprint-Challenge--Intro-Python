# GroundVehicle class
class GroundVehicle():
    def __init__(self, num_wheels=4): #Num_wheels defaults to 4 if not specified when the object constructed 
        self.num_wheels = num_wheels

    # Method drive() that returns "vroooom".
    def drive(self): 
        return "vroooom"

# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle): 
    def __init__(self):
        super().__init__(2) ## Sets number of wheels to two by passing to superclass

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        super().drive() 
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles: 
    vehicle.drive()
