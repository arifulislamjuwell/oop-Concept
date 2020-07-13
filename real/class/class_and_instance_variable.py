class Vehicle:

    #class variable
    color =['black', 'white']
    wheel= [2,4]
    is_license= False

    #instance variable
    def __init__(self,name, top_speed):
        self.name= name
        self.top_speed= top_speed
        super().__init__()

    def top_spd(self):
        return 'top speed is {}'.format(self.top_speed)
    
    def description(self):
        return 'name of the vehicle is {} vehicle color available {}, and wheel must be {}'.format(self.name, len(self.color), self.wheel)


gixxer_2019= Vehicle('gixxer 2019', '130kmph')
print(gixxer_2019.description())

print(gixxer_2019.color)
print(Vehicle.wheel)