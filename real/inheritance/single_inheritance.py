class Vehicle:

    #class variable
    color =['black', 'white']
    wheel= [2,4]
    is_license= False

    #instance variable
    def __init__(self,name, top_speed):
        self.name= name
        self.top_speed= top_speed

#single inheritance
class MotorBike(Vehicle):
    
    #invoking the __init__ of the parent class  
    def __init__(self, name, top_speed, bike_type):
        self.bike_type= bike_type
        super().__init__(name, top_speed)

    def model_year(self, year):
        return "and the model year is {}".format(year)

gixxer= MotorBike('gixxer', '130', '4 stoke')
print(gixxer.model_year(2019))