from passenger import Passenger
from person import Person
class StudentPassenger(Passenger):

    def StudentPassenger(self):
        return None

    def __init__(self,fare,travelDistance,id,name,passengerType):
        super().__init__(fare, travelDistance, id, name, passengerType)


    def CalculateTotalFare(self):
        TotalFare = self.fare*self.travelDistance
        return TotalFare

    def CalculateTotalFare(self,dis):
        TotalFare = (self.fare*self.travelDistance)-((self.fare*self.travelDistance)*dis)
        return TotalFare

    def display(self):
        print("Staff Passenger info :")
        print("-------------------------------")
        Person.__str__(self)
        print("Potal Fare Before Discount :"+str(self.CalculateTotalFare(0)))
        print("Calculate Totafare After 70% Discount :"+str(self.CalculateTotalFare(0.7)))

