class Vehicle:

    #class variable
    vehicle_type= "motorbike"
    wheel= 2

    #instance variable
    def __init__(self, bike_name, top_speed):
        self.bike_name= bike_name
        self.top_speed= top_speed

    def get_vehicle_description(self):
        print("The vehicle type is {} and the name of the bike is {} top speed {}".format(self.vehicle_type, self.bike_name, self.top_speed))

    #instance variable tyre_Size
    def tyre_description(self, tyre_size):
        print("This bike have {} wheels and the size of the tyre is {}".format(self.wheel, tyre_size))

    def byke_type(cls):
        print("The vehicle type is {}".format(cls.vehicle_type))

    @classmethod
    def byke_wheel(cls):
        print("The vehicle type is {}".format(cls.vehicle_type))

    @staticmethod
    def oil_cost_per_day(km_per_ltr, ltr_price, total_km):
        ltr_need= total_km/km_per_ltr
        return ltr_need*ltr_price

# Vehicle.byke_type= classmethod(Vehicle.byke_type)
# a= Vehicle('sd',87)c
# a.byke_type()
class Suzuki(Vehicle):

    def __init__(self, bike_name, top_speed):
        super().__init__(bike_name, top_speed)


    def oil_cost_per_day(self , km_per_ltr, ltr_price, total_km):
        ltr_need= total_km/km_per_ltr
        return ltr_need*ltr_price    

r= Suzuki('gxr', 170)
print(r.oil_cost_per_day(44, 89, 761))

a= Vehicle('gxr', 987)
a.get_vehicle_description()