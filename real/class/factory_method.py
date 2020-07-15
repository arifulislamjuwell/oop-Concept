class Vehicle:

    #class variable
    vehicle_type= "motorbike"
    wheel= 2
    max_top_speed= 150

    #instance variable
    def __init__(self, bike_name, top_speed):
        self.bike_name= bike_name
        self.top_speed= top_speed
    

    def byke_description(self):
        print("Bike name is {} and top speed {}".format(self.bike_name, self.top_speed))

    @classmethod
    def byke_type(cls, bike_name, speed_less_than_max):
        return cls(bike_name, cls.max_top_speed-speed_less_than_max)

# Vehicle.byke_type= classmethod(Vehicle.byke_type)
# a= Vehicle('sd',87)c
# a.byke_type()
a= Vehicle.byke_type('gixxer', 20)
a.byke_description()