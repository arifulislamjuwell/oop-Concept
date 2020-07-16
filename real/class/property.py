class Vehicle:

    #instance variable
    def __init__(self, bike_name):
        self.bike_name= bike_name

    def get_bike_name(self):
        return self.bike_name

    def set_bike_name(self, value):
        self.bike_name= value

    def del_bike_name(self):
        del self.bike_name

    name= property(get_bike_name, set_bike_name, del_bike_name)


bike_1= Vehicle('suzuki')
print(bike_1.name)
bike_1.name= 'yamaha'
del bike_1.name
