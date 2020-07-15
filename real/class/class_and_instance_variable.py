class Vehicle:

    #class variable
    vehicle_type= "motorbike"
    wheel= 2

    #instance variable
    def __init__(self, bike_name, top_speed):
        self.bike_name= bike_name
        self.top_speed= top_speed
    
    #instance variable tyre_Size
    def tyre_description(self, tyre_size):
        print("This bike have {} wheels and the size of the tyre is {}".format(self.wheel, tyre_size))