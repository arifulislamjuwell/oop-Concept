from passenger import Passenger
from studentpassenger import StudentPassenger
from transport import Transport

if __name__ == '__main__':
    name = input("enter passenger name:")
    rp = Passenger(500.0,2,"183-35-2200",name,"Regular Passenger")
    rp.display()

    passengerType = input("Enter Passenger Type :")
    sp = StudentPassenger(300.0,2,"173-35-2213","shahriar",passengerType)
    sp.display()

    t = Transport("DA-1203","Private Car","Ac")
    t.display()


