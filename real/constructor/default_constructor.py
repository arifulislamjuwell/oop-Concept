class Vehicle:

    #default constructor
    def __init__(self):
        self.name= 'Fz'

    def vehicle_name(self):
        return 'the name of this vehicle is {}'.format(self.name)

fz= Vehicle()
print(fz.vehicle_name())

fz_1= Vehicle()
print(fz.vehicle_name())