class Vehicle:

    #parameter constructor
    def __init__(self,name, top_speed):
        self.name= name
        self.top_speed= top_speed
        super().__init__()

    def vehicle_name(self):
        return 'the name of this vehicle is {}'.format(self.name)

fz= Vehicle('gixxer', '130')
print(fz.vehicle_name())

fz_1= Vehicle('fz', "120")
print(fz_1.vehicle_name())