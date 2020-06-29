from person import Person
class Passenger(Person):
    fare=""
    travelDistance=''

    def Passenger(self):
        return

    def __init__(self,fare,travelDistance,id,name,passengerType):
        Person.__init__(self,id, name, passengerType)
        self.fare=fare
        self.travelDistance = travelDistance

    def CalculateTotalFare(self):
        TotalFare = (self.fare*self.travelDistance)+((self.fare*self.travelDistance)*0.02);
        return TotalFare


    def display(self):
        print("Regular Passenger info :")
        print("----------------------------------")
        super().__str__()
        print("Fare :"+str(self.fare))
        print("Travel Distance :"+str(self.travelDistance))
        print("Total Fare With 2% Tax :"+str(self.CalculateTotalFare()))
