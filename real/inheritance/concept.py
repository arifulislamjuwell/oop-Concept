class Vehicle:

    #class variable
    color =['black', 'white']
    wheel= [2,4]
    is_license= False

    #instance variable
    def __init__(self,name, top_speed):
        self.name= name
        self.top_speed= top_speed

    # Adds an instance variable by method
    def set_engine(self, name):
        self.engine= name

    def top_spd(self):
        return 'top speed is {}'.format(self.top_speed)
    
    def description(self):
        return 'name of the vehicle is {} vehicle color available {}, and wheel must be {}'.format(self.engine, len(self.color), self.wheel)

class MotorBike(Vehicle):
    
    #invoking the __init__ of the parent class  
    def __init__(self, name, top_speed, bike_type):
        self.bike_type= bike_type
        super().__init__(name, top_speed)

    def model_year(self, year):
        desvription= self.description()
        return desvription+ self.top_spd()+"and the model year is {}".format(year)

gixxer= MotorBike('gixxer', '130', '4 stoke')
gixxer.set_engine('fi')
print(gixxer.model_year(2019))